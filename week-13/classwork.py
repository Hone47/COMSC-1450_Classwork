#1
class flyer: 
  def fly(self):
    return "flying high"
class swimmer:
  def swim(self):
    return "Swimming fast!"
class duck(flyer, swimmer):
  def quack(self):
    return "Quack!"
  
duck1 = duck()
print(duck1.quack(), duck1.fly(), duck1.swim())

#2
class MusicPlayer:
  def __init__(self,playlist_name): 
    self.playlist_name = playlist_name
  def play_music(self):
    return self.playlist_name
class GPS:
  def __init__(self,destination):
    self.destination = destination
class SmartCar(MusicPlayer,GPS):
  def __init__(self,playlist_name,destination,car_model):
    MusicPlayer.__init__(self,playlist_name)
    GPS.__init__(self,destination)
    self.car_model = car_model
  def play_music():
    MusicPlayer.play_music()
tesla = SmartCar("rock","texas", "tesla")

#3
class Dog:
  def speak():
    print("woof")
class Cat:
  def speak():
    print("meow")
class CreateConfusedPet(Dog,Cat):
  def speak(self):
    Dog.speak(self)
    Cat.speak(self)
    print("what am i?")