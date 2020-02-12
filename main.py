#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    i=1
    numbers = 0
    while i < 6 :
        print("Please enter number ", i)
        number = int(input())
        numbers = numbers + number
        i = i + 1
    average = numbers / 5
    print("Average is : ", average)
    return 0

if __name__ == "__main__":
    main()
