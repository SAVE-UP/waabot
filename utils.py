import os
import json
from google.protobuf.json_format import MessageToJson
from getcryptoprice import getbtcprice

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
    print(response.intent.display_name) # For Debug Purpose
    fulfillmentText = ""
    som = 0
    btcmarge = 0.01 # Marge bénéficiaire ajoutez au prix normal du btc
    if response.intent.display_name == '3.1.a.get.price.cfa':   # Intent Name comparison
        btcCurentprice = float(getbtcprice().replace(',', "")) # Prix en EURO
        print(btcCurentprice)
        btcKaderPrice = btcCurentprice + (btcCurentprice * btcmarge)
        usrQtsResp = response.parameters.fields["number"] # Valeur en btc
        usrBtc_ = float(json.loads(MessageToJson(usrQtsResp)))
        usrTotPrice = btcKaderPrice * usrBtc_
        usrTotPriceCFA = usrTotPrice * 655.99 # Conversion euro -> cfa
        fulfillmentText = "Le prix pour "+str(usrBtc_) + " bitcoin est " +str(usrTotPriceCFA) +" CFA" \
                            + "\n\nComment souhaitez vous  payer? \n*Flooz* \n*Tmoney*" \
                              " "
        return fulfillmentText
    elif response.intent.display_name == '6.user.confimation':
        userResponse = ""
        if (userResponse == "oui" or "yes"):
            return "Veuillez envoyer le montant indiquer au *+22891888464* par *Tmoney* ou " \
                   "au *+22898231871* par *Flooz*"
        elif(userResponse == "non" or "no"):
            return ""
        else:
            return "Vous devez envoyer soit: \n- *Oui* pour Confirmer la transaction " \
                   "\n- *Non* pour Annulez "
    elif response.intent.display_name == '':
        return "N/A"
    else:
        return response.fulfillment_text

#response.fulfillment_text