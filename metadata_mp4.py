import mutagen.mp4 as mtg_mp4


def add_mp4_metadata(track_path, track_metadata):
    pass
    audio_file = mtg_mp4.MP4(track_path)
    audio_file.tags['\xa9nam'] = track_metadata['title']
    audio_file.tags['\xa9alb'] = track_metadata['album']
    audio_file.tags['\xa9ART'] = track_metadata['artists']
    if "image" in track_metadata.keys():
        cover_image = [mtg_mp4.MP4Cover(open(track_metadata['image'], "rb").read())]
        audio_file.tags['covr'] = cover_image
    if "total_tracks" in track_metadata.keys():
        audio_file.tags['trkn'] = [(int(track_metadata['track_number']), int(track_metadata['total_tracks']))]
    else:
        audio_file.tags['trkn'] = [(int(track_metadata['track_number']), 0)]
    if "isrc" in track_metadata.keys():
        audio_file.tags["----:LATUL:ISRC"] = mtg_mp4.MP4FreeForm(track_metadata['isrc'].encode("UTF-8"), mtg_mp4.AtomDataType.ISRC)
    audio_file.save()
