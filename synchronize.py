from os import listdir
import mutagen.flac as mtg_f
import mutagen.mp4 as mtg_mp4


def synchronize_downloads(tidal_list, dir_path):
    get_all_isrc_from_directory(dir_path)
    for track in tidal_list:
        pass


def get_all_isrc_from_directory(dir_path):
    isrc_list = []
    not_isrc_list = []
    for file_name in listdir(dir_path):
        if file_name.endswith(".flac"):
            audio_file = mtg_f.FLAC(dir_path + "/" + file_name)
            saved_tags = audio_file.tags.keys()
            if 'isrc' in saved_tags:
                isrc_list.append(audio_file.tags['isrc'])
            else:
                track_info = {}
                if 'title' in saved_tags:
                    track_info['title'] = audio_file.tags['title']
                if 'artist' in saved_tags:
                    track_info['artist'] = audio_file.tags['artist']
                if 'album' in saved_tags:
                    track_info['album'] = audio_file.tags['album']
                track_info['duration'] = int(audio_file.info.length)
                not_isrc_list.append(track_info)
        elif file_name.endswith(".mp4"):
            audio_file = mtg_mp4.MP4(dir_path + "/" + file_name)
            saved_tags = audio_file.keys()
            if "----:LATUL:ISRC" in saved_tags:
                isrc_list.append(audio_file["----:LATUL:ISRC"][0].decode("UTF-8"))
            else:
                track_info = {}
                if '\xa9nam' in saved_tags:
                    track_info["title"] = audio_file['\xa9nam'][0]
                if '\xa9ART' in saved_tags:
                    track_info["artist"] = audio_file['\xa9ART'][0]
                if '\xa9alb' in saved_tags:
                    track_info["album"] = audio_file['\xa9alb'][0]
                track_info['duration'] = int(audio_file.info.length)
                not_isrc_list.append(track_info)
