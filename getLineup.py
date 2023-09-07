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
         
        #grab all html in Main   
        results = soup.find(id="main")

        
        job_elements = results.find_all("p")
        artists = []
        for i in range(0,len(job_elements)):
            print(job_elements[i].text)
            artists.append(job_elements[i].text.split('•' or '\n'))
    
    else:
        print("reponse code error:"+page.status_code)


def main():
    getList()


if __name__ == "__main__":
    main()