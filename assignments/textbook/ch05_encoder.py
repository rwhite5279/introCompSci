# encoder.py, Chapter 4, Example
# From Zelle's Python Programming, Chapter 4
# A program to encode and decode messages

def encode_and_decode():
    inp = raw_input("Enter your message to be encoded: ")

    # Now, print out the numbers for each character entered
    for each_ch in inp:
        print ord(each_ch),
    print

    # Here, we convert each character's number to a list item, and then
    # print the list
    coded_inp = []
    for each_ch in inp:
        coded_inp = coded_inp + [ord(each_ch)] 
    print "The LIST of code values is: ", coded_inp

    # We can also take the numbers and put them into one long string of numbers,
    # and print that string
    # Note that we have to use the str function to convert the numbers to
    # string values to be concatenated
    coded_inp_string = ""    # initialize the string to be empty
    for each_ch in inp:
        coded_inp_string = coded_inp_string + str(ord(each_ch)) + " "
    coded_inp_string = coded_inp_string[0:-1]
    print "The string of code values is: ", coded_inp_string

    # Now we can print out the decoded versions, from both the list and the string form

    print "Now we'll decode your LIST of numbers for you!"
    for each_item in coded_inp:
        print chr(each_item),
    print

    print "And here's the decoded STRING of numbers:"
    import string   # Need this library for its functions
    message = ""
    for each_num in string.split(coded_inp_string," "):
        message = message + chr(eval(each_num))
    print message

encode_and_decode()


