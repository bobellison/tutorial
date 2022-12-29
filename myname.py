# myname.py
# myname request module
# Author: Robert Ellison
# module to request the users name


# get_name function -- requests users name
def get_name():
    name = None
    while not name:
        name=input("Please enter your name: ")
    return name

