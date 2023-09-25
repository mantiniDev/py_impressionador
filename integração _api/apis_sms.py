from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC97043c4b8ce06f6658f193e6a6015e2e'
auth_token = '12e606d0e5192e8af20f729889ff0485'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testando",
                     from_='+12564140811',
                     to='+5521995930261'
                 )

print(message.sid)