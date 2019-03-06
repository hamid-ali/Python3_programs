"""
This script creates an empty file.
"""
#filename = input("Enter name of file u want to create")
import datetime
filename =datetime.datetime.now()
#create empty file
def create_file():
	with open(filename.strftime("%d.%m.%Y.txt"),"w+") as file:
		file.write("You have created this file on "+ filename.strftime("%d th of %B,%Y"))

create_file()
