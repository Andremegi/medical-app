FROM python:3.10.6-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY images images
COPY models models

CMD uvicorn images.apifile:app --host 0.0.0.0 --port $PORT
