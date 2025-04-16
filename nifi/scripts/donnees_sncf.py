import requests
import json
import sys

def fetch_sncf_data():
    url = "https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/regularite-mensuelle-ter/records"
    params = {
        "where": "region in ('Occitanie', 'Auvergne-Rhône-Alpes') and date > '2020-12'",
        "order_by": "date desc",
        "limit": 100
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        seen_keys = set()

        for record in data.get("results", []):
            if "date" in record and len(record["date"]) == 7:
                record["date"] += "-01"

            key = f"{record.get('date')}_{record.get('region')}"
            if key in seen_keys:
                continue
            seen_keys.add(key)

            print(json.dumps(record, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    fetch_sncf_data()
