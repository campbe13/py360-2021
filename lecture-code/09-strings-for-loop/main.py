# strings & for loops, in class exercises

def eight_chars(word):
  if len(word)>8:
    return "Too long"
  elif len(word)<8:
    return "Too short"
  else:
    return "Perfect, thank you for the word starting with " + word[0]
def bad_password(name, password):
  print("name", name)
  print("password", password)
  if name in password:
    return True 
  else:
    return False

def isbad_password(name, password):
   return (name in password) 

def count_e(sentence):
  count = 0 
  for letter in sentence:
    if letter == 'e' or letter == 'E':
      count += 1

  return count

def reverse_word(word):
  reversed = ''
  for letter in word:
    reversed = letter +reversed
  return reversed
def secondletters1(word):
  secondstring = ''
  ix = 0
  for letter in word:
    if ix%2 == 1:
      secondstring = secondstring+ letter
    ix += 1
  return secondstring


def main():
  sentence = input("enter a sentence: ")
  reverse = reverse_word(sentence)
  print(f"sentence {sentence} reversed {reverse}")
  
  secondstr = secondletters1(sentence)
  print(f"sentence {sentence} every 2nd letter {secondstr}")
  
  num = count_e(name)
  print(f"sentence has {num} e's")
  
  name = input("What is your name: ")
  password = input("What is your password: ")

  if ( isbad_password(name, password)):
    print("you need a better password")
  else:
    print ("password ok")

  name = input("What is your name: ")
  password = input("What is your password: ")
  
  result = isbad_password(name, password)
  if result:
    print("you need a better password")
  else:
    print ("password ok")
  input_word = input("enter an 8 letter word: ")
  print(eight_chars(input_word))

  result = eight_chars(input("enter an 8 letter word: "))
  print(result)

  input_word = input("enter an 8 letter word: ")
  result = eight_chars(input_word)
  print(result)
  
  print(eight_chars(input("enter an 8 letter word")))
 

#code the main function below  

# Code below ensures that the function called main is invoked when you run
if __name__ == "__main__":
    main()

