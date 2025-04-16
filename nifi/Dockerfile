FROM apache/nifi:1.27.0

USER root

RUN apt-get update && \
    apt-get install -y python3.10 python3.10-distutils python3.10-venv python3-pip && \
    apt-get clean

RUN pip3.10 install --no-cache-dir yfinance==0.2.54 numpy==2.2.2 pandas==2.2.3

WORKDIR /data

RUN mkdir -p /data/drivers && chmod -R 777 /data/drivers

RUN cd /data/drivers && \
    wget -O mariadb-java-client-3.5.0.jar https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.0/mariadb-java-client-3.5.0.jar && \
    wget -O mysql-connector-j-8.0.33.jar https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar && \
    ls -lah /data/drivers

RUN cp /data/drivers/*.jar /opt/nifi/nifi-current/lib/
RUN chown -R nifi:nifi /data/drivers /opt/nifi/nifi-current/lib/

WORKDIR /opt/nifi/nifi-current

USER nifi

