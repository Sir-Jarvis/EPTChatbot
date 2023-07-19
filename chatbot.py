import openai
from transformers import pipeline

# Clé API d'OpenAI - Remplacez 'VOTRE_CLE_API' par votre propre clé API
openai.api_key = 'VOTRE_CLE_API'

# Charger le modèle French_semantic de Hugging Face
model_name = "iarfmoose/gpt2-finetuned-scratch-chatbot-french"
chatbot = pipeline('text-generation', model=model_name, tokenizer=model_name)

# Lire les documents à partir du fichier
def read_documents_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        documents = file.read().split("\n")  # Séparer les documents par sauts de ligne
    return documents

# Rechercher une réponse dans les documents en fonction de la question
def search_response_in_documents(question, documents):
    for document in documents:
        if question in document:
            return document
    return None

# Utiliser le chatbot pour répondre à une question donnée
def get_chatbot_response(question, documents):
    response = search_response_in_documents(question, documents)
    if response:
        return response
    else:
        # Utiliser l'API d'OpenAI pour générer une réponse
        prompt = "Quels autres renseignements souhaitez-vous connaître sur l'École Polytechnique de Thiès ?"
        openai_response = openai.Completion.create(
            engine="text-davinci-002",  # Modèle GPT-3 d'OpenAI
            prompt=prompt + " " + question,
            max_tokens=100,
            stop=["\n", "ChatGPT:"],  # Arrêter la réponse après une ligne vide ou le début d'une nouvelle réponse
        )
        return openai_response['choices'][0]['text'].strip()

# Charger les documents à partir du fichier ou se trouvent les donnees.
documents_file_path = "ept_data.txt"
documents = read_documents_from_file(documents_file_path)
