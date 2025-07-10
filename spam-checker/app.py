from flask import Flask, request

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_spam():
    content = request.json.get('content', '')
    spam_keywords = ['win', 'lottery', 'prize']
    is_spam = any(word in content.lower() for word in spam_keywords)
    return {"spam": is_spam}

app.run(host='0.0.0.0', port=5001)
