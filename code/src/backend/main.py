from flask import Flask,json, jsonify, request
from google import genai
import requests
import os
from dotenv import load_dotenv

GEMINI_API_KEY = os.getenv("gemini_Key")


app = Flask(__name__)


@app.route('/healthCheck', methods=['GET'])
def healthCheck():
    return json.dumps({'status': 'ok',"working":True}), 200


@app.route('/whyGenAI', methods=['POST'])
def whyGenAI():
    print(GEMINI_API_KEY)
    client = genai.Client(api_key = GEMINI_API_KEY)
    prompt = request.json['prompt']
    res = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents=prompt
    )

    print(res.text)
    return res.text, 200
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=6969)
    