"""reverse_it.py by Richard White, 2011-04-18

This program takes any string entered by the user and reverses it, using three different techniques to do so. All three techniques, obviously, will need to produce the same output: the string, reversed."""































































"""PSEUDOCODE:
1. Get the string from the user (using a function?)
2. Reverse the string using one technique (going backwards through string with a for loop?)
3. Reverse the string using a second technique (string manipulation?)
4. Reverse the string using a third technique (converting it to a list and using the .reverse() function for lists?)
5. Show the results and end.


MORE PSEUDOCODE:

def get_string():
    pass

def reverse1(userInput):
    for end of string to beginning:
        print letter

def reverse2(userInput):
    print userInput[start:end:-1]

def reverse3(userInput):
    userList <- userInput # convert string to list
    userListReversed = userList.reversed()
    ReversedString = userListReversed.join()

def main:
    userString = get_string()
    print reverse1(userString)
    print reverse2(userString)
    print reverse3(userString)

if __name__ == "__main__":
    main()
"""































































































def get_string():
    userString = raw_input("Enter a string and I'll reverse it: ")
    return userString

def reverse1(userInput):
    """This function works by running backwards through the string, one character at a time. This is the old-fashioned way to do it, and although it's useful to know how to do this, it's not what you'd typically use in a Python program."""
    userInputReversed = ""
    for i in range(len(userInput)-1,-1,-1):
        userInputReversed += userInput[i]
    return userInputReversed

def reverse2(userInput):
    """This is the fancy Python way to do it, and it take up far less space on the page. Neat."""
    userInputReversed = userInput[::-1]
    return userInputReversed

def reverse3(userInput):
    """This technique converts the string to a list of characters, then uses the .reverse() method to reverse the order of that list. Finally, we join the list of characters back into a single string. Again, not ideal for THIS situation, but knowing how to use this technique can be useful!"""
    userList = list(userInput) # convert string to list
    userList.reverse()  # reverse list
    userInputReversed = ''.join(userList)  # convert list back to string
    return userInputReversed
    
def main():
    userString = get_string()
    print reverse1(userString)
    print reverse2(userString)
    print reverse3(userString)

if __name__ == "__main__":
    main()
