__author__ = 'alicia.williams'

# CIS-125 FA 2015 9/16/15
# mikilo.py
#
# This program converts distance from kilometers to miles.
def main():
    k = eval(input("Please enter a distance in Kilometers: "))
    m = 0.621371 * k
    print("The distance", k, "in Kilometers is equal to", m, "Miles")
    
main()