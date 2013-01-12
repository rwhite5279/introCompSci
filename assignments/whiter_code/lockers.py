import os
import time
lockerNum = input("How many lockers? ")
lockers = []
for i in range(lockerNum):
    lockers.append(0)
for student in range(lockerNum):
    for locker in range(student,lockerNum,student+1):
        if lockers[locker] == 0: lockers[locker] = 1
        else: lockers[locker] = 0
    lockerstring = ''
    os.system('clear')
    for locker in lockers:
        lockerstring += str(locker)
    print lockerstring
    time.sleep(0.02)
