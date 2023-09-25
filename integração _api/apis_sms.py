from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'token'
auth_token = 'token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testando",
                     from_='+12564140811',
                     to='+5521995930261'
                 )

print(message.sid)