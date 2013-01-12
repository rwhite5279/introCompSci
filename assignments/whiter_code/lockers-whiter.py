"""lockers-whiter.py , by Richard White, 2011-04-18
THE LOCKER PROBLEM
There are 1000 students at a school, and each student has a locker, and the lockers are all in a line, and numbered from 1 to 1000. The lockers are all initially closed at the start of the problem, when student #1 starts at locker # 1, and visits locker, opening them. Student #2 starts at the second locker, and visits every other locker (2, 4, 6, etc.), and closes them. Student #3 starts at locker #3 and visits every third locker (3, 6, 9, etc), and closes the door if it's open, or opens the door if it's closed. This process continues until all 1000 students have traveled along the line of lockers.

What is the final state of each locker in the row of 1000 lockers? Write a program to simulate the opening and closing of the lockers in this problem."""
























































"""
ANALYSIS / STRATEGY
1. Let the row of lockers be represented by either a string of characters or a list of digits, 0 for closed and 1 for open. Initialize the list so that all lockers are closed.
2. Begin a student loop that will track each student as they go through the lockers.
3. Begin a locker loop that will track each door, based on the student number
4. For each door in our loop, open the door if it's close, or close it if it's open.
5. Once the loops are done, print out the locker statuses.

* To help the development, consider starting with a smaller number of lockers, say 10, or 50.
* Use lots of print statements during development to reveal what's going on.
"""





































"""
MORE DETAILED PSEUDOCODE
1. for every locker: locker[i] = 0
2. for student in range[1,1000]:
3.     for locker in range[student,1000,student]:
4.         if locker is 0, make it 1:
5.         else make it 0 # it had to have been 1
6. print lockers
"""



















































import time

def close_lockers(num_of_lockers):
    lockers = []
    for i in range(num_of_lockers):
        lockers.append(0)
    return lockers

def print_lockers(lockers):
    lockerString = ""    
    for locker in lockers: lockerString += str(locker)
    print lockerString

def main():
    num_of_lockers = 100
    lockers = close_lockers(num_of_lockers)
    for student in range(1,num_of_lockers + 1):  # Students are 1 - 1000
        for x in range(student ,num_of_lockers + 1,student):
            lockers[x-1] = (lockers[x-1] + 1) % 2  # flips bit between 0 and 1
            print_lockers(lockers)
            time.sleep(0.05)
    print_lockers(lockers)



if __name__ == "__main__":
    main()
