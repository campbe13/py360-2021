# example using tuple
# pmcampbell
# 2022-02-17

def sumproduct(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product
    
def main():
    sum1, prod1 = sumproduct(5,15)
    print(f" 5 and 15 sum {sum1} prod {prod1}")
    sum2, prod2 = sumproduct(55,15)
    print(f" 55 and 15 sum {sum2} prod {prod2}")
    
if __name__ == "__main__":
    main()
