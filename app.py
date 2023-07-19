from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response, documents

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.form['user_input']
    response = get_chatbot_response(user_question, documents)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
