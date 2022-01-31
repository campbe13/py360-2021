# string vs int
#  + is a concat operator when used with strings!
#  + is additon when used with numbers!
# 2022-01-24
# pcampbell

# strings
whathappens =  '1' + '2'
print(f' strings {whathappens}')

# numbers
whathappens =  1 + 2
print(f' numbers {whathappens}')

# mixed (string first)
# error
# whathappens =  '1' + 2
whathappens =  '1' + str(2)
print(f' mixed string first {whathappens}')

# mixed (string num first)
# error
# whathappens =  1 + '2'
whathappens =  1 + int(2)
print(f' mixed number first {whathappens}')
