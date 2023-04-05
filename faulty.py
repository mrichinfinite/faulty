'''Bot that sends a message to a Webex space when a new fault is detected in an ACI fabric.'''

import requests
import urllib3
from access import *
from acitoolkit.acitoolkit import *
from acitoolkit.aciFaults import Faults
from creds import *
from flask import Flask, request

urllib3.disable_warnings() # Disable warning message

app = Flask(__name__)

def main():
    '''Main execution'''
    session = Session(URL, USERNAME, PASSWORD)
    session.login()

    subscribe_to_faults(session)

@app.route("/", methods=["POST"])
def receive_webhook():
    '''Webhook'''
    data = request.json
    message = data.get("message")

    if message:
        post_message_to_webex(message)

    return "OK"

def subscribe_to_faults(session):
    '''Subscribe to faults'''
    Faults.subscribe_faults(session, only_new=True)

    while True:
        if Faults.has_faults(session):
            faults = Faults.get_faults(session)
            for fault in faults:
                message = "**New Fault** : \n\n𝙎𝙪𝙗𝙟𝙚𝙘𝙩: {}\n𝘿𝙚𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣: {}\n𝘿𝙉: {}\n𝙍𝙪𝙡𝙚: {}\n𝙎𝙚𝙫𝙚𝙧𝙞𝙩𝙮: {}\n𝙏𝙮𝙥𝙚: {}\n𝘿𝙤𝙢𝙖𝙞𝙣: {}\n𝘾𝙖𝙪𝙨𝙚: {}".format(fault.subject, fault.descr, fault.dn, fault.rule, fault.severity, fault.type, fault.domain, fault.cause)
            
                post_message_to_webex(message)
                
def post_message_to_webex(message):
    '''Post to Webex'''
    header = {"Authorization": ACCESS_TOKEN, "Content-Type": "application/json"}
    message_url = "https://webexapis.com/v1/messages"
    request_body = {"roomId": ROOM_ID, "text": message}
    response = requests.post(message_url, json=request_body, headers=header)

    if not response.ok:
        print("FAILED TO SEND {} TO Webex".format(message))

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000, debug=True)
