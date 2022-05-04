'''
Teacher's solutions 
https://replit.com/team/2022-360-s2/Test-2-practice-questions
'''
from classes import Tree

def trees():
  '''name Red Maple, height 15m, diameter 50cm , age 30 years, family Acer
  from __ init__ name, height, diameter, age, family):'''
  tree1 = Tree("Red Maple", 15, 50, 30, "Acer")
  '''name Sugar Maple, height 10m, diameter 25cm , age 15 years, family Acer
Black Ash height 30m, diameter 55cm, age 50 years, family Fraxinus'''
  tree2 = Tree("Sugar Maple", 10, 25, 15, "Acer")
  tree3 = Tree("Black Ash", 30, 55, 50, "Fraxinus")
  print(tree3)
  print(tree3.name)
  "Using your Red Maple instance determine if it is the same family as the Sugar Maple, display a message showing (same family or not) with the names of the trees & their family; do the same with Sugar Maple vs Black Ash (hint: you will have to use the family attribute of your other instance as a parameter for the check_fam() method )"
  if tree1.check_fam(tree2.family):
    print("Same family ", tree1.name, tree1.family, tree2.name, tree2.family)
  else:
    print("Not Same family ", tree1.name, tree1.family, tree2.name, tree2.family)
  if tree1.check_fam_obj_param(tree3):
    print("Same family ", tree1.name, tree1.family, tree3.name, tree3.family)
  else:
    print("Not Same family ", tree1.name, tree1.family, tree3.name, tree3.family)
    
  """Display the cost of replacing the black   ash and the name of the tree.
  """
  print(tree3.name, "costs $", tree3.cost(), "to replace" )  
def approx_e(tolerance):
  approx = 1 
  k = 1.0
  for i in range(2,1000):
    print("k",k, "i",i, "approx", approx)
    if abs(approx - (approx + 1/k)) < tolerance:
      return approx
    approx += 1/k 
    k = i*k # k *= i
  return approx 
  '''Write a function dicts() that takes a parameter a dictionary that contains entries with duplicate values. Have it create and return a new dictionary with the duplicate values removed.
For example'''
def dicts(dict1):
  newdict = {} 
  for key,value in dict1.items():
     if value in newdict.values():
       continue
     else:
       newdict[key] = value
  return newdict
# using not
def dicts_not(dict1):
  newdict = {} 
  for key,value in dict1.items():
     if value not in newdict.values():
         newdict[key] = value
  return newdict
'''Write a function list_to_ dict(list1, list2) that takes parameters 2 lists of the same size. Use the first parameter as the keys and the 2nd as the values to create a new dictionary.
For example
'''
def list_to_dict(list1,list2):
  newdict = {} 
  for i in range(len(list1)):
    print("list1[i]",list1[i],"list2[i]",list2[i])
    newdict[list1[i]] = list2[i]
  return newdict
  '''Write a function arrays() that takes a 2d numpy array of numbers as a parameter

Create a new array of the same size (rows & columns)
Loop through each element of the array parameter, if the element is >=0 assign it to the new array (same row & column) if it is not assign 0 to that element in the new array.
def pandas():
  df =pd.read_csv('inspection.csv')
  print(df.head())
  print(df.columns)
  max_fine = df.montant.max()
  print(df.montant.max())
  ix = df.montant.idxmax()  # index of the max
  bad_resto = df.iloc[ix]  # row
  print(type(bad_resto))
  print(f'the biggest fine of ${max_fine} goes to ')
  print(f'{bad_resto.etablissement} at {bad_resto.adresse}')
  name = df.etablissement.value_counts().idxmax()  # addr of the max
  addr=df.loc[df.etablissement == name].adresse.iloc[0]
  print()
  max_count =df.etablissement.value_counts().max()
  print(f'the most fines handed out: {max_count}  ')
  print(f'{name} at {addr}')
  name = df.etablissement.value_counts().idxmin()  # index of the max is name/etablissement
  print("name", name)
  addr=df.loc[df.etablissement == name].adresse.iloc[0]
  
  min_count =df.etablissement.value_counts().min()
  print(f'the least fines handed out: {min_count}  ')
  print(f'{name} at {addr} ' )
  # using item() instead of iloc[]
  addr=df.loc[df.etablissement == name].adresse.item()
  print("addr via loc & .item() ",addr)
  #print(df.etablissement.value_counts())  # index 
  return At the end of the function, return the new array'''
import numpy as np
def arrays(array1):
  newarray = np.zeros(array1.shape)
  i = 0
  for row in array1:
    j = 0 
    for col in row:
      print("i",i,"j",j)
      if col >= 0:
          newarray[i,j] = array1[i,j]
      j += 1
    i += 1
  return newarray
def arrays_ix(array1):
  newarray = np.zeros(array1.shape)
  rows, cols = array1.shape
  for  i in range(rows):
    for j in range(cols):
      print("i",i,"j",j)
      if array1[i,j] >= 0:
          newarray[i,j] = array1[i,j]
  return newarray
def pandas():
  df =pd.read_csv('inspection.csv')
  print(df.head())
  print(df.columns)
  max_fine = df.montant.max()
  print(df.montant.max())
  ix = df  pandas() .montant.idxmax()  # index of the max
  bad_resto = df.iloc[ix]  # row
  print(type(bad_resto))
  print(f'the biggest fine of ${max_fine} goes to ')
  print(f'{bad_resto.etablissement} at {bad_resto.adresse}')
  name = df.etablissement.value_counts().idxmax()  # addr of the max
  addr=df.loc[df.etablissement == name].adresse.iloc[0]
  print()
  max_count =df.etablissement.value_counts().max()
  print(f'the most fines handed out: {max_count}  ')
  print(f'{name} at {addr}')
  name = df.etablissement.value_counts().idxmin()  # index of the max is name/etablissement
  print("name", name)
  addr=df.loc[df.etablissement == name].adresse.iloc[0]
  
  min_count =df.etablissement.value_counts().min()
  print(f'the least fines handed out: {min_count}  ')
  print(f'{name} at {addr} ' )
  # using item() instead of iloc[]
  addr=df.loc[df.etablissement == name].adresse.item()
  print("addr via loc & .item() ",addr)
  #print(df.etablissement.value_counts())  # index 
  return       
def main():
  print("blah")
  #trees()
  '''import math
  print("math_e",math.e)
  print("approx_e(0.5)",approx_e(0.5))
  print("approx_e(0.05)",approx_e(0.05))'''
  '''  fruit = { "apples": 10, "oranges": 15, "grapes": 45, "plums":10}
  print(dicts(fruit))
  print(dicts_not(fruit))
  # dict = { "apples": 10, "oranges": 15, "grapes": 45 }
  list1 = ["kiwi","apples", "oranges", "grapes"]
  list2 = [12, 10, 15, 45]
  print(list_to_dict(list1,list2))'''
  #results in dict = { "apples": 10, "oranges": 15, "grapes": 45 }
  print("blah")
  '''array = np.array([[1, -2, 3], [-5,9,-6]])
  print(array)
  print(arrays(array))
  array = np.array([[-, -2, 3], [-5,-2,6]])
  print(array)
  print(arrays_ix(array))'''
  pandas() 
if __name__ == '__main__':
  print("before main")
  main()
