from flask import Flask,json, jsonify, request
from google import genai
from flask_cors import CORS 
import os
from dotenv import load_dotenv
import Inference

GEMINI_API_KEY = os.getenv("gemini_Key")


app = Flask(__name__)
CORS(app)


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
    

"""
@request body
{
    userInfo: array of strings
}

@response body
{
    response: str
}
"""
@app.route('/gatherInfo',methods=['POST'])
def gatherInfo():
    userInfoArray = request.json['userInfo']
    print(userInfoArray)
    responseTextBox = ""
    prompt = "you are a bank employee and you are trying to gather information about a customer with the following details: "
    for i in range(len(userInfoArray)):
        prompt += ", " + userInfoArray[i] + " "
    prompt += " now please summarize the information you have gathered in a paragraph and your answer will be shown to user do not predict what user wants but simply summarize the information you have gathered do not put okay in start, but start with Based on the information we have gathered, "
    print(prompt)
    client = genai.Client(api_key = GEMINI_API_KEY)
    res = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents=prompt
    )
    responseTextBox = res.text
    # for i in range(len(userInfoArray)):
    #     responseTextBox += userInfoArray[i] + " "
    print(responseTextBox)
    return json.dumps({'response':responseTextBox}), 200


"""
@request body
{
    userInfo: str
}

@response body
{
    response: json
}
"""
@app.route('/columnData',methods=['POST'])
def columnData():
    columnData = request.json['userInfo']
    customerID = request.json['customerID']
    data = Inference.customer_info(customerID)
    # data = {"Customer code":15898,"Employee index: A active, B ex employed, F filial, N not employee":"A","Customer's Country residence":"ES","Customer":"Dafasdf"}
    return json.dumps(data), 200


"""
@request body
{
    userInfo: json
}
@response body
{
    response: {
        responseImg : array of json {productName : str, productImage : imgPath},
        reasonText : str
    }
}

"""
@app.route('/preferedProducts',methods=['POST'])
def preferedProducts():
    # userInfoArray = request.json['userInfo']
    customerID = request.json['customerID']
    userSummary = request.json['userSummary']
    userInfo = Inference.customer_info(customerID)
    test,test2 = Inference.infer(customerID)
    imagePath = 'resources/img/25473.png'
    responseImg = []
    prompt = f'user summary is this {userSummary}, and we have suggested these products'
    for i in test:
        prompt += ", " + i + " "
    if test2.count != 0:
        prompt += "and we have also suggested these loans"
        for i in test2:
            prompt += ", " + i + " "
    prompt+= " about the customer is "
    for key in userInfo:
        prompt += f", {key} is {userInfo[key]}"
    prompt+=", now as bank employee explain it to the customer why these products are suggested, but start with Based on the information we have gathered, please do not refer to customer, your answer will be read by bank employee for customer, it should in lines of 'Based on the information we have gathered, we have suggested these products to you because'"

    client = genai.Client(api_key = GEMINI_API_KEY)
    res = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents=prompt
    )
    # responseImg = []
    # imagePath = 'resources/img/25473.png'
    # res = {"text":"alha omega"}
    for i in range(3):
        responseImg.append({"productName":test[i],"productImage":imagePath})
    return json.dumps({'response':responseImg,"reason":res.text}), 200



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=6969)
    