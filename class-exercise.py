# In JS
# function fahr_to_kelvin {
    #  return ((temp-32) * (5/9))+ 273.15
#}
#console.log(fahr_to_kelvin(100)) : runs without parameter

def fahr_to_kelvin(temp):
    return ((temp-32) * (5/9))+ 273.15

print (fahr_to_kelvin(100)) # without parameter (100), it will give type error

# functions must have a body
def first_function(): 
    pass # pass means do nothing, but sill works since pass is "body"

result = first_function()
print (result)


# In JS
# function firstFunction () {
#
#}

# Anonymous/inline function lambda

# // JavaScript
# const nums = [1, 3, 2, 6, 5];
# let odds = nums.filter(num => num % 2);

# Python
nums = [1, 3, 2, 6, 5]
odds = list( filter(lambda num: num % 2, nums) )
print (odds)

# Not allowed until after the code below, does not "hoist"
# add(5, 10)

# def add(a, b):
#   return a + b

# Calling Functions
# In Python, calling functions is the same as it is in JavaScript:

def add(a, b):
  return a + b
  
def sub(a, b):
  return a - b

def compute(a, b, op): #op = operator 
  return op(a, b)

print( compute(1, 2, add) )


#JS
#function compute (a, b, fn) {
    #return fn(a,b)
#} 
# compute (1,2, add)

# a & b are parameters
def add(a, b):
  return a + b
  num = 5

# num & 10 are arguments
add(num, 10)

def add(a, b):
  return a + b
  
add()
  
# Generates the following error:
# TypeError: add() missing 2 required positional arguments: 'a' and 'b'

# Accepting a varying number of arguments
# In JavaScript, we were able to access "extra" arguments being passed in to a function by using the special arguments:

# // Using the arguments special variable
# function sum() {
#   let total = 0;
#   for (arg of arguments) total += arg;
#   return total;
# }

# console.log( sum(1, 5, 10) );  // -> 16
# Or preferably by using ES2015's rest parameters:

# function sum(...nums) {
#   return nums.reduce((sum, num) => sum + num, 0);
# }

# console.log( sum(1, 5, 10) );  // -> 16

# Python's *Parameter Specifier (*args)
# Using the *specifier in a parameter list allows us to pass in a varying number of arguments into a function:

def f(*args):
  print( type(args) )  #returns the type "class tuples"
  for arg in args:
    print(arg)

f(1, 2, 'SEI')

def print_names(*names): 
    for name in names:
        print ("hello " + name)
    
print_names("Ji", "Matt", "Cody")

def print_names(greeting, *names): 
    for name in names:
        print (greeting + name)
    
print_names("Hello", "Ji", "Matt", "Cody")

# Always use the *argsparameter after any required positional parameters. For example:

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': []}
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

