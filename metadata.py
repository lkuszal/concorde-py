from os import remove as remove_file
from os.path import isfile

from scripts import change_extension, download_asset, tidal_connection_wrapper
from metadata_mp4 import add_mp4_metadata
from metadata_flac import add_flac_metadata
from logger import write_log


def add_audio_metadata(track, track_extension, track_path, session):
    metadata = get_audio_metadata(track, track_path, session)
    if track_extension in ('.m4a', '.mp4'):
        add_mp4_metadata(track_path, metadata)
    elif track_extension == '.flac':
        add_flac_metadata(track_path, metadata)
    else:
        write_log('error', f'Not recognized extension {track_extension} for {track.name}')
    delete_audio_image(track_path)


def download_audio_image(track, track_path, session):
    image_url = tidal_connection_wrapper(session, track.album.image, 640)
    if image_url:
        image_path = change_extension(track_path, 'jpg')
        download_asset(image_url, image_path, session)
        return image_path
    else:
        write_log('error', f'downloading image for {track.name} failed')
        return False


def delete_audio_image(track_path):
    image_jpg = change_extension(track_path, 'jpg')
    image_png = change_extension(track_path, 'png')
    if isfile(image_jpg):
        remove_file(image_jpg)
    if isfile(image_png):
        remove_file(image_png)


def get_isrc(track):
    isrc = track.isrc
    if isrc and len(isrc) > 0:
        return isrc
    else:
        return False


def get_audio_metadata(track, track_path, session):
    metadata = {
        "title": track.name,
        "track_number": str(track.track_num),
        "artists": [x.name for x in track.artists],
        "album": track.album.name
    }
    total_tracks = tidal_connection_wrapper(session, track.album.tracks)
    if total_tracks:
        metadata['total_tracks'] = str(len(total_tracks))
    image = download_audio_image(track, track_path, session)
    if image:
        metadata["image"] = image
    isrc = get_isrc(track)
    if isrc:
        metadata["isrc"] = isrc
    return metadata
