from twilio.rest import Client


def send_notification(to, message):
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message, from_="+919729774955", to=to  # Your Twilio phone number
    )
