
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font


#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

rank = 0
name = ''
release_date = ''
total_gross = 0.0
distributor = ''


for row in table_rows[1:6]:
    td = row.findAll('td')
    rank = int(td[0].text)
    name = td[1].text
    release_date = td[8].text
    total_gross = float(td[5].text.replace('$','').replace(',',''))
    distributor = td[9].text.replace('\n','')
    theaters = int(td[6].text.replace(',',''))
    revenue = total_gross/theaters

    print(f"Rank: {str(rank)}")
    print(f"Name: {name}")
    print(f"Release Date: {release_date}")
    print(f"Total Gross: ${total_gross:,.2f}")
    print(f"Distributor: {distributor}")
    print(f"Theaters: {theaters}")
    print(f"Average Revenue per Theater: ${revenue:,.2f}")
    print()


    '''
    OTHER WAY:
    for x in range(1,6)
        td = table_rows[x].findAll('td')
        print(td[0])
        input()
    '''