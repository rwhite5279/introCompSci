#!/usr/bin/env python
# Sieve of Eratosthenes

maxPrime = input("Enter maximum prime, I'll give you all below that one: ")
allNums = []
for i in range(2,maxPrime+1):
    allNums.append(i)
# Go through list, first number is always a prime!
while len(allNums)>0:
    aPrime = allNums.pop(0) # prints 0 element 
                            # and removes from list
    print aPrime, "is prime!"
    # Need to remove multiples aPrime, but how?
    for aNum in allNums:
        if aNum % aPrime == 0:  # if aNum is a multiple of aPrime
            allNums.remove(aNum)


