from twilio.rest import Client 
import os

account_sid = 'a'
auth_token = 'b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="hello welcome",
                    from_='+12058754043',
                    to='+91 8010271565'
                )

print(message.sid)
