import tidal
import urllib.request
from os import remove
from time import sleep
session = tidal.login_to_tidal(handle_login_link=tidal.login_wrapper)
a = session.user.favorites.tracks()[0]
switch_1 = switch_2 = False
'''
for x in range(100):
    if switch_1:
        switch_2 = True
    
    try:
        print(session.user.favorites.tracks())
    except Exception as e:
        print('favorites.tracks')
        print(e)
        switch_1 = True

    try:
        print(a.name)
    except Exception as e:
        print('track.name')
        print(e)
        switch_1 = True
        
    try:
        print(a.get_url())
    except Exception as e:
        print('track.get_url()')
        print(e)
        switch_1 = True
        
    try:
        print(urllib.request.urlretrieve(a.get_url(), 'C:/Users/Latul/Desktop/music/asd.mp4'))
        remove('C:/Users/Latul/Desktop/music/asd.mp4')
    except Exception as e:
        print('download album image')
        print(e)
        switch_1 = True

    try:
        print(a.artists)
    except Exception as e:
        print('track.artists')
        print(e)
        switch_1 = True
        
    try:
        print(a.track_num)
    except Exception as e:
        print('track.track_num')
        print(e)
        switch_1 = True
        
    try:
        print(a.album)
    except Exception as e:
        print('track.album')
        print(e)
        switch_1 = True
        
    try:
        print(a.album.name)
    except Exception as e:
        print('track.album.name')
        print(e)
        switch_1 = True
        
    try:
        print(a.album.tracks)
    except Exception as e:
        print('track.album.tracks')
        print(e)
        switch_1 = True
        
    try:
        print(a.album.image(80))
    except Exception as e:
        print('track.album.image')
        print(e)
        switch_1 = True

    try:
        print(urllib.request.urlretrieve(a.album.image(80), 'C:/Users/Latul/Desktop/music/asd.jpg'))
        remove('C:/Users/Latul/Desktop/music/asd.jpg')
    except Exception as e:
        print('download album image')
        print(e)
        switch_1 = True

    if switch_1 and switch_2:
        break
'''

while True:
    for track in session.user.favorites.tracks():
        print(urllib.request.urlretrieve(track.album.image(80), 'C:/Users/Latul/Desktop/music/asd.jpg'))
        remove('C:/Users/Latul/Desktop/music/asd.jpg')
