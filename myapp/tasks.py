# tasks.py

from twilio.rest import Client

def send_sms_alert(temperature):
    # Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=f"Warning: The refrigerator door has been open for too long. Current temperature: {temperature}°C",
        from_='+1234567890',  # Your Twilio number
        to='+12345555'  # The store manager's number
    )
    
    print(f"SMS sent: {message.sid}")
