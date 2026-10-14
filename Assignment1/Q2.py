def process_atm_transactions(balance):
  final_balance = balance
  successful_trans = 0
  while True:
    amount = int(input("Enter a transaction amount"))
    if(amount == 0):
        return(final_balance,successful_trans )
    
    elif(amount > 0):
      successful_trans += 1
      final_balance += amount
    #abs so negative values will not pass this check and let user pull out infinite money
    elif(amount < 0 and abs(amount) <= final_balance):
      successful_trans += 1
      final_balance += amount
    else:
      print("Insufficient funds.")


def main():
  balance = int(input("What is your starting balance?"))
  finalbalance, successful_trans = process_atm_transactions(balance)
  print(finalbalance, successful_trans)

main()
  
  