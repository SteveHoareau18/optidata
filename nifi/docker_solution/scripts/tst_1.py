import yfinance as yf
import json
import re
import requests
import numpy as np
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import mysql.connector
from mysql.connector import Error

# -----------------------------
# Extraction du nom d'entreprise depuis la question
# -----------------------------
def extract_company_from_question(question):
    """
    Utilise un pipeline NER basé sur Transformers pour extraire le nom d'une entreprise
    depuis la question.
    """
    # Chargement du tokenizer et du modèle NER pour le français
    tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")
    ner_pipeline = pipeline(
        "ner",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="simple"
    )
    
    ner_results = ner_pipeline(question)
    companies = [entity["word"].strip() for entity in ner_results if entity.get("entity_group") == "ORG"]
    
    # Si aucune entité n'est trouvée, on vérifie manuellement la présence de "tesla"
    if not companies and "tesla" in question.lower():
        companies.append("Tesla")
        
    return companies

# -----------------------------
# Récupération du ticker via Yahoo Finance
# -----------------------------
def get_ticker_from_company_name(company_name):
    """
    Interroge l'API Yahoo Finance pour obtenir le ticker associé au nom de l'entreprise.
    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": company_name, "quotesCount": 1, "newsCount": 0}
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur lors de la récupération des données (code {response.status_code}).")
        return None

    try:
        data = response.json()
    except Exception as e:
        print("Erreur lors de la conversion de la réponse en JSON :", e)
        return None

    try:
        ticker = data["quotes"][0]["symbol"]
        return ticker
    except (IndexError, KeyError) as e:
        print("Erreur lors de l'extraction du ticker :", e)
        return None

# -----------------------------
# Génération d'une requête SQL SELECT pour récupérer les données sur 6 mois
# -----------------------------
def generate_sql_select(ticker):
    """
    Génère une requête SQL permettant d'extraire les données boursières de l'entreprise
    identifiée par le ticker sur les six derniers mois.
    La table utilisée est 'stock_data' et l'on suppose que la colonne stock_date est au format DATE.
    """
    sql = (
        f"SELECT * FROM AMB.financial_data "
        f"WHERE ticker = '{ticker}' "
        f"AND AMB.financial_data >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);"
    )
    return sql

# -----------------------------
# Connexion à la base de données MySQL et exécution de la requête
# -----------------------------
def execute_sql_query(sql_query):
    """
    Se connecte à la base de données MySQL et exécute la requête SQL fournie.
    """
    try:
        # Paramètres de connexion à la base de données dans un conteneur Docker
        connection = mysql.connector.connect(
            host='mariadbs',          # Nom du service Docker ou l'adresse IP du conteneur
            database='AMB',  # Nom de votre base de données
            user='nifi_user',  # Nom d'utilisateur de la base de données
            password='nifi_password'  # Mot de passe de la base de données
        )

        if connection.is_connected():
            print("Connexion réussie à la base de données")

            # Création d'un curseur pour exécuter la requête
            cursor = connection.cursor()

            # Exécution de la requête SQL
            cursor.execute(sql_query)

            # Récupération des résultats
            records = cursor.fetchall()

            # Affichage des résultats
            print(f"\n=== Résultats de la requête ===")
            for row in records:
                print(row)

    except Error as e:
        print("Erreur lors de la connexion ou de l'exécution de la requête :", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("\nConnexion à la base de données fermée")

# -----------------------------
# Programme principal
# -----------------------------
if __name__ == "__main__":
    # Question posée
    question = input("Posez votre question sur l'actualité : ").strip()
    print("Question :", question)
    
    # Extraction du nom d'entreprise depuis la question grâce au LLM (NER)
    companies = extract_company_from_question(question)
    if not companies:
        print("Aucune entreprise identifiée dans la question.")
        exit(0)
    
    # Pour ce cas, on prend la première entreprise extraite
    company = companies[0]
    print("Entreprise identifiée :", company)
    
    # Récupération du ticker via Yahoo Finance
    ticker = get_ticker_from_company_name(company)
    if not ticker:
        print(f"Ticker non trouvé pour l'entreprise '{company}'.")
        exit(0)
    print("Ticker identifié :", ticker)
    
    # Génération de la requête SQL permettant de trouver les données pour les 6 derniers mois
    sql_query = generate_sql_select(ticker)
    print("\n=== Requête SQL générée ===")
    print(sql_query)

    # Exécution de la requête SQL
    execute_sql_query(sql_query)
