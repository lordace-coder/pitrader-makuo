import os
import requests

# MAIL_API = 'https://api.brevo.com/v3/emailCampaigns'


def send_mail(mail_info, mail_subj, std_name):

    # Brevo API endpoint for sending transactional emails..
    url = "https://coco-api.onrender.com/api/send-mail/931038"

    payload = {
        "recipient_list": [os.getenv("email", "lordyacey@gmail.com")],
        "subject": f"{mail_subj}",
        "content": f"{mail_info}",
        "is_html": True,
        "context": {},
    }

    # Our post request..
    response = requests.post(url, json=payload)
    print(response.json())
    return
