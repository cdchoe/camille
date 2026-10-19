# 2.1 Vocab Review

# 1. git is a local tool on your computer, while github is a remote repository (like cloud)
# 2. terminal is the application that the command line is on. 
# 3. A local repository is a directory on your computer, while a remote repository is a directory stored on github. 
# 4. version control is a system that tracks, organizes, and manages changes to computer files. 
# 5. The staging area is where you put your files before committing them to a repository. 
# 6. git add is the command used to add files to the staging area. 
# 7. git commit is the command used to save changes to the local repository. 
# 8. git push is the command to save changes to the remote repository. 
# 9. git status is used to check the files in your local repository. 
# 10. git pull is the command used to get the latest changes from the remote repository.
# 11. pwd is used to print your current working directory. 
# 12. ls is used to list the files and directories in your current working directory. 
# 13. cd is used to change directory. 
# 14. nano is used to create and edit text files in the terminal. 
# 15. touch is used to create a new file. 
# 16. mv is used to move or rename files.
# 17. cm is used to remove files. 
# 18. cat is used to display the contents of a file.

# 2.2 A Directory Tree

# pwd
# ls
# cd ../brianna_repo and git pull
# mv homework.py ../judy_decal/homework
# cd ../judy_decal/homework
# cat homework.py
# git add ., git commit -m "changes to homework.py", git push origin main
# git pull origin main, git push origin main. Judy did not save the changes from her remote repository to her local repository before trying to push to the remote repository. 
# ~/Recent

# 3.1 Data Types

def checkDataType(x):
    if type(x) == int:
        return "int"
    elif type(x) == float:
        return "float"
    elif type(x) == str:
        return "str"
    elif type(x) == bool:
        return "bool"
    elif type(x) == list:
        return "list"
    elif type(x) == tuple:
        return "tuple"
    elif type(x) == dict:
        return "dict"

# 3.2 Conditionals

def evenOrOdd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

# 4 Loops

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 5.1 Lists

def duplicateList(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item)
    return new_list

# 5.2 Debugging

# The def line in the function is missing a colon at the end. 
def square(num):
    return num * num

# 6 Running Your Code
my_list = ['a', 'b', 'c']
print(my_list)
print(duplicateList(my_list))