# ceasar cypher with digits
# user enters 4 digit int
# and a shift
#
# show encrypted number

# pmcampbell
# 2022-01-31

# test data
# 1234 shift 5  result 6789
# 9875 shift 5  4320

number = int(input("enter 4 digits: "))
shift = int(input("enter a shift value: "))

print("floor division")
print(f'//1000 {number// 1000}')
print(f'//100 {number// 100}')
print(f'//10 {number// 10}')
print(f'//1 {number// 1}')
print("modulo")
print(f'%1000 {number% 1000}')
print(f'%100 {number% 100}')
print(f'%10 {number% 10}')

digit1 = number // 1000
digit4 = number % 10

digit2 = number % 1000 // 100
digit3 = number % 100 // 10

print (f'digits {digit1}{digit2}{digit3}{digit4}')

caesar1 = (digit1 + shift) %10
caesar2 = (digit2 + shift) %10
caesar3 = (digit3 + shift) %10
caesar4 = (digit4 + shift) %10

print (f'caesar digits {caesar1}{caesar2}{caesar3}{caesar4}')

encrypted = caesar1 * 1000 + caesar2 * 100 + caesar3 * 10 + caesar4

print(f'put it together, input {number}  encrypted {encrypted}')
# formatting needed for leading 0
print(f'put it together, input {number}  encrypted {encrypted:04d}')
