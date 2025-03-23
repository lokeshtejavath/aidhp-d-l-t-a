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
    
#TODO
@app.route('/userInfo', methods=['POST'])
def userInfo():
    #params from Santander dataset
    params = ["Customer code","Employee index: A active, B ex employed, F filial, N not employee, P pasive","Customer's Country residence","Customer's sex","Age","The date in which the customer became as the first holder of a contract in the bank","New customer Index. 1 if the customer registered in the last 6 months.","Customer seniority (in months)","1 (First/Primary), 99 (Primary customer during the month but not at the end of the month)","Last date as primary customer (if he isn't at the end of the month)","Customer type at the beginning of the month ,1 (First/Primary customer), 2 (co-owner ),P (Potential),3 (former primary), 4(former co-owner)","Customer relation type at the beginning of the month, A (active), I (inactive), P (former customer),R (Potential)","Residence index (S (Yes) or N (No) if the residence country is the same than the bank country)","Foreigner index (S (Yes) or N (No) if the customer's birth country is different than the bank country)","Spouse index. 1 if the customer is spouse of an employee","channel used by the customer to join","Deceased index. N/S","Addres type. 1, primary address","Province code (customer's address)","Province name","Activity index (1, active customer; 0, inactive customer)","Gross income of the household","segmentation: 01 - VIP, 02 - Individuals 03 - college graduated","Saving Account","Guarantees","Current Accounts","Derivada Account","Payroll Account","Junior Account","Más particular Account","particular Account","particular Plus Account","Short-term deposits","Medium-term deposits","Long-term deposits","e-account","Funds","Mortgage","Pensions","Loans","Taxes","Credit Card","Securities","Home Account","Payroll","Pensions","Direct Debit"]
    client = genai.Client(api_key = GEMINI_API_KEY)


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
    for i in range(len(userInfoArray)):
        responseTextBox += userInfoArray[i] + " "
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
    dummyData = {"customer code": "Customer code","employee index": "Employee index","country residence": "Customer's Country residence","age": "Customer Age","seniority": "Customer seniority (in months)","channel": "channel used by the customer to join","gross income of the household": "Gross income of the household","segmentation": "01 - VIP, 02 -Individuals, 03 - college graduated","saving account": "Saving Account","guarantees": "Guarantees","current accounts": "Current Accounts","derivada account": "Derivada Account","payroll account": "Payroll Account","junior account": "Junior Account","más particular account": "Más particular Account","particular account": "particular Account","particular plus account": "particular Plus Account","short-term deposits": "Short-term deposits","medium-term deposits": "Medium-term deposits","long-term deposits": "Long-term deposits","e-account": "e-account","funds": "Funds","mortgage": "Mortgage","pensions": "Pensions","loans": "Loans","taxes": "Taxes","credit card": "Credit Card","securities": "Securities","home account": "Home Account","payroll": "Payroll","pensions": "Pensions","direct debit": "Direct Debit"}
    return json.dumps(dummyData), 200


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
    userInfoArray = request.json['userInfo']
    print(userInfoArray)
    imagePath = 'resources/img/25473.png'
    reasonText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse consectetur diam molestie orci varius rutrum. Donec consectetur quis justo ut dignissim. Phasellus hendrerit finibus bibendum. Sed iaculis ipsum vel placerat laoreet. Ut eu arcu eu nisl commodo scelerisque. Nunc sed laoreet quam. Morbi sed tempus orci.'
    responseImg = []
    for i in range(3):
        responseImg.append({"productName":"alpha"+i,"productImage":imagePath})
    return json.dumps({'response':responseImg,"reason":reasonText}), 200



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=6969)
    