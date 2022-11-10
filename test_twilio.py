import keys2
from twilio.rest import Client


client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+12284528841"
myCellphone = "+17088971571"

textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body="Hey there!")

print(textmsg.status)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",to=myCellphone,from_=TwilioNumber)