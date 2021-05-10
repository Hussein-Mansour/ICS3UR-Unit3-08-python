#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon/May10/2021
# This program Determines if a year is a leap year


def main():
    # this function checks if its a leap year or not

    # input
    year_str = input("please enter the year:")

    # process  & output
    try:
        year_int = int(year_str)

        if (year_int % 4):
            if (year_int % 400):
                print("{} not a leap year.".format(year_int))
            else:
                print("{} is definitely a leap year!".format(year_int))
        else:
            print("{} is definitely a leap year!".format(year_int))

    except Exception:
        print("invalid input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
