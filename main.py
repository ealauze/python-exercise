#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    number1 = int(input("Please enter number 1 : "))
    number2 = int(input("Please enter number 2 : "))
    number3 = int(input("Please enter number 3 : "))
    number4 = int(input("Please enter number 4 : "))
    number5 = int(input("Please enter number 5 : "))
    average = (number1+number2+number3+number4+number5)/5
    print("Average is : ", average)
    return 0

if __name__ == "__main__":
    main()
