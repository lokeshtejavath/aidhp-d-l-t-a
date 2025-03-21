from flask import Flask,json, jsonify


app = Flask(__name__)


@app.route('/healthCheck')
def healthCheck():
    return json.dumps({'status': 'ok',"working":True}), 200




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=6969)
    