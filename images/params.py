import os

LOCAL_MODEL_PATH =  os.path.join(os.path.expanduser('~'), ".lewagon", "medical_app", "images")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
MODEL_TARGET = os.environ.get("MODEL_TARGET")
