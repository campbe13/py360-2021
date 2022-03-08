'''
examples from the slide deck
using range, strings, tuples, lists, dicts
'''
def review_range():
  for i in range(10):
   print('hi!')

  sum=0
  for i in range(2,5):
     sum = sum+i

  print("sum",sum)
  
  for i in range(5, 115, 10):
     print(i)

def review_strings():
  count = 0
  # goes through every letter!! 
  word  = "bonjour hola hello"
  for letter in word:
     count +=1
     print(f'{count} {letter}')
  
  # stops at first match
  if 'll' in word:
     print("yes!")
  else:
    print("no!")

  # every 2nd letter  (use index)
  for i in range(2, len(word), 2):
     print(word[i])

def inc(list,x):
  x = x + 1	
  for i in range(len(list)):
    list[i] += 1

def mutable_vs_immutable():
  nums = [2,6,7]
  y = 5
  print("before", "nums", nums, "y", y)
  inc(nums, y)
  print("after", "nums", nums, "y", y)

def values_vs_pointers():
  # numbers assigned as values
  c = 2	# value
  d = c    # value  
  d += 1
  c += 3
  print('c',c,'d',d)
  
  # lists are assigned as references/pointers
  a = [2,3,5]
  b = a   # pointer the same list
  b[0] =111
  print('a',a,'b',b) 
def review_tuples():
  tuplea = 1, 2, 3, 5, 10
  print(tuplea[0])
  print(tuplea[len(tuplea)-1])
  #tuplea[0] = 99  # nope immutable!!!
def review_lists():
  a = [2,3,5]
  listc = modify_list(a)
  print("a",a,"listc",listc)
  
def modify_list(list):
  b = list 
  b[0] = 100
  c = b+list
  return c

def dictionary():
  empty = {}
  # key : value pairs
  month = { "jan" : 1 , "feb" : 2 , "mar" : 3 , \
        "apr" : 4 , "may" : 5 , "jun" : 6 , "jul" : 7 , "aug" : 8 , \
        "sept" : 9 , "oct" : 10 , "nov" : 11 , "dec" : 12}
  
  print(month['jul'])
  #print(month[7])  # oops nope, only by key, not value
  #print(month[0])  # oops nope, no index!
  month["sep"] = 9 # add a new element
  if 'sept' in month:
    print("sep & sept deleting one")
    del month['sept']
  print(month)

  for val in month.values():
    print("month value", val)
  
  for key in month.keys():
    print("month key", key)

  for key,value in month.items():
    print("month  key", key, "month value", val)
  
# main runs the review functions
def main():
  review_range()

  review_strings()

  mutable_vs_immutable()

  values_vs_pointers()
  
  review_lists()
  
  review_tuples()

  dictionary()
if __name__ == "__main__":
  main()
