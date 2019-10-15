#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: October 2019
# This tells you if you can date the ladies grandchild

import constants

def main():
    # this function calculates area and perimeter
    
    # imput
    length = int(input("Enter Length of package (cm): "))
    width = int(input("Enter Width of package (cm): "))
    height = int(input("Enter Height of package (cm):  "))
    
    weight = int(input("Enter Weight of package in kg:  "))
    
    # process
    volume = length*width*height
    
    print("")
    print("")
    print("Weight is {} kg".format(weight))
    
    if constants.MAXWEIGHT > weight:
        print("The package's weight is not too heavy.")
    elif constants.MAXWEIGHT < weight:
        print("The package is too heavy! Must be below 27 kg!")
    elif constants.MAXWEIGHT == weight:
        print("The package is too heavy! Must be below 27 kg, not exactly.")
    
    print("")
    print("")
    print("Volume is {} cm^2".format(volume))
    
    if constants.MAXVOLUME > volume:
        print("The package is well sized.")
    elif constants.MAXVOLUME < volume:
        print("The package is too big! Must be smaller than 100 000 cm cubed!")
    elif constants.MAXVOLUME == volume:
        print("The package is too big! Must be smaller than 100 000 cm cubed, not exactly.")
    
    
if __name__ == "__main__":
   main()
