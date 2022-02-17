# given a year, month, day determine the day of the week
# using zellers congruence algorithm
# pmcampbell
# 2022-02-14

'''
implement the zellers congruence algorithm
params:   year, month, day
returns:  numeric day of week 0-6

(note y,c,m OKish ariable names, used for speed's sake taken directly from the formula given
test case
Feb 1, 1998 results in Sunday
'''
def zeller(year, month, day):
  y = year//100  # last 2 digits of year
  c = year %  100  # first 2 digits of the year
  m = month -2
  if m < 1:
    m = m - 1
    y = y - 1 
  
  day_number = ( (26*m - 2) / 10 + day + y + y/4 + c/4 +5 *c) % 7
  return day_number

#code the day_name function below
def day_name(day_number):
  if day_number == 0:
    day =  "Saturday"
    
  elif day_number == 1:
    day = "Sunday"
    
  elif day_number == 2:
    day =  "Monday"
  elif day_number == 3:
    day =  "Tuesday"
  elif day_number == 4:
    day =  "Wednesday"
  elif day_number == 5:
    day =  "Thursday"
  else:
    day =  "Friday"
  return day

#code the main function below
'''
main code drives the functions
'''
def main():
  year = int(input("enter a year: "))  
  month = int(input("enter a month: "))  
  day = int(input("enter a day: "))  
  print(f"That day is/was/will be a {day_name(zeller(year,  month, day))}")

# Code below ensures that the function called main is invoked when you run
if __name__ == "__main__":
    main()

