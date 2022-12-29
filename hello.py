# hello.py
# Author: Robert Ellison
# A small script to say hello from Git

# load modules
import myname


# main code

# call the get_name function from the myname module
name = myname.get_name()

#print our welcome message
print("Hello {}".format(name),"from Git!")
