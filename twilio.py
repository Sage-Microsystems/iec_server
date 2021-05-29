import requests
from requests.auth import HTTPBasicAuth

TWILIO_ACCOUNT_ID = "AC9f1eccfcb217c5e30728bd362b5ab7d3"
TWILIO_ACCOUNT_TOKEN = "cb3a03fe9997233c4f812b9c7d9de90c"
TWILIO_SERVICE_ID = "VAb016387b77f8f8898ab5cf2bd07b1d86"

AUTH_HEADER = HTTPBasicAuth(TWILIO_ACCOUNT_ID, TWILIO_ACCOUNT_TOKEN)

def send_code(to,locale="en-GB"):
    url = f"https://verify.twilio.com/v2/Services/{TWILIO_SERVICE_ID}/Verifications"
    payload = {
        "To": to,
        "Channel": "sms",
        "Locale": locale
    }

    response = requests.post(url, data=payload, auth=AUTH_HEADER)
    return response

def verify_code(to, code):
    url = f"https://verify.twilio.com/v2/Services/{TWILIO_SERVICE_ID}/VerificationCheck"
    payload = {
        "To": to,
        "Code": code
    }

    response = requests.post(url, data=payload, auth=AUTH_HEADER)
    return response