"""capitalize-whiter.py , by Richard White, 2011-04-19
This program capitalizes the first word in every sentence of an input string.
"""






























































"""
PSEUDOCODE
1. Get the user's input
2. Go through the string and identify the first word in each sentence.
3. Capitalize that word.
4. Print the edited string.

Note that, because strings are immutable in Python, you can't just 'reach in and replace a character.' Once you've found the character you want to replace, you need to:
a. break the string apart around that character, and
b. assemble it again around the new character.

Tricky!
"""


















































































def main():
    # This goes through every character in the string and looks 2 characters ahead to see what's happening.
    # Another approach would be to .split() the string up by ". ", and then capitalize the first character
    # in each of those substrings.
    userString = raw_input("Enter a string of text and I'll help you capitalize it: ")
    userString = userString.replace(userString[0],userString[0].upper(),1)
    for i in range(len(userString)-2):
        print "Examining",userString[i],"and",userString[i+2]
        if userString[i:i+2] in [". ","? ","! "]:
            print "We found a period and the character 2 ahead is a",userString[i+2]
            userString = userString[:i+2] + userString[i+2].upper() + userString[i+3:]
    print userString
    
if __name__ == "__main__":
    main()