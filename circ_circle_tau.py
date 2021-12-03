#!/usr/bin/env python3
# Created By: Logan Sweeney
# Date: Dec. 2, 2021
# This program asks the user for the radius and
# calculates and displays the circumference using TAU.
import constants
import time

x = 2.5


def main():
    # get user input
    print("Today we will calculate the circumference of a circle.")
    radius = float(input("Enter radius (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Calculating...")
    time.sleep(x)
    print("")
    print("The circumference is: {}mm".format(circumference))


if __name__ == "__main__":
    main()
