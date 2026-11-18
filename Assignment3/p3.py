class MediaItem:
  def __init__(self, title, minutes):
    self.title = title
    self.minutes = minutes
  
  def play(self):
    return f"Playing {[self.title]} ({self.minutes} mins)"
class PodcastEpisode(MediaItem):
  def __init__(self, title, minutes, host):
    super().__init__(title, minutes)
    self.host = host
  def play(self):
    return super().play() + f"Hosted by [{self.host}]"
  
test = PodcastEpisode("Tech Talk", 45, "Alex")
print(test.play())