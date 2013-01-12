#!/usr/bin/python
# -------------- PROBLEM ----------------------

# Chapter 7, Programming Exercise #6
# The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a penalty of $200 for any speed over 90 mph. Write a program that accepts a speed limit and a clocked speed and either prints a message indicating the speed was legal or prints the amount of the fine, if the speed is illegal.










































# -------------- PSEUDO CODE -------------------

# Define the main function

#    Get driver's speed
#    Get speed limit
#    If speed <= speed limit:
#        print legal
#    else:
#        calculate fine based on $5 * difference
#        if speed > 10:
#            add $200 penalty
#        print total fine

# Call the main function






































# -------------- PROGRAM -----------------------

# ch07ex06.py, Chapter 7, Exercise 6
# From Zelle's Python Programming, Chapter 7
# By Richard White
# 2011-01-20

# This program calculates speeding fines

def main():

	# Get the driver's speed and the speed limit
    drivers_speed = input("Please enter the driver's speed: ")
    speed_limit = input("Please enter the speed limit: ")
    
    # Compare the driver's speed with the speed limit
    if drivers_speed <= speed_limit:
        print ("You keep driving safe, son.")
    else:
        print ("How fast do you think you were going?")
        print "I clocked you going", drivers_speed,"!"
        # Calculate the fine
        fine = 5.0 * (drivers_speed - speed_limit)
        print fine
        if drivers_speed > 90:
            fine += 200
        print ("I'm afraid that's going to be a %5.2f fine!" % (fine))

if __name__ == "__main__":
    main()
