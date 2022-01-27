# using different data types
# and order of operations
# 2022-01-25
# pmcampbell

num1 = 2* 20
print(num1) # int
num2 = 2*23.5
print(num2) # float
word1 = 5 * "hi" 
print(word1)  # string
word2 = "bye" +  "hi"
print(word2)  #string
#word3 = "bye" *  "hi"
#print(word3) # error
#word4 = 3.1415 *  "hi"
#print(word4) # error
word4 = True  *  "hi"
print(word4) # True > 1
word4 = False  *  "hi"
print(word4)  # False > 0

year = input("enter a year: ")  # year is a string
yearsago = 2022 - int(year)   # convert year to int then subtract
print(f' {year} was {yearsago} years ago') 
print(float(year))  # shows decimal point


num = str(1.5)
print(type(num))  # string
num = 1.5
print(type(num))  # float

# order of operations 

# the braces are not needed because the order of ops 
# means they are done in the correct order 
# 1. mult & division (left to right)  ok bc commutative
# 2. addition
c = float(input("Temp celsius to convert: "))
print(f"order of ops  c * 9 / 5 + 32 {(c * 9 / 5 + 32)}f")

print(f"order of ops  (c * 9 / 5) + 32 {(c * 9 / 5) + 32}f")

print(f"order of ops  (c * (9 / 5) + 32 {(c * (9 / 5)) + 32}f")
