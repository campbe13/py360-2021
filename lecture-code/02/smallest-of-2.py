# determine smallest of 2 numbers
# 2022-01-24
# pcampbell

# test data (test all branches)
# 5,6   result 5
# 6,5   result 5
# 55,55 result 55

num1 = input("number please: ")
num2 = input("number please: ")

if num1 < num2:
    min = num1
else:
    min = num2

print(f'{min} is smallest, given {num1} and {num2}')