class Song:
    "Class to represent a song"

    def __init__(self, title, artist, duration=0) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    def __str__(self) -> str:
        return self.title

    name = property(get_title)


class Album:
    def __init__(self, name, year, artist=None) -> None:
        self.name = name
        self.year = year
        if not artist:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        song_found = find_object(field=song, object_list=self.tracks)
        if not song_found:
            song_found = Song(title=song, artist=self.artist)
            if not position:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)

    def __str__(self) -> str:
        return self.name


class Artist:
    def __init__(self, name) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, name, year, title):
        album_found = find_object(field=name, object_list=self.albums)
        if not album_found:
            print(name + " not found.")
            album_found = Album(name=name, year=year, artist=self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(song=title)

    def __str__(self) -> str:
        return self.name


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    # new_artist = None
    # new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist, album, year, song = tuple(line.strip("\n").split("\t"))
            year = int(year)
            print(artist, album, year, song)

            # Unoptimized Version
            # if not new_artist:
            #     new_artist = Artist(name=artist)
            #     artist_list.append(new_artist)
            # elif new_artist.name != artist:
            #     new_artist = find_object(field=artist, object_list=artist_list)
            #     if not new_artist:
            #         new_artist = Artist(name=artist)
            #         artist_list.append(new_artist)
            #     new_album = None

            # if not new_album:
            #     new_album = Album(name=album, year=year, artist=new_artist)
            #     new_artist.add_album(new_album)
            # elif new_album.name != album:
            #     new_album = find_object(field=album, object_list=new_artist.albums)
            #     if not new_album:
            #         new_album = Album(name=album, year=year, artist=new_artist)
            #         new_artist.add_album(new_album)

            # new_song = Song(title=song, artist=new_artist)
            # new_album.add_song(new_song)

            # OOPS version
            new_artist = find_object(field=artist, object_list=artist_list)
            if not new_artist:
                new_artist = Artist(name=artist)
                artist_list.append(new_artist)
            new_artist.add_song(album, year, song)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(
                        "{0.name} \t {1.name} \t {1.year} \t {2.title}".format(
                            new_artist, new_album, new_song
                        ),
                        file=checkfile,
                    )


if __name__ == "__main__":
    artists = load_data()
    print(f"There are {len(artists)} artists.")
    create_checkfile(artists)
