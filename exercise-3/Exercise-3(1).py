
# coding: utf-8

# 
# ![](https://i.stack.imgur.com/OtSPD.png)
# 
# ## Exercise 3: Python through a Jupyter notebook
# 
# 
# Python is a programming language that basically allows you to "do things to objects." The objects in python are called variables, the things you can do to variables are called functions. We start this week by going through some of the types of objects in python, and then present some of the things you can do to them. 
# 
# But first, let's look at programming basics.

# In[90]:

# This is my first python notebook!

# Any line in a python file that begins with a "#" character ("hashtag", "octothorpe", ...) is a comment- 
# Comments are human-readable lines that explain what the computer code is performing
# Python ignores these lines, but any human should be able to read the comments in your code 
# to figure out exactly what your program does. 


# ### Python can function as an overpowered calculator:

# In[9]:


# add, multiply, exponentiate
print(2+2)
print(2*3)
print(2**3)
print(2-3)
print(2-3+6)

# programs often make use of the modulus operator:
print(8 % 3)
print(2*3**3)
print(15%2)
print(15%7)
print(30%7)

# see pages 59-60 of CSB text for a full list of mathematical operators


# ### Questions to answer:
# 
# **What does this modulus operator achieve? How did you figure this out?**    
# 
# [your answer here]
# Modulus operator achieves the biggest result when we divide some numbers then the commands leave the reminder. So, by using this command, we actually will know how much the reminder. I figure out this command by reading Allesina's book and making some examples.
# 
# 
# 
# **Briefly describe a scenario in which this might be useful.**  
# 
# [your answer here]
# In my opinion, modulus command is one of the interesting commands since this will be very useful for some calculations using Python.
# 

# In[92]:

# Comments can go after a line of valid code:

print("This line has both code and comments") # here is a comment


# In[93]:

# Python can do comparisons

# is (5+7) greater than (2*6)?
(5+7) > 2*6


# In[94]:

# is (5+7) greater than or equal to (2*6)?
(5+7) >= 2*6


# ### Variable names 
# 
# A lot of computing involves manipulating variables. You can think of variables as a box that hold some information. Variables can hold different types of information - some can contain integers, others might contains text strings, others might have a combination, etc. When we name a variable, we basically assign a name to some piece of information:

# In[95]:

# Let's make a variable called "favorite_pizza_topping" and assign it the value "grapes"

favorite_pizza_topping = "grapes"


# In[96]:

# Then we can see what we saved in favorite_pizza_topping
favorite_pizza_topping


# In[97]:

# We can override what is saved in an existent variable:
favorite_pizza_topping = "feta cheese"


# In[98]:

favorite_pizza_topping


# In[99]:

# Let's play with some numbers

a = 10
b = 7

a - b
a - 2


# ### Assigning variables with "=" vs. comparisons with "=="
# 
# A single `=` sign is used for assigning values to variables, but a double equal to sign `==` is used to check if two objects are identical

# In[100]:

# assign
a = 10


# In[101]:

a == 100


# In[102]:

a == 10


# ### Object types
# Python has several different "types" of objects. Some of these are very straightforward - e.g. `integer`, `string`; others might d a little less obvious, e.g. `list`, `dictionary`. I won't introduce dictionaries formally here - see line 444 of CSB Ch. 3.

# In[103]:

a = 100
type(a)


# In[104]:

type("a")


# In[105]:

fruits = ["apples", "grapes", "bananas"]
type(fruits)


# ### Conditionals in Python
# *Conditional* statements allow us to write programs that behave differently based on some external parameters. For example, we might want to write a program that prints "Endangered species present!" if a sample of DNA is found to have sequences from an endangered species, or "No endangered species detected" if not.

# In[106]:

a = 5

if a == 5: # note that all if statements are of the structure "if <CONDITION> :
    print("a is equal to 5") # note that the entire "body" of an if statement must be tabbed over (4 spaces)


# In[107]:

if a == 6:
    print("a is equal to 6") 
# Nothing printed from this output, since we don't ask the program to do anything if a is not equal to 6


# In[108]:

if a == 6: 
    print("a is equal to 6")
else: # no <CONDITION> required for else statement- the statement is just run if the previous conditional is False
    print("a is not equal to 6")


# In[109]:

# we can do conditionals on strings

food = "pizza"

food == "pizza"


# In[110]:

# Series of if-else statements with elif

a = 5

if a <= 4:
    print("a is less than or equal to 4")
elif a >= 6:
    print("a is greater than or equal to 6")
else: 
    print("a is neither greater than or equal to 6, nor less than or equal to 4")


# ### Functions
# As I said above, python is a language that lets you do things to objects. We've explored some of the types of objects - `int`, `str`, `list`, etc. Now, we begin to explore how to do things to these objects.
# 
# There are two ways to do things in python- first, we can use built-in or custom-written functions; second, we can use object-specific methods. We will explore each of these in turn.
# 
# Let's begin with built-in functions. We have used some of these already (`print()`, `type()`), but there's a lot more out there.

# In[111]:

# Built in functions

# All functions are of the format "name_of_function(user_input)", where "user_input" is something the user defines.

# the len() function returns the length of a list

fruits = ["apples", "grapes", "bananas"]
len(fruits)


# In[112]:

# abs() returns the absolute value
abs(-123)


# In[113]:

# the help() function returns help files for other functions
help(abs)


# #### Custom defined functions
# The power of programming lies in writing custom functions that make computers perform complicated tasks to our specifications- we achieve this by writing custom functions.

# In[114]:

# let's write a simple function that returns "three times the square of the input value":

def sq_times_three(number): # all custom functions are written as "def function_name(input):"
    return((number**2)*3)   # the body of the function is always tabbed over (4 spaces)


# In[115]:

# test our custom function
# sq_times_three(2) should return (2^2)*3 = 12
sq_times_three(2) 


# In[116]:

# sq_times_three(-3) should return (-3^2)*3 = 27
sq_times_three(3)


# Functions in python don't just do mathematical operations. They can take any input and return any output. 
# 
# Let's write a function that performs the following task (Adapted from Google for Education's Learn Python module):
# 
# ````
# # Function name: donuts
# # Given an int count of a number of donuts, return a string
# # of the form 'Number of donuts: <count>', where <count> is the number
# # passed in. However, if the count is 10 or more, then use the word 'many'
# # instead of the actual count.
# # So donuts(5) returns 'Number of donuts: 5'
# # and donuts(23) returns 'Number of donuts: many'
# ```
# 
# Let's make a game plan first:  
# 1. The function should be called `donuts`, so the first line should be `def donuts(count):`.  
# 2. The function needs to perform different things based on what is the value of counts. Do we know how to make a computer perform different tasks based on input? 
# [YOUR ANSWER HERE]
# 3. The function then needs to return a string.
# 
# 
# **Write your solution in the next code chunk**. Hint: you can concatenate a variable to a defined string using the format `print("words" + variable)`. Check your code by removing the comment hashtags

# In[117]:

#def donuts(count):
#    if (condition):
#        return(a string)
#    else:
#        return(a different string)
# donuts(5)
# donuts(23)


# #### Object Methods
# 
# Python is an object oriented language- all objects contain data but also some useful methods of manipulation. See Section 3.4.5 in CSB text for more on this.

# ### Regular Expressions in python using the re library
# 
# We can do regular expressions in python by importing the `re` library (a library is a set of functions that is not shipped with the core python program but can be imported in as needed). The `re` library contains a lot of functions that can help with string manipulation, as I demonstrate below.

# In[118]:

import re
my_string = "Hello, world!"

# we can just find a string
print(re.findall(pattern=",", string=my_string)) # find a comma
# find a space (\s), followed by the letter 'w', followed by any character (.*)
print(re.findall(pattern="\sw.*", string=my_string)) 


# In[119]:

# From last week
line = "denovo105;   Orthopteroidea; 100; Orthoptera; 100; Ensifera; 100; Grylloidea; 100; Gryllidae; 100; Gryllinae; 100; Gryllodes; 50; Gryllodes sigillatus; 50;"
to_write = re.search("(denovo\d*;).*;\s100", line)
print("group 0 of the regex is:")
print(to_write.group(0))

print("\ngroup 1 of the regex is:")
print(to_write.group(1))


# In[120]:

# Regular expressions for matching patterns in DNA 
dna = "ATCGCGAATTCAC"
if re.search(r"GC(A|T|G|C)GC", dna):
    print("restriction site found!")


# ## Homework
# 
# This homework should be submitted as an ipython notebook file committed in your github repo by next Wednesday, 1 Feb.
# 
# \1. Create a new ipython notebook in your `exercise-3` folder within `lab-work`. Call this file "Exercise-3-hw". 
# \2. Define the following variables in your new ipython notebook:
# 
# ```
# set "a" equal to 3
# set "b" equal to 17
# set "c" equal to the sum of a and b
# 
# set "favorite_animal" to one of your favorite animals
# 
# set "favorite_dinners" to a list of three of your favorite dinners
# 
# set "num_fav_dinners" to the number of items in your "favorite_dinners" list. NOTE: You must use the len() function to achieve this task.
# ```
# 
# \3. Write a function named "hw3_function". This function must meet the following criteria: 
# 
# ```
# The function should take an integer as an input. If the user runs the function with something that is not an integer, your function should print an error message.
# 
# If the integer is less than 5, return the message "Brr! It's cold!"
# If the integer is greater than 25, return the message "It's pretty warm!"
# If the integer is between 5 and 25, return the message "What a pleasant temperature!"
# 
# For example, hw3_function("duck") should return an error
# For example, hw3_function(17) should return "What a pleasant temperature!"
# ```
# 
# \4. Consider the DNA string "ATAATTAACGGAGCTTATTA". Write a python regular expression that will search for the patter "G, A or T, A or T, G, A or T or G or C".
# 
# \5. Write a function that plays "Rock Paper Scissors" with the user. Your functions should meet the following criteria:
# 
# ```
# The function shold be named "rps"
# 
# The user must input the words "rock" or "paper" or "scissors" into the function. If the user enters anything else, the function should print a statement asking the user to run it again properly.
# 
# The function should randomly select one of "rock, paper, scissors" each time it is run. Hint: you wil have to use the "choice" function in the "random" library to select from a list each time. Feel free to google for advice on this.
# 
# The function should follow the standard rules of rock paper scissors ("rock beats scissors; scissors beats paper; paper beats rock; tie of both the same") to determine a winner.
# 
# The function should return a string of the following format: "You picked <user_choice>; Computer picked <random_choice>; +1 for <You or Computer>!"
# 
# For example, rps("rock") can return either one of the three sentences, depending on which is sampled randomly:
# "You picked rock; Computer picked rock; this is a tie!"
# "You picked rock; Computer picked paper; +1 for Computer!"
# "You picked rock; Computer picked scissors; +1 for You!"
# ```
# 
# 

# In[ ]:




# In[ ]:




# In[ ]:



