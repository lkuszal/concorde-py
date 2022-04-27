from datetime import datetime
from os import makedirs


def start(path):
    global log_file
    makedirs(path, exist_ok=True)
    log_file = open(path + timestamp(), "a", encoding="utf-8")
    write_log('info', 'started')
    
    
def end():
    write_log('info', 'completed')


def write_log(status, message):
    message = f'{status.upper()}: {message} {timestamp()}\n'
    log_file.write(message)


def timestamp():
    return datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
