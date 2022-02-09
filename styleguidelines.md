# Style Guidelines for functions
    
* All functions must have a docstring comment that explain what they take as parameters, what they do, and what they return
* Functions should be responsible for one thing only! 
    * Don't write a function that asks for user input, calculates and prints to screen
    * instead 
      1. ask for user input
      2. call a function with the argument(s)
      3. display the return value of the function
    * Why? The function is not tied to the user interface -> can be reused
* Be careful of indentation! Use the repl.it default - it will add indents if the previous line ends with a colon `:`
* Add empty/blank lines (whitespace) before and after function definitions. Also add blank lines to indicate logical sections.

## Example
```python
''' 
This function adds 5 
parameter num: a  number
returns:  the given number plus 5
'''
def add_five(num):
    return (num +5)
    
num = int(input('Enter a number'))
print(add_five(num))
```
