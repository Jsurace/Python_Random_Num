"""
Program: int_file.py
Author: Jenna
Date: 3/14/2019

Program will open a file named 'integers.txt' if that file does not
exist, it will create it. The program will then loop writing 15
random numbers to the txt file and then close the file.
"""

import random 

myFile = open("integers.txt", "a")

myFile.write("Here are the new numbers!\n")

for count in range(15):
	number = random.randint(1, 500)
	myFile.write(str(number) +'\n')

myFile.close() 
