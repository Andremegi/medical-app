import os

from chat_bot.model import chat_with_bot, load_model_tokenizer_from_gcs

if __name__ == "__main__":
    model, tokenizer = load_model_tokenizer_from_gcs()

    user_input = "I’ve been feeling a bit under the weather lately. I have a sore throat and a cough. Should I go see a doctor?"
    bot_reply, _ = chat_with_bot(model, tokenizer, user_input)
    print(bot_reply)
