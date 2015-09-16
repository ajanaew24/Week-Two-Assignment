__author__ = 'alicia.williams'

# CIS-125 FA 2015 9/16/15
# convert.py
#
# This program converts temperature from Fahrenheit to Celsius.

F = eval(input("Please enter a temperature in Fahrenheit: "))

C = (F-32) * 5 / 9

print("The temperature", F, "in Fahrenheit is equal to", C, "Celsius")
