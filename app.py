from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'sk-None-npfGjCBxf0hzIKMsadtQT3BlbkFJB1a9aZsR0a4L4KESV4sS'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are a mental health support chatbot. Answer the following question empathetically and informatively: {user_input}",
            max_tokens=150
        )
        message = response.choices[0].text.strip()
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
