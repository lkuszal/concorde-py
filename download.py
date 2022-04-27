
from os.path import isfile
from os import makedirs
from re import sub, compile

from metadata import add_audio_metadata
from logger import write_log
from scripts import tidal_connection_wrapper, download_asset


def clear_name_for_file(string, advanced=True):
    if advanced:
        return sub(compile(r'[(\[]feat.*[)\]]|[(\[].*[rR]emaster.*[)\]]|'
                           r'[(\[].*[cC]over.*[)\]]|[(\[].*[vV]ersion.*[)\]]|'
                           r'[(\[].*[fF]rom.*[)\]]|[(\[].*[lL]ive.*[)\]]'
                           r'[*]|[?]|[|]|[\\]|[/]|["]|[:]|[>]|[<]'), '', string)
    else:
        return sub(r'[*]|[?]|[|]|[\\]|[/]|["]|[:]|[>]|[<]', '', string)


def create_track_name(download_location, track_name, extension, increment=''):
    ready_track_path = download_location + track_name + increment + extension
    if isfile(ready_track_path):
        if increment:
            new_increment = '(' + str(int(increment[1:-1]) + 1) + ')'
        else:
            new_increment = '(1)'
        return create_track_name(download_location, track_name, extension, new_increment)
    return ready_track_path


def check_audio_extension(track_url):
    extension_in_url = track_url.split('?token=')[0].split('.')[-1]
    if extension_in_url == 'm4a':
        return '.mp4'
    else:
        return '.' + extension_in_url


def get_track_url(track, session):
    track_url = tidal_connection_wrapper(session, track.get_url)
    if track_url:
        return track_url
    else:
        write_log('error', f'retrieving track_url for {track.name} failed')
        return False


def download_favourites(session, dir_path='./TidalDownloads', offset=0, limit=None):
    makedirs(dir_path, exist_ok=True)
    for track in session.user.favorites.tracks(offset=offset, limit=limit):
        write_log('info', f'track no. {offset}')
        offset += 1
        download_track(track, session, dir_path)


def download_track(track, session, dir_path='./TidalDownloads'):
    track_url = get_track_url(track, session)
    if track_url:
        music_extension = check_audio_extension(track_url)
        track_path = create_track_name(dir_path, clear_name_for_file(track.name), music_extension)
        if download_asset(track_url, track_path, session):
            write_log('info', f'downloaded {track.name}')
            add_audio_metadata(track, music_extension, track_path, session)
        else:
            write_log('error', f'downloading of {track.name} failed')
