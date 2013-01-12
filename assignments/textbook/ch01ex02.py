# ch01ex02.py
# Zelle, Chapter 1, Exercise 2
# By Richard White
# 2009-05-19

def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    for i in range(10):     # Do the random thing ten times
        x = 3.9 * x * (1-x)
        print x

main()   # We've defined the routine in this program... now we have to call it
         # so that it'll run!
