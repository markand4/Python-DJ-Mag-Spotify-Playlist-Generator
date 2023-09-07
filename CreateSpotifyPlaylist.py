import requests
from bs4 import BeautifulSoup

def getArtistList(year):
    #Set URL will change to user input later
    url = 'https://djmag.com/top100djs/'+year

    #Get page from request package
    page = requests.get(url)

    #Check http status then continue
    if page.status_code == 200:
        print("Lineup :-\n")
      
        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(page.content,'html.parser')   
         
        #grab all top 100dj divs from site    
        results = soup.findAll(name='div',class_='top100dj-name')

        #creates artust list from list of top 100 dj div elements
        #Dev note add async or parllel later 
        artists = []
        for result in results:
            artists.append((result.find('a').text).replace('\n',''))

        return(artists)
    else:
        print("reponse code error:"+page.status_code)


def main():
    getArtistList('2019')


if __name__ == "__main__":
    main()