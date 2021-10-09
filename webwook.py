from flask import Flask, request, make_response, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)


@app.route('/')  # this is the home page route
def hello_world():  # this is the home page function that generates the page code
    return "Hello world!"


@app.route('/sms', methods=['GET','POST'])
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

if __name__ == '__main__':
    app.run(debug=True)  # This line launch the program