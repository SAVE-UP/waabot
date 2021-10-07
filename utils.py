import os
import json
from google.protobuf.json_format import MessageToJson

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "wabot-ao9v-277bd4f17abb.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "wabot-ao9v"

def detect_intent_from_text(text, session_id, language_code='fr'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(query, session_id):
    response = detect_intent_from_text(query,session_id)
    print(response.intent.display_name)
    fulfillmentText = ""
    som = 0
    if response.intent.display_name == 'achat.bitcoin':  # Intent Name comparison
        resp1 = response.parameters.fields["number1"]
        num1 = json.loads(MessageToJson(resp1))
        resp2 = response.parameters.fields["number2"]
        num2 = json.loads(MessageToJson(resp2))
        som = str(num1 + num2)
        fulfillmentText = "La somme des deux nombre est: "+som
        return fulfillmentText
    elif response.intent.display_name == 'achat.etherum':
        return "N/A"
    elif response.intent.display_name == '':
        return "N/A"
    else:
        return response.fulfillment_text

#response.fulfillment_text