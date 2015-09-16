__author__ = 'alicia.williams'

# CIS-125 FA 2015 9/16/15
# temptable.py
#
# This creates a pseudo-table of temperatures converting from Fahrenheit to Celsius.

def main():
    for C in range(0, 101, 10):
        F = (9 / 5 * C) + 32
        print(C, F)

main()