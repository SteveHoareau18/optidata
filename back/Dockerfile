FROM python:3.12-alpine

COPY . /app

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    python3-dev \
    py3-setuptools \
    py3-pip \
    && pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]