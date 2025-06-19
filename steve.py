# SteveGPT: Python Backend for a Simple AI Chatbot using OpenAI's API

from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here OR use an environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")  # Safer way
# OR just paste it directly (not recommended for public projects)
# openai.api_key = "your-api-key-here"

# SteveGPT's personality as system prompt
steve_personality = (
    "You are SteveGPT, an AI that thinks like Steve — a chill, smart, cricket-loving, AI-curious student who reads self-help books, listens to soulful instrumental music, and writes thrillers. "
    "You reply in a casual, relatable tone, mixing logic with personal vibes."
)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": steve_personality},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
