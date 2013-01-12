# -------------- PROBLEM ----------------------

# Chapter 3, Programming Exercise #1
# Write a program to calculate the volume and surface area of a sphere from its radius, given as input. Here are some formulas that might be useful:
# V = 4/3(pi)r^3
# A = 4(pi)r^2



































# -------------- PSEUDO CODE -------------------

# Import the math library
# Define the main function

#	 Tell the user what this program is for
#    Ask the user what the radius is

#    Calculate the Volume
#    Calculate the Area

#    Print out the volume and area

# Call the main function






































# -------------- PROGRAM -----------------------

# ch03ex01.py, Chapter 3, Exercise 1
# From Zelle's Python Programming, Chapter 3
# By Richard White
# 2009-07-02

# This program has the user enter the radius of a sphere,
# and then prints out the Volume and Surface Area of that sphere

import math # This route makes use of the math library


def main():
    radius = input ("Enter the radius of a sphere (in [units]), and I'll tell you its Volume and Surface Area: ");
    volume = (4/3)*math.pi*radius**3; 
    surface_area = 4*math.pi*radius**2;  
    print "The radius of your sphere is", radius, "[units]."   
    print "The volume of this sphere is", volume, "[units^3]."
    print "The surface area of this sphere is", surface_area, "[units^2]."    

main()


