import os
import sys # pip install os-sys
import time

#you can clear the screen anywhere where u want to call the function

my_message = """This can also used to do new line
see it is working!! """

def typewriter(my_message):
    for char in my_message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.1)

        else:
            time.sleep(1)

os.system("cls") # for linux use clear instead of cls
typewriter(my_message) # call ur function 


#now you can use this anywhere where u want to use it  just copy the def part and paste it in your code
