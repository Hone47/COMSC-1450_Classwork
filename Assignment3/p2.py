class GiftCard:
  def __init__(self, owner, balance = 0.0):
    self.__owner = owner
    self.__balance = balance
  
  def get_balance(self):
    return self.__balance
  
  def reload(self,amount):
    if amount > 0: 
      self.__balance += amount
  
  def spend(self, amount):
    if self.__balance - amount > 0:
      self.__balance -= amount
    else:
      print("Insufficient gift card balance!")
      

giftcard = GiftCard("Jordan")
giftcard.reload(50)
giftcard.spend(75)
giftcard.spend(20)
# giftcard.__balance