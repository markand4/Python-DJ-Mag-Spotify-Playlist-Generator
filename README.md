# Python DJ Mag Spotify Playlist Generator 

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)

Python DJ Mag Spotify Playlist Generator 

Python script that allows user to login to their spotify and create a spotify playlist of DJ Mag's top 100 artists of a given year by user 

## Prerequisites

Before you begin, ensure you have met the following requirements:

In order to use the Spotify API, you need to create a Spotify Developer app you need to follow [these steps](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/) to
to get a client ID and a client secret. You will also need to define a redirect URI: http://localhost:8888/callback.

You can use either a virtual enviroment or install [Python](https://www.python.org/downloads/), I will show you how to install and run on basis you have Python and [Pip](https://pip.pypa.io/en/stable/installation/) installed. 

## Installing Python DJ Mag Spotifu Playlist Generator 

First, clone the repository and cd into it:

```bash
https://github.com/markand4/Python-DJ-Mag-Spotify-Playlist-Generator.git
cd Python-DJ-Mag-Spotify-Playlist-Generator
```
Install Dependancies
```bash
pip install -r requirements.txt
```
Create Following Env Variables from Guide in Prerequisites except use the below Redirect

```bash
export SPOTIPY_CLIENT_ID="<app_client_id>"
export SPOTIPY_CLIENT_SECRET="<app_client_id>"
export SPOTIPY_REDIRECT_URI= "http://localhost:8888/callback"
```



## Using Python DJ Mag Spotify Playlist Generator 


To use Python DJ Mag Spotify Playlist Generator, run this Command: 

```
python CreateSpotifyPlaylist.py (year between 2004 and 2022)
```


## Contact

If you want to contact me you can reach me at markkurpiel@gmail.com

