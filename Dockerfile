FROM python:3.10.6-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY setup.py setup.py

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

COPY images images
COPY text_data text_data
COPY chat_bot chat_bot

CMD uvicorn images.api:app --host 0.0.0.0 --port $PORT
