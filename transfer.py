from distutils.util import strtobool

class TidalResourcesTransfer:
    @classmethod
    def __init__(cls, donor_account, acceptor_account):
        donor = donor_account
        acceptor = acceptor_account
        cls.move_favourite_tracks(cls, donor.Favourites.tracks())

        cls.created_playlists = cls.donor.playlists()
        cls.favourite_videos = cls.donor.Favourites.videos()
        cls.favourite_playlists = cls.donor.Favourites.playlists()


    def move_favourite_tracks(self, favourite_tracks, acceptor):
        print("Move favourite tracks?, e.g.:")
        for track in favourite_tracks[3]:
            print(track.name)
        if strtobool(input("Y/N")):
            for track in favourite_tracks:
                acceptor.Favourites.add_track(track.id)

        else:
