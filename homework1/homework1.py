# File: homework1.py

#   --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print (c)
print(type(c)) # c is a complex data type, a number with a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a series of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is an array, a list of elements in a specific order

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs (words and their definitions)

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a collection of fixed values in a defined sequence

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is an array, a list of elements in a specific order

i = True
print(i)
print(type(i)) # i is a boolean, a data type that can only be true or false

j = None
print(j)
print(type(j)) # j is a nonetype, a data type that represents the absence of value or a null value (data type for the special constant None)

k = [True, "blue", 12]
print(k)
print(type(k)) # k is an array, a list of elements in a specific order

l = str(14)
print(l)
print(type(l)) # l is a string, a series of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals (any number containing an exponent sign is a float, even if it is a whole number)

'''
1. I found 9 different data types. 
2. integer, float, complex, string, array, dictionary, tuple, boolean, nonetype
3. b and m are both floats; d and l are both strings; e, h and k are both arrays
4. l is a string because it uses the str() function, which converts the integer 14 into the string "14"
5. range
'''

n = range(4)
print(n)
print(type(n)) # n is a range, a data type that represents a sequence of numbers (in this case, 0, 1, 2, 3)



#   --- Booleans ---

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # False, 10 is not equal to 9

print(10 <= 9) # False, 10 is greater than 9, not less than or equal to 9

print(bool("abc")) # True, any non-empty string is True

print(bool(123)) # True, any non-zero number is True

print(bool(["apple", "cherry", "banana"])) # True, any non-empty array is True

print(bool(True)) # True, the boolean value is True

print(bool(False)) # False, the boolean value is False

print(bool(0)) # False, 0 is False

print(bool("")) # False, an empty string is False

print(bool(" ")) # True, any non-empty string is True (this string is not empty because it contains a space)

print(bool(())) # False, an empty tuple is False

print(bool([])) # False, an empty array is False

print(bool({})) # False, an empty dictionary is False

print(bool(True and False)) # False, both sides of the and operator must be True for the statement to be True

print(bool(True and True)) # True, both sides of the and operator are True

print(bool(False and False)) # False, both sides of the and operator must be True for the statement to be True

print(bool(True or False)) # True, only one side of the or operator must be True for the statement to be True

print(bool(True or True)) # True, both sides of the or operator are True

print(bool(False or False)) # False, both sides of the or operator are False

print(bool(not(False))) # True, the not operator reverses the boolean value of False to True

print(bool(not(True))) # False, the not operator reverses the boolean value of True to False

'''
I noticed the pattern that anything empty is False. 
I was most surprised by the result of print(bool(True or False)). 
print(bool({"name": "Camille"})) will return True because the dictionary is not empty. 
print(bool(not(not(False)))) will return False because the inner not reverses the False to True, then the outer not reverses the True to False. 
'''



#   --- Operators ---

# Arithmetic Operators

print(10 + 5) # 15, + performs addition

print(10 - 5) # 5, - performs subtraction

print(2 * 4) # 8, * performs multiplication

print(6/3) # 2.0, / performs division, which always returns a float

print (5 % 2) # 1, % performs the modulus (remainder after division)

print(3 ** 2) # 9, ** performs exponentiation

print(15 // 2) # 7, // performs floor division (division that rounds down to the nearest whole number), which always returns an integer

# Comparison Operators

print(5 == 2) # False, == checks if two values are equal

print (10 != 10) # False, != checks if two values are not equal

print(2 < 5) # True, < checks if the left value is less than the right value

print(12 > 5) # True, > checks if the left value is greater than the right value

print (5 <= 6) # True, <= checks if the left value is less than or equal to the right value

print (1 >= 10) # False, >= checks if. the left value is greater than or equal to the right value

# Assignment Operators

x = 5
x += 5
print(x) # x = x + 5, += adds the right number to the current value of the left number

x = 5
x -= 4
print(x) # x = x - 4, -= subtracts the right number from the current value of the left number

x = 5
x *= 3
print(x) # x = x * 3, *= multiplies the current value of the left number by the right number

# Logical Operators

'''
1. The and operator returns True only if both statements are True, and returns false otherwise. print(True and True) will return True, and print(True and False) will return False. 
2. The or operator returns True if at least one of the statements is True. print(True or False) will result in True, and print(False or False) will result in False. 
3. The not operator reverses the boolean value of a statement. print(not(False)) will return True, and print(not(True)) will return False. 
'''

'''
1. / performs division and always returns a float, while // performs floor division, a type of division that rounds down to the nearest whole number, and always returns an integer. 
2. % performs the modulus, which returns the remainder after division, while // performs floor division. 
3. You would use % to calculate the remainder when dividing two numbers. For example, print(15 % 4) will return 3, because that is the remainder when 15 is divded by 4. 
4. Assignment operators work by assigning a new value to a variable based on its current value. 
'''



#   --- Strings ---

my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h

print(my_string[1]) # Prints: e

print(my_string[2]) # Prints: l

print(my_string[3]) # Prints: l

print(my_string[4]) # Prints: o

print(my_string[-1]) # Prints: o

print(my_string[1:3]) # Prints: el

print(my_string[0:5:2]) # Prints: hlo

print(len(my_string)) # Prints: 5

print(my_string + "goodbye") # Prints: hellogoodbye

print(my_string * 7) # Prints: hellohellohellohellohellohellohello

'''
1. Slicing means to take a specific portion of a string. I sliced my string in manipulations 2-9. 
2. Prints: Hello, my name is Oski
3. Prints: Hello, my name is Oski
4. The difference between the last two print statements is that the second one contains an f-string, which allows you to embed variables directly into the string instead of writing it as a separate part of the statement, like in the first print statement. 
'''

name = "Oski"
print("Hello, my name is", name)

name = "Oski"
print(f"Hello, my name is {name}")



#   --- Terminal Commands ---

''' 
cd
Change Directories. Use it to move from one folder to another
Example: cd Desktop

ls
List. Lists files and folders inside the working directory. 
Example: ls

ls -a
List All. Lists all files and directories (including hidden ones) inside of the working directory
Example: ls -a

mkdir
Make Directory. Makes a new directory inside of your working directory. 
Example: mkdir python_decal

cat
Displays the contents of a file.
Example: cat file.txt

pwd
Print Working Directory. Returns the directory you are currently in. 
Example: pwd

cd ..
Change Directory. Moves you up one level from your working directory. 
Example: cd ..

cd .
Change Directory. Moves you zero levels from your working directory (keeps you where you are)
Example: cd . 

cd ~
Change Directory. Moves you from your working directory to the home directory. 
Example: cd ~

cp
Copy. Copies a file into a specific directory. 
Example: cp file.txt ~/Downloads/

mv
Move. Moves files and directories to other directories. 
Example: mv file.txt ~/Desktop/

rm
Remove. Deletes files and directories
Example: rm file.txt

clear
Clear. Clears your terminal window of previous commands and outputs. 
Example: clear

grep
Global Regular Expression Print. Searches for specific text patterns. 
Example: grep "find_this" file.txt
'''

'''
1. nano: opens a text editor (opens, creates, and edits text)
   less: used to view the contents of a text file one screen at a time (does not load the entire file at once)
   head: shows the first 10 lines of a file
2. ls -a shows all directories and files, while ls does not show the hidden directories and files. 
3. Hidden files are files that do not normally show up in directory listings, They are usually background data, protected system, files, or store configurations. 
4. -n specifies the amount of lines or line numbers used in a terminal command
   -i allows grep to perform a case-insensitive search
   -l uses long listing format (shows permissions, owner, size, and date)
'''