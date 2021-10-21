#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program calculates the area of a square


import math


def calculate_area(side_length):
    # calculate area

    # process
    area = side_length * 4

    # output
    return area


def main():
    # this function gets the user input

    # input
    side_length_as_string = input("Enter the side length of a square (cm) : ")

    # call function
    try:
        side_length_from_user = float(side_length_as_string)
        if side_length_from_user > 0:
            calculated_area = round(calculate_area(side_length_from_user), 2)
            print(
                "\nThe area of a square with a side length of {0} cm is {1} cm.".format(
                    side_length_as_string, calculated_area
                )
            )
        else:
            print("\nNegative number entered, please try again.")
    except Exception:
        print("\nInvalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
