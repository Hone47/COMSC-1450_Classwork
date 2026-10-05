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
    

 
  # raw_code = input("Enter access code")
  # is_valid = validate_acess_code(raw_code)
  # if is_valid:
  #   print("sucess")
  # else:
  #   print("access denied")
print(audit_text_stream("security"))
  
  
