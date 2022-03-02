'''
the code below is not thoroughly tested 
and there are other solutions
'''
def login():
  name = input("name svp ")
  password = input("password svp ")
  if password == 'P@55w0rD':
    print("Access granted ", name)
    return True
  else:
    print("access denied")
    return False

def cash_cheque(amount):
  if amount < 10:
    return 1.00
  elif amount < 100:
    return amount*.1
  elif amount < 1000:
    return amount*.05 + 5
  else:
    return amount*.1 +40
def multiple_logon1():
  for i in range(5):
    if login():
      return True
  return False
def multiple_logon2():
  count_true = 0
  count_false = 0
  for i in range(5):
    if login():
      count_true += 1
    else:
      count_false +=1
  if count_true > 0:
    return True
  else:
    return False
# for letter in string:   is only 1 char  at a time 
# if 'bank' in string: will only match the 1st bank
def find_bank(string):
  count = 0
  for i in range(len(string)-1):
    print ("string[i:i+4]",string[i:i+4])
    if string[i:i+4] == 'bank':
      count += 1
  return count

print("3, ", find_bank("bank in bank not bank"))
print("0, ", find_bank("xank in bxnk"))
print("1, ", find_bank("bank"))

def multiple_cheque():
  count = int(input("how many cheques "))
  sum_service = 0
  for i in range(count):
    amount = float(input(f'cheque {i} amount: '))
    service = cash_cheque(amount)
    print ("service", service)
    sum_service += service
  print (f"service charges {sum_service}")
  return sum_service  # were not asked to do this

multiple_cheque()
