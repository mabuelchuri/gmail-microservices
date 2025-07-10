from flask import Flask, request

app = Flask(__name__)
mailbox = []

@app.route('/store', methods=['POST'])
def store_mail():
    data = request.json
    mailbox.append(data)
    print("Current mailbox:", mailbox)
    return {"status": "stored"}, 200

app.run(host='0.0.0.0', port=5002)
