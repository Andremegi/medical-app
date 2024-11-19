import os
from google.cloud import storage
from chat_bot.params import *
from transformers import AutoTokenizer, AutoModelForCausalLM

# Only use it to save the big model from your computer to Google cloud
def upload_model_tokenizer_to_gcs(local_path):
    """
    Uploads folders with model and tokenizer recursively to a GCS bucket.
    """
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    for target in ["model", "tokenizer"]:
        target_path = os.path.join(local_path, target)
        for root, dirs, files in os.walk(target_path):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)

                # Upload the file
                gcs_path=f"chat_bot/{target}/{file_name}"
                blob = bucket.blob(gcs_path)
                blob.upload_from_filename(local_file_path)
                print(f"✅ Uploaded {local_file_path} to gs://{BUCKET_NAME}/{gcs_path}")

def load_model_tokenizer_from_gcs():
    # Check if the model exists locally
    if os.path.exists(LOCAL_MODEL_PATH):
        print(f"✅ Model found locally at {LOCAL_MODEL_PATH}")
    else:
        print("❌ Model not found locally. Fetching from GCS...")
        # Load model from GCS
        try:
            client = storage.Client()
            bucket = client.bucket(BUCKET_NAME)

            for target in ["model", "tokenizer"]:
                gcs_folder_path = f"chat_bot/{target}"
                blobs = bucket.list_blobs(prefix=gcs_folder_path)

                for blob in blobs:
                    # Compute relative path to recreate the structure locally
                    relative_path = os.path.relpath(blob.name, gcs_folder_path)
                    local_file_path = os.path.join(LOCAL_MODEL_PATH, target, relative_path)

                    # Create necessary local directories
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                    # Download the file
                    blob.download_to_filename(local_file_path)
                    print(f"✅ Downloaded {blob.name} to {local_file_path}")
        except Exception as e:
            print(f"❌ Error loading model from GCS: {str(e)}")
            return None, None

    model = AutoModelForCausalLM.from_pretrained(os.path.join(LOCAL_MODEL_PATH, "model"))
    tokenizer = AutoTokenizer.from_pretrained(os.path.join(LOCAL_MODEL_PATH, "tokenizer"))

    print("✅ Model and tokenizer loaded successfully")
    return model, tokenizer

def chat_with_bot(model, tokenizer, user_input, chat_history=None):
    if chat_history is None:
        chat_history = ""

    # Append the user's input to the chat history
    chat_history += f"User: {user_input} </s> Bot:"

    # Tokenize the input text and chat history
    inputs = tokenizer(chat_history, return_tensors="pt", truncation=True)
    input_ids = inputs['input_ids'].to(model.device)
    attention_mask = inputs['attention_mask'].to(model.device)

    # Generate the bot's response
    output_ids = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=150,  # Increase token length
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,  # Prevent repeating n-grams
        do_sample=True,  # Enable sampling for better variety
        temperature=0.7,  # Control randomness for coherent output
        num_beams=5,  # Use more beams for diversity and coherence
        num_return_sequences=1,  # Return only one coherent response
        top_p=0.9,  # Use nucleus sampling
        early_stopping=True,  # Stop when a logical endpoint is reached
    )

    # Decode and return the bot's response
    response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Update the chat history with the bot's response
    chat_history += f"{response} </s>"
    return response, chat_history
