# -------------- PROBLEM ----------------------

# Chapter 3, Programming Exercise #3
# Write a program to determine the molecular weight of a hydrocarbon based on the number of hydrogen, carbon, and oxygen atoms. You sould use the following weights:
# ATOM           WEIGHT (grams/mole)
#-----------------------------------
# H              1.0079
# C              12.011
# O              15.9994












































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Ask the user for the number of Hydrogen, Carbon, and Oxygen atoms

#    Calculate the Total molecular weight based on the total number of atoms

#    Print out the molecular weight

# Call the main function













































# -------------- PROGRAM -----------------------

# ch03ex03.py, Chapter 3, Exercise 3
# From Zelle's Python Programming, Chapter 3
# By Richard White
# 2009-07-02

# This program has the user enter a number of hydrogen, carbon, and oxygen atoms
# in a molecule, and then prints out the molecular mass of that molecule.

def main ():
    # Constant values for atomic weights
    hydrogen_weight = 1.0079
    carbon_weight = 12.011
    oxygen_weight = 15.9994

    print "This program will calculate the molecular mass of a hydrocarbon for you."
    hydrogen_atoms = input ("Enter the number of hydrogen atoms in the molecule: ") 
    carbon_atoms = input ("Enter the number of carbon atoms in the molecule: ")  
    oxygen_atoms = input ("Enter the number of oxygen atoms in the molecule: ")   
    
    # Calculating total weight for the molecule
    molecular_weight = hydrogen_atoms * hydrogen_weight + carbon_atoms * carbon_weight + oxygen_atoms * oxygen_weight    

    print "The total weight of your molecule is",molecular_weight," amu."

main()
