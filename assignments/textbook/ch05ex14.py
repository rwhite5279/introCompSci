"""
Chapter 5, Exercise 14, from Zelle's Python Programming, 2nd Ed.
Word count. A common utility on Unix/Linux systems is a small program call "wc." This program analyzes a file to determine the number of lines, words, and characters contained therein. WRite your own version of wc. The program should accept a file name as input and then print three numbers showing the count of lines, words, and characters in the file.
"""

def readFile():
    fileName = raw_input("What file would you like to read? ")
    inFile = open(fileName,"r")
    return inFile.read()   # reads the entire file as one long string

def getStats(text):
    # lines are separated by "\n", so lets split it up by that
    lines = text.split("\n")
    print "The number of lines is",len(lines)
    words = text.split(" ")
    print "The number of words is",len(words)
    print "The number of characters is",len(text)


def main():
    text = readFile()
    getStats(text)

if __name__ == "__main__":
    main()
