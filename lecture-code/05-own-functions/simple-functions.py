# writing your  own functions
# from exercises 05-01 
# teacher demo
# pmcampbell
# 2022-02-07

# hello()   :(
# code for your own hello function
def hello():
  print("Hello World")
  print("that was hello world")
# call your own hello function
hello() 
hello()
hello()
# code for your own hello function with a name parameter
def hello_name(name):
  print(f"Hello {name}")

hello_name("Fozzie") 
name = "Miss Piggy"
hello_name(name) 
# call your function 3x with these variables as the argument
muppet_name = "Kermit"
hello_name("muppet_name")
user_name = "Simon" 
hello_name(user_name)
name = 'Kate Mckinnon'
hello_name(name)
# call your own hello function

# write code to ask for a name, use the name in your function
name = input("What is your name:")
hello_name(name)
hello_name("muppet "+name)


# write a function with a number parameter & use it to multiply a string of your choice
# you might want to use a unicode character remember \print  where xxxx is the unicode value for the char
def string_multiplier(mult):
  print(mult*"Muppets! ")

string_multiplier(5)
string_multiplier(3)
string_multiplier(0)
# run your function
def mu_mult(mult):
  print(mult*"\u00b5")

mu_mult(100)
# code  smallest of two function
def small(num1, num2):
  if num1 < num2:
    min = num1
  else:
    min = num2
  return min

print(f' 1, 5 minimum {small(1,5)}')  # 1
print(f' 5, 1 minimum {small(5,1)}')  # 1
print(f' 12, 5 minimum {small(12,5)}')  # 5
