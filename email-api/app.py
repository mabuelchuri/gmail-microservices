from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_email():
    data = request.json
    email = data.get('email')
    content = data.get('content')

    # Call spam-checker service
    response = requests.post("http://spam-checker:5001/check", json={"content": content})
    if response.json()['spam']:
        return {"status": "rejected", "reason": "spam"}, 403

    # Forward to mail-storage
    requests.post("http://mail-storage:5002/store", json={"email": email, "content": content})
    return {"status": "sent"}, 200

app.run(host='0.0.0.0', port=5000)
