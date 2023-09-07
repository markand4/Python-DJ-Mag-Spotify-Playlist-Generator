import requests
from bs4 import BeautifulSoup

def getList():
    #Set URL will change to user input later
    url = 'https://goldrushfestaz.com/lineup/'

    #Get page from request package
    page = requests.get(url)

    #Check http status then continue
    if page.status_code == 200:
        print("Lineup :-\n")
      
        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(page.content,'html.parser')   
         
        
        results = soup.find(id="main")
        print(results.prettify())
  
        # l is the list which contains all the text i.e news 
        l=soup.find("ul",{"class":"searchNews"})
      
        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
        for i in l.findAll("a"):
            print(i.text)
    else:
        print("reponse code error:"+page.status_code)


def main():
    getList()


if __name__ == "__main__":
    main()