# EPTChatbot
 Chatbot de l'École Polytechnique de Thiès

Ce projet est un chatbot personnalisé pour l'École Polytechnique de Thiès. Le chatbot est capable de répondre aux questions sur l'école à partir des données fournies dans le fichier `documents.txt`. Il utilise l'API d'OpenAI pour générer des réponses lorsque les informations ne sont pas trouvées dans les documents.

## Exigences

- Python 3.9 ou supérieur
- Clé API d'OpenAI (pour utiliser leur service d'API)

## Installation

1. Clonez le dépôt vers votre machine locale :

-- bash -- command line
git clone git@github.com:Sir-Jarvis/EPTChatbot.git
cd EPTChatbot

2. Installez les dépendances nécessaires :
pip install -r requirements.txt

3. Ajoutez votre clé API d'OpenAI dans le fichier chatbot.py :
# Clé API d'OpenAI - Remplacez 'VOTRE_CLE_API' par votre propre clé API. La clé est payante
openai.api_key = 'VOTRE_CLE_API'

4. Pour exécuter le chatbot en utilisant l'interface web, utilisez la commande suivante :
python app.py

Cela démarrera le serveur Flask. Vous pouvez maintenant accéder à l'interface web du chatbot en ouvrant votre navigateur et en accédant à l'URL http://localhost:5000/.

Pour poser des questions au chatbot directement depuis la console, vous pouvez utiliser la fonction get_chatbot_response() dans le fichier chatbot.py. Voici un exemple :

from chatbot import get_chatbot_response, documents

''' 
user_question = "Quels sont les programmes académiques offerts par l'École polytechnique de Thiès ?"
response = get_chatbot_response(user_question, documents)
print("Réponse du chatbot :")
print(response)
'''

Déploiement
Vous pouvez déployer ce chatbot sur une plateforme d'hébergement telle que Heroku(ce qui n'a pas marché avec moi vu la ùéthode de paiement) ou sur pythonanywhere(rencontre de quelques erreurs ppour creer l'environnement virtuel) ou bien sur netlify.

Auteur
Cheikh LO


