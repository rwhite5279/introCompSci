# factorial.py
# From Zelle's Python Programming, Chapter 3
# By Richard White
# 2009-06-02

import math # This program calculates factorials

def main():
    n = input("Enter the number for which you want to calculate the factorial:")
    fact=1
    for i in range (n, 1, -1):
        fact=fact * i
    print "The factorial of ",n," (",n,"!) is ", fact

main()


