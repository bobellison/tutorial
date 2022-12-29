# myname.py
# Author: Robert Ellison

name = None

# get_name function -- requests users name
def get_name():
    while name is None:
        name=input("Please enter your name: ")
    return name

