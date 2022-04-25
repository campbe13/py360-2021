'''
defines the BetterDog class

Improvement on the original Dog class, for use with dataset
(no age given)
'''

class BetterDog:
  # initializer
  def __init__ (self, name,  breed, size, age, sex, breedable, colour):
    # init attributes
    self.name = name # str
    self.breed = breed   # str
    self.size = size  #str
    self.age = age  # int
    self.sex = sex  # str
    self.canbreed = breedable # bool
    self.colour = colour  # str
  # behaviours
  def bark(self):
    if self.size in ['small','medium']:
      return 'yip yip yip'
    elif self.size == 'xlarge':
      return 'ROWF ROWF ROWF'
    else:
      return 'rowf rowf rowf'
  def changeAge(self, newage):
    if newage < 0 or newage > 25:
      return
    self.age = newage
  def isBreedable(self):
    return self.canbreed
  def dogInfo(self):
    return (f"Name {self.name} breed {self.breed} {self.size} {self.colour}")
