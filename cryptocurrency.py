from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.investing.com/crypto/currencies'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
#print(title.text)

table_rows = soup.findAll("tr")

name = ''
symbol = ''
current_price = 0.0
change = 0.0
corresponding_price = 0.0

for row in table_rows[1:6]:
    td = row.findAll('td')
    name = td[2].text
    symbol = td[3].text
    current_price = float(td[4].text.replace('$','').replace(',',''))
    change = float(td[8].text.replace('%','').replace(',',''))

    if change > 0:
        corresponding_price = round((current_price * (1-(change * .01))),2)
    if change < 0:
        corresponding_price = round((current_price * (1+(change * .01))),2)
    
    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Current Price: ${current_price:,.2f}")
    print(f"Percent Change in the Last 24 Hours: {str(change)}%")
    print(f"Corresponding Price: ${corresponding_price:,.2f}")
    print()
    input()


import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+12284528841"
myCellphone = "+17088971571"

counter = 1
for row in table_rows[1]:
    if current_price < 40000 and counter == 1:
        textmessage = client.messages.create(to=myCellphone,from_=TwilioNumber,body="Bitcoin's current price is below $40,000!")
        print(textmessage)
        counter += 1

counter = 1
for row in table_rows[2]:
    if current_price < 3000 and counter == 1:
        textmessage = client.messages.create(to=myCellphone,from_=TwilioNumber,body="Ethereum's current price is below $3,000!")
        print(textmessage)
        counter += 1