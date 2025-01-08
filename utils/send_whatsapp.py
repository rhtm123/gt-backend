import os
from twilio.rest import Client
import json
from decouple import config

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


def send_msg(content_template_sid, variables):
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)
    variables_json = json.dumps(variables)  # Convert dictionary to JSON string

    message = client.messages.create(
    from_='whatsapp:+12564641710',  # Twilio's WhatsApp Sandbox number or your WhatsApp-enabled Twilio number
    to='whatsapp:+919518901902',  # Replace with the recipient's WhatsApp number
    content_sid=content_template_sid,
    content_variables=variables_json,
    )

    print(f"Message sent! SID: {message.sid}")
    return message.sid