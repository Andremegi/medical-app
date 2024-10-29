FROM python:3.10.6-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY tabular_data tabular_data

CMD uvicorn tabular_data.apifile:app --host 0.0.0.0 --port $PORT
