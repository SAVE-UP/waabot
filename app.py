from flask import Flask, request, make_response, jsonify
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply
app = Flask(__name__)



@app.route("/")
def index():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

@app.route("/webhook", methods=['GET','POST'])
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return "{'fulfillmentText': 'This is a response from webhook.'}"

def response():
    # function for responses
    return make_response(jsonify(results()))

if __name__ == "__main__":
    app.run(debug=True)