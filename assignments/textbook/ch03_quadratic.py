# quadratic.py
# From Zelle's Python Programming, Chapter 3
# By Richard White
# 2009-06-02

import math # This route makes use of the math library to
            # demonstrate the sqrt function

def main():
    print "This program find the real solutions to a quadratic equation."
    print
    a, b, c = input("Please enter the coefficients (a, b, and c):")
    disRoot = math.sqrt(b*b-4*a*c)
    root1 = (-b + disRoot)/(2*a)
    root2 = (-b - disRoot)/(2*a)
    print
    print "The solutions are:", root1, " and ", root2

main()


