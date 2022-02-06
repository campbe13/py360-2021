# using random.seed
# the seed() function will customize the start number of the random number generator
# pmcampbell
# 2022-02-06

import random

dice = random.randint(1,6)
print(dice)
dice = random.randint(1,6)
print(dice)
dice = random.randint(1,6)
print(dice)

random.seed(10)
dice = random.randint(1,6)
print(f'seed 10 {dice}')
random.seed(10)
dice = random.randint(1,6)
print(f'seed 10 {dice}')
random.seed(10)
dice = random.randint(1,6)
print(f'seed 10 {dice}')

random.seed(15)
dice = random.randint(1,6)
print(f'seed 15 {dice}')
random.seed(15)
dice = random.randint(1,6)
print(f'seed 15 {dice}')
random.seed(15)
dice = random.randint(1,6)
print(f'seed 15 {dice}')
random.seed(15)
