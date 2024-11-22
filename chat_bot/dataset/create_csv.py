import os
import pandas as pd

# Path to the folder containing the disease files
folder_path = os.path.dirname(os.path.abspath(__file__))

# List to store the data for the CSV file
data = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Only process text files
    if filename.endswith(".txt"):
        # Get the disease name from the filename (lowercase)
        disease = filename.split('.')[0].lower()

        # Read the content of the file
        with open(os.path.join(folder_path, filename), 'r') as file:
            file_content = file.read().strip()

            # Split the content into separate conversations
            conversations = [conv.strip() for conv in file_content.split('\n\n') if conv.strip()]

            # Append each conversation as a new row
            for conv in conversations:
                data.append([conv, disease])

# Create a DataFrame
df = pd.DataFrame(data, columns=["conversations", "disease"])

# Save the DataFrame to a CSV file
output_file = os.path.join(folder_path, "medical_conversations.csv")
df.to_csv(output_file, index=False)

print(f"CSV file has been created: {output_file}")
