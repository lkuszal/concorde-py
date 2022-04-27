from webbrowser import open_new_tab
from os.path import isfile
from json import dump, load
import tidalapi

from logger import write_log


def login_wrapper(string):
    open_new_tab(f'https://{string.split()[1]}')
    

def login_to_tidal(handle_login_link=print):
    session = tidalapi.Session()
    session.login_oauth_simple(function=handle_login_link)
    define_audio_quality(session)
    return session


def dump_oauth_to_json(session, json_file):
    oauth_data = {
        'token_type': session.token_type,
        'session_id': session.session_id,
        'access_token': session.access_token,
        'refresh_token': session.refresh_token
    }
    dump(oauth_data, open(json_file, 'w'))


def load_oauth_from_file(json_file):
    session = tidalapi.Session()
    oauth_data = load(open(json_file, 'r'))
    session.load_oauth_session(
        session_id=oauth_data['session_id'],
        token_type=oauth_data['token_type'],
        access_token=oauth_data['access_token'],
        refresh_token=oauth_data['refresh_token']
    )
    return session


def start_session():
    json_file = './tidal_session_info.json'
    if isfile(json_file):
        session = load_oauth_from_file(json_file)
    else:
        session = login_to_tidal(handle_login_link=login_wrapper)
        dump_oauth_to_json(session, json_file)
    return session


def define_audio_quality(session, quality='lossless'):
    audio_qualities = {
        'low': tidalapi.Quality.low.value,
        'high': tidalapi.Quality.high.value,
        'lossless': tidalapi.Quality.lossless.value,
        'master': tidalapi.Quality.master.value
    }
    session.config.quality = audio_qualities[quality]


def refresh(session):
    refresh_token = session.refresh_token
    session.token_refresh(refresh_token)
    write_log('info', 'tidal token was refreshed')
