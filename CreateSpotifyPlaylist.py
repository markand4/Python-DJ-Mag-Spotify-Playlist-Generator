import requests
from requests import post, get
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os, json
import base64
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


def getArtistList(year):
    #Set URL will change to user input later
    url = 'https://djmag.com/top100djs/'+year

    #Get page from request package
    page = requests.get(url)

    #Check http status then continue
    if page.status_code == 200:
      
        #parser for html
        soup=BeautifulSoup(page.content,'html.parser')   
         
        #grab all top 100dj divs from site    
        results = soup.findAll(name='div',class_='top100dj-name')

        #creates artist list from list of top 100 dj div elements
        #Dev note add async or parllel later?
        artists = []
        for result in results:
            artists.append((result.find('a').text).replace('\n',''))

        return(artists)
    else:
        print("reponse code error:"+page.status_code)


def getSpotifyToken():
    #Grabs Client id and secret from .env
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return(spotify)


def search_for_artists(spotify, artists):
    #goes through artist array and calls API to get artist ID  
    artistResults = []
    for artist in artists:
        result = spotify.search(q='artist:' + artist, type='artist')
        if(len(result['artists']['items'])>0):
            artistResults.append(result['artists']['items'][0]['id'])
        else:
            print("Can't find artist "+artist)
                 
    return(artistResults)
    


def grabTopSongs(spotify, artists_results):
    songList = []
    for artist_result in artists_results:
        results = spotify.artist_top_tracks(artist_result)
        songList.append(results['tracks'][:10])

    return(songList)

def createPlaylist(song_list):
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    token = util.prompt_for_user_token(
        scope="playlist-modify-public",
        redirect_uri='http://localhost:8888/callback',
        client_id=client_id,
        client_secret=client_secret
    )
    spotify = spotipy.Spotify(auth=token)

    currentUserID = (spotify.current_user())['id']

    #Creates list of song URI per artist combining them all into one makes it too big for add songs to playlist API call later 
    song_uri_list = []
    for songs in song_list:
        artist_songs_uri = []
        for song in songs:
            artist_songs_uri.append(song['uri'])
        song_uri_list.append(artist_songs_uri)

    playlist = spotify.user_playlist_create(user=f'{currentUserID}',name='2019 DJ Mag Top 100',description='playlist of top 100 dj based on year from DJ mag')
    
    
    for songs_uri in song_uri_list:
        spotify.user_playlist_add_tracks(user=f'{currentUserID}',playlist_id=playlist['id'],tracks=songs_uri)
    

def main():
    artists = getArtistList('2019')
    token = getSpotifyToken()
    artists_results = search_for_artists(token, artists)
    song_list = grabTopSongs(token, artists_results)
    createPlaylist(song_list)
    

if __name__ == "__main__":
    main()