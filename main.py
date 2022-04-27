import download
import tidal
import logger


path_dir = 'C:/Users/Latul/Desktop/music/'
logger.start(path_dir)
current_session = tidal.start_session()
tidal.define_audio_quality(current_session, 'lossless')
download.download_favourites(current_session, dir_path=path_dir)
logger.end()
