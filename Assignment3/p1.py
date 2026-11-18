class Playlist:
  def __init__(self, title):
    self.songs = []
    self.title = title
  
  def add_songs(self, song_name):
    self.songs.append(song_name)
  
  def remove_song(self, song_name):
    self.songs.remove(song_name)
  
  def get_summary(self):
    summary = ""
    summary = f"Title:{self.title}, Song Count: {len(self.songs)}, "
    for s in self.songs:
      summary += s + " "
    
    return summary
  
playlist = Playlist("Road Trip")
playlist.add_songs("song1")
playlist.add_songs("song2")
playlist.add_songs("song3")
print(playlist.get_summary())


      
    
    