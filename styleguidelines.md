# Style Guidelines 

## For functions
    
* All functions must have a docstring comment that explains what they take as parameters, what they do, and what they return
* Functions should be responsible for one thing only! 
    * Don't write a function that asks for user input, calculates and prints to screen
    * instead 
      1. ask for user input
      2. call a function with the argument(s)
      3. display the return value of the function
    * Why? The function is not tied to the user interface -> can be reused
* Be careful of indentation! Use the repl.it default - it will add indents if the previous line ends with a colon `:` (if you are using another editor for each indentation use 4 spaces)
* Add empty/blank lines (whitespace) before and after function definitions. Also add blank lines to indicate logical sections.

## Example
```python
''' 
add_five: This function adds 5 to the parameter and returns that value
parameter num: a  number
returns:  the given number plus 5
test data:
5 results in 10
100 results in 105
1.1 results in 5.1
'''
def add_five(num):
    return (num +5)
    
num = int(input('Enter a number'))

print(add_five(num))
```
## For variable and function names 
### Rules you must follow or else there will be a syntax error 
* name must start with a letter (or underscore _do not use underscore this way_)
* can contain letters, digits , and underscores
* variable names are case sensitive  (so `Add_tax` and `add_tax` and `Add_Tax` ... would be considered different functions (don't do this on purpose, it would be confusing))
* cannot be a **reserved** keyword
    * certain words already have a meaning in Python
    * if you tried to use the word as a variable or function name, Python would be confused about what you wanted to do
    * for example try naming a variable "if"  or "print"  you will create errors
### Rules most Python programmers follow, including you!
[Python.org PEP8 Conventions](https://www.python.org/dev/peps/pep-0008/)
* PEP8 is the Style Guide for Python Code
* variables start with a lowercase letter 
* Function names should be lowercase, with words separated by underscores as necessary to improve readability.
* Variable names should be lowercase, with words separated by underscores as necessary to improve readability.
* class names use camel case and must begin with a captial letter  (CamelCase is where each word begins with a capital letter.)
* Constants are written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.
Variable names follow the same convention as function names.

Variable names follow the same convention as function names.
* if a variable name is many words, use an underscore to separate
### Example
```python
# good names func
area_right_triangle()
# good names variable
length
height
# constany
GRAVITY   
# bad names funcs
a()
area()
# bad names variables
l
HEIGHT
h
```
