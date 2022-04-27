import tidalapi
from requests import HTTPError

session = tidalapi.Session()
session.login_oauth_simple()

mother = session.user
mother_favorite_list = mother.favorites.tracks()
input()
new_session = tidalapi.Session()
new_session.login_oauth_simple()

child = new_session.user
child_favorites = child.favorites
print(len(mother_favorite_list))
print(len(child_favorites.tracks()))
for old_track in mother_favorite_list:
    try:
        print(child_favorites.add_track(old_track.id))
    except HTTPError:
        print(old_track.id, old_track.name)
print('completed')
