
'''
# Problem 1
x ="hello"
# print(dir(x))
def validate_acess_code(raw_code):
  parsed_code = raw_code.strip()
  parsed_code = parsed_code.lower()
  
  if parsed_code.startswith("admin") and parsed_code.endswith("2026"):
    return True
  else:
    return False

def audit_text_stream(flagged_word):
  occurrence_total = 0
  while True:
    sentence = input("Enter your sentence")
    if(sentence.lower() == "exit"):
     break
    else:
      occurrence_total += sentence.lower().count(flagged_word)
  return occurrence_total
    

 
'''
with open("/Users/danny/Classwork/COMSC-1450_Classwork/Week-7/data.txt", "r") as infile:
  with open("/Users/danny/Classwork/COMSC-1450_Classwork/Week-7/data2.txt", "w")as outfile:
    for i in infile:
      outfile.write(i.upper())
      
  x = [] 
  total = 0
  for i in range(5):
      n = int(input("enter a num"))
      total += n
      x.append(n)

  print(total)