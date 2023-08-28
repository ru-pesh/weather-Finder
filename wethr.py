import requests
# Requests moduele will help fetching data from the url.
from bs4 import BeautifulSoup
# The bs4 moduele and beautifulsoup is imported for filtering data from
def weth(city):
    HEADERS =om {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    # header variable is taken to avoid compulsion of API from website  
    url="https://www.google.com/search?q=weather+"+ city
    response = requests.get(url,headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        tem=soup.find(id = "wob_tm")
        temp=tem.getText()
        sped=soup.find(id="wob_ws")
        speed=sped.getText()
        prec=soup.find(id="wob_pp")
        precipitation=prec.getText()
        x = soup.find(class_ = "BBwThe")
        name = x.getText()
        print('\n\t\t\t', name,'\n')
        print('The current temperature of',name,'is',temp,'degree celsius')
        print('The current wind speed of',name,'is',speed)
        print('The current precipitation percentage of',name,'is',precipitation,'\n')
    except :
        print('\nNo data found about the given city-',city,'\n')

print('\t\t\t\tWELCOME TO WEATHER FORCASTING PROGRAM')

while True:
    city=input("Enter name of the city\n ")
    weth(city)
    n=input('press y to find next or press any other button to finish ')
    if n=='y' or n == 'Y':
        continue
    else:
        break
# The above code iterates till someone wins.



