from flask import Flask, request, make_response, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)


@app.route('/')  # this is the home page route
def hello_world():  # this is the home page function that generates the page code
    return "Hello world!"


@app.route('/sms', methods=['POST'])
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


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    sum = 0
    query_result = req.get('queryResult')
    num1 = int(query_result.get('parameters').get('number1'))
    num2 = int(query_result.get('parameters').get('number2'))
    sum = str(num1 + num2)
    print('here num1 = {0}'.format(num1))
    print('here num2 = {0}'.format(num2))
    return {
        "fulfillmentText": 'The sum of the two numbers is: ' + sum,
        "source": "webhookdata"
    }

if __name__ == '__main__':
    app.run(debug=True)  # This line launch the program