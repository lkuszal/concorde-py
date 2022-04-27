from urllib.request import urlretrieve

from tidal import refresh
from logger import write_log


def change_extension(path, new_extension):
    return '.'.join(path.split('.')[:-1]) + '.' + new_extension


def tidal_connection_wrapper(session, function, *args):
    try:
        return function(*args)
    except:
        if not session.check_login():
            refresh(session)
        try:
            return function(*args)
        except Exception as error:
            write_log('error', f'{function} failed with error {str(error)}')
            return False


def download_asset(url, path, session):
    return tidal_connection_wrapper(session, urlretrieve, url, path)
