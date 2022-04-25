'''
using Dog License data with  pandas
instantinating and using objects from the BetterDog class
'''
from dogs import BetterDog
import pandas as pd

dogdf = pd.read_csv('dogs2017-wsize.csv')

breed_series = dogdf.Breed.value_counts() 
# go throught the series  & show breeds with only 1 
for breed, count in breed_series.items():
  if count <= 1:
    print(breed)
    
single_breed = []
for breed, count in breed_series.items():
  if count <= 1:
    single_breed.append(breed)

print("only 1", single_breed)

'''
create some better dog objects
first extract some data
'''


'''
BetterDog attributes on instantiation
name,  breed, size, age, sex, breedable, colour
'''
def buildDog(random_dog):
  colour = random_dog.iloc[0].Color
  name = random_dog.iloc[0].DogName
  breed = random_dog.iloc[0].Breed
  size = random_dog.iloc[0].Size
  sex = ''
  breedable = False
  if 'female' in random_dog.iloc[0].LicenseType.lower():
    sex = 'female'
    if 'spayed' in random_dog.iloc[0].LicenseType.lower():
      breedable = False
    else:
      breedable = True
  elif 'male' in random_dog.iloc[0].LicenseType.lower():
    sex = 'male'
    if 'neutered' in random_dog.iloc[0].LicenseType.lower():
      breedable = False
    else:
      breedable = True
  
  first_dog = BetterDog(name,breed,size, 0, sex, breedable, colour)
  return first_dog

list_of_dogs = []
for i in range(5):
  random_dog = dogdf.sample()
  adog = buildDog(random_dog)
  list_of_dogs.append(adog)

for dog in list_of_dogs:
  print(dog.bark())
  print(dog.dogInfo())
