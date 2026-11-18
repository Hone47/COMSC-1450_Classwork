
'''
#p1
x ="hello"
# print(dir(x))
def validate_acess_code(raw_code):
  parsed_code = raw_code.strip()
  parsed_code = parsed_code.lower()
  
  if parsed_code.startswith("admin") and parsed_code.endswith("2026"):
    return True
  else:
    return False
#p2
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
  

#p3
def verify_file_record(line_content):
  line_content.strip()
  if line_content.startswith("#"):
    return 0
  if line_content.startswith("id"):
    return 1
  else:
    return -1

#p4
with open("numbers.txt", "r") as file:
    numbers = file.readlines()

total = 0
count = 0

for num in numbers:
    total += float(num)
    count += 1

average = total / count

print("Average:", average)

#p5
with open("numbers.txt", "r") as file:
    numbers = file.readlines()

total = 0

for num in numbers:
    if int(num) % 2 == 0:
        total += int(num)

print("Sum of even numbers:", total)

#q6
evenNums = []
with open("odd_numbers.txt", "w") as file:
    for num in numbers:
        if int(num) % 2 != 0:
            file.write(num + "\n")  
    
#q7
def filter_log_records():
    with open("raw_log.txt", "r") as infile:
        with open("cleaned_log.txt", "w") as outfile:

            for line in infile:
                cleaned_line = line.strip()

                if cleaned_line:
                    cleaned_line = cleaned_line.upper()
                    outfile.write(cleaned_line + "\n")


filter_log_records()