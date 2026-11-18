class Character:
  def __init__(self, name, health = 100):
    self.name = name
    self.heath = health
  def take_damage(self, amount):
    self.heath -= amount
    print(f"[{self.name}], took [{amount}] damage.")

class ArmoredKnight(Character):
  
  def __init__(self, name, armor, health=100):
    super().__init__(name, health)
    self.armor = armor
  
  def take_damage(self,amount):
    print(f"Amour blocks [{self.armor}] damage")
    reduce_damage = max(0,amount-self.armor)
    super().take_damage(reduce_damage)

knight = ArmoredKnight("Author", 15) 

knight.take_damage(40)
print(knight.heath)