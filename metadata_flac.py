import mutagen.flac as mtg_f
from mutagen.id3 import PictureType
from PIL import Image

from scripts import change_extension


def add_flac_metadata(track_path, track_metadata):
    audio_file = mtg_f.FLAC(track_path)
    audio_file['TITLE'] = track_metadata['title']
    audio_file['ALBUM'] = track_metadata['album']
    audio_file['TRACKNUMBER'] = track_metadata['track_number']
    audio_file['ARTIST'] = track_metadata['artists']
    if "image" in track_metadata.keys():
        cover_image = generate_flac_image(track_metadata["image"], PictureType.COVER_FRONT)
        thumbnail_path = create_thumbnail_image(track_metadata["image"])
        thumbnail_image = generate_flac_image(thumbnail_path, PictureType.FILE_ICON)
        audio_file.add_picture(cover_image)
        audio_file.add_picture(thumbnail_image)
    if 'isrc' in track_metadata.keys():
        audio_file['ISRC'] = track_metadata['isrc']
    audio_file.save()
    
    
def create_thumbnail_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((32, 32), resample=Image.LANCZOS)
    new_image_path = change_extension(image_path, 'png')
    image.save(new_image_path, "PNG")
    return new_image_path


def generate_flac_image(image_path, id3_type):
    src_image = Image.open(image_path)
    flac_image = mtg_f.Picture()
    flac_image.data = open(image_path, "rb").read()
    flac_image.width = src_image.width
    flac_image.height = src_image.height
    flac_image.mime = u"image/" + image_path.split('.')[-1]
    flac_image.type = id3_type
    return flac_image
