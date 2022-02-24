# the usual stuff here (all names if team work)
 
import random
def show_cegeps(cegeps):
  for cegep in cegeps:
    if "awson" in cegep:
      print(f"You can go to {cegep} the best")
    else:
      print(f"You can go to {cegep}")

def roll_10():
  rolls = []
  for i in range(10):
    num=random.randint(1,6)
    rolls.append(num)
  return rolls
  
def largest_num(list_of_nums):
  largest=0
  for num in list_of_nums:
    if num > largest:
      largest=num
  return largest

def smallest_num(list_of_nums):
  smallest=999999   # better: use math lib infinity 
  for num in list_of_nums:
    if num < smallest:
      smallest=num
  return smallest

def main():
  students = ['John', 'Jane', 'Jo']
  grades=[80, 65, 97, 44, 100, 44]
  cegeps  \
  = ['Dawson', 'Vanier', 'JAC', 'Gerald Godin', 'Champlain', 'dawson College', 'Rosemont']
  fruits = ['apple','banana','cherry','orange', 'kiwi', 'melon', 'orange', 'mango']
#code your functions/inline here
  print("fruits---------------------------------------")
  count = 0
  for fruit in fruits:
    if fruit == 'orange':
      count +=1  
  print("oranges",count)

  for fruit in fruits:
    if "err" in fruit:
      print(fruit)

  fruits[1] = 'skittles'
  del fruits[3]   # len -1 & shift left
  del fruits[5]
  fruits.append('banana')
  print(fruits)
  
  print("cegeps---------------------------------------")
  show_cegeps(cegeps)
  
  print("grades---------------------------------------")
  grade = largest_num(grades)
  print(f" of this list {grades} the largest is {grade}")
  
  print("dice---------------------------------------")
  rolls = roll_10()
  print (rolls)
  sum = 0
  for roll in rolls:
    sum += roll
  
  print("average", sum//len(rolls))
  
  largest = largest_num(rolls)
  '''
  largest = 0
  for roll in rolls:
    if roll > largest:
      largest = roll
  '''
  print("largest",largest)

  smallest = smallest_num(rolls)
  '''
  smallest =7
  
  for roll in rolls:
    if roll < smallest:
      smallest = roll
  '''
  print("smallest",smallest)
  
if __name__ == "__main__":
    main()

