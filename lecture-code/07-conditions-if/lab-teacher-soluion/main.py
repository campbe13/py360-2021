# two functions with conditions
# pmcampbell
# 2022-02-14
import random

def magic_8_ball():
  shake = random.randint(1,8)
  if shake == 1:
    return "● It is certain."
  if shake == 2:
    return "● It is decidedly so."
  if shake == 3:
    return "● Outlook not so good."
  if shake == 4:
    return "● Very doubtful."
  if shake == 5:
    return "Reply hazy, try again."
  if shake == 6:
    return "● Ask again later."
  if shake == 7:
    return "● Better not tell you now."
  if shake == 8:
    return "Signs point to yes. "

def alt1_magic_8_ball():
  shake = random.randint(1,8)
  if shake == 1:
    return "● It is certain."
  elif shake == 2:
    return "● It is decidedly so."
  elif shake == 3:
    return "● Outlook not so good."
  elif shake == 4:
    return "● Very doubtful."
  elif shake == 5:
    return "Reply hazy, try again."
  elif shake == 6:
    return "● Ask again later."
  elif shake == 7:
    return "● Better not tell you now."
  else:
    return "Signs point to yes. "

def alt2_magic_8_ball():
  shake = random.randint(1,8)
  if shake == 1:
    msg =  "● It is certain."
  elif shake == 2:
    msg =  "● It is decidedly so."
  elif shake == 3:
    msg =  "● Outlook not so good."
  elif shake == 4:
    msg =  "● Very doubtful."
  elif shake == 5:
    msg =  "Reply hazy, try again."
  elif shake == 6:
    return "● Ask again later."
  elif shake == 7:
    msg =  "● Better not tell you now."
  else:
    msg =  "Signs point to yes. "
  return msg

def can_drive(age): 
  if age < 16:
    return "you are too young to drive"
  elif age <= 21:
    return "You’re old enough to drive, but not old enough to rent a car"
  else: 
    return "You’re old enough to both drive and to rent a car!"

def main():
  name = input("What is your name: ")
  msg = magic_8_ball()
  print(f"for you {name} magic 8 ball says {msg}")
  print(f"for you {name} alt1 magic 8 ball says {alt1_magic_8_ball()}")
  print(f"for you {name} alt2 magic 8 ball says {alt2_magic_8_ball()}")
  age = int(input("How old are you? "))
  print(f" {age} {can_drive(age)}")

if __name__ == "__main__":
    main()
