class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []

    def add_song(self,song):
        if len(self.store) >= self.capacity:
            self.store.pop(0)
        self.store.append(song)

    def get_recently_played_songs(self):
        return  self.store

store = RecentlyPlayedStore(3)

store.add_song('S1')
store.add_song('S2')
store.add_song('S3')


print(store.get_recently_played_songs())

store.add_song('S4')
print(store.get_recently_played_songs())

store.add_song('S2')
print(store.get_recently_played_songs())

store.add_song('S1')
print(store.get_recently_played_songs())
