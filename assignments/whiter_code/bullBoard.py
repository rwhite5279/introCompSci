#!/usr/bin/env python
"""
bullBoard-crashwhite.py
This program demonstrates some of the ways that Python can interact with an sqlite database.


"""

import sqlite3    # This module is required to work with an sqlite database
import hashlib    # This module produces hash values for our database
import random     # Used to create random hash values
import datetime   # Used to get the current date and time
import os         # Used so we can turn off the tty during password entry

#################### FUNCTION TO CONNECT TO DATABASE #################

def connect_to_database():
    # Connect to the database if it exists, otherwise create it.
    connection = sqlite3.connect('bullBoard.sqlite')
    # The cursor() object is used to execute SQL queries (interacting with the database).
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS "userTable" 
                ("userID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                 "userNick" VARCHAR NOT NULL UNIQUE,
                 "userEmail" VARCHAR NOT NULL UNIQUE,
                 "userSignup" DATETIME NOT NULL DEFAULT CURRENT_DATE,
                 "userHash" CHAR NOT NULL,
                 "userPassword" VARCHAR NOT NULL, 
                 "userActive" BOOL NOT NULL DEFAULT True)''')
                 
    c.execute('''CREATE TABLE IF NOT EXISTS "commentTable"
                ("commentID" INTEGER PRIMARY KEY NOT NULL,
                 "commentThread" INTEGER,
                 "commentUserID" INTEGER,
                 "commentTime" DATETIME NOT NULL DEFAULT (CURRENT_DATE),
                 "commentHash" CHAR,
                 "comment" CHAR,
                 "commentFlagged" BOOL NOT NULL DEFAULT False)''')
    return c, connection
   
   
##################### FUNCTION TO CLOSE THE DATABASE ###################

def close_database(connection):
    # Close the database connection when we're done with it.
    connection.close()

#################### FUNCTION TO ADD A USER -- GOOD STUFF HERE! #################    

def add_user(c,connection):
    """
    This function collects user data and adds it to the
    database via cursor c. Don't assemble directly using
    strings due to insecurity--use tuples. See 
    http://docs.python.org/library/sqlite3.html 
    for more info.
    """
    nickname = raw_input("Enter usernickname: ")
    email = raw_input("Enter your email: ")
    os.system("stty -echo")	# Disable local echo
    password = raw_input("Enter a password: ")
    os.system("stty echo")  # Enable echo again
    print ""
    now = datetime.date.today()  # current day
    # create random 32-character hash to represent user
    userHash = hashlib.sha1(str(random.random())).hexdigest()  
    # create random 32-character hash of their password
    userPassword = hashlib.sha1(password).hexdigest()
    """
    To execute an SQL query for SQLite, Python needs to
    assemble the query contents in a tuple. Once you've
    established a means for executing an SQL query, you
    have to:
        a. assemble the query
        b. execute it using the cursor (c)
    """
    # checks database to see if someone is there already
    c.execute('SELECT userNick, userEmail from userTable \
    WHERE userNick = ? or userEmail = ?', (nickname, email))
    # (Tuple) above substitutes in for ? in statement
    # Get results from the query and store in list data
    data = c.fetchall()   
    """ If we got any results from that query,
    let them know that their data is duplicated."""
    if len(data) > 0:         
        print "I'm sorry.",
        for row in data:
            if row[0] == nickname:
                print "That nickname is already taken."
            if row[1] == email:
                print "That email is already registered"
    else: # No duplicates, so enter info!
        # Assemble data into a tuple   
        myTuple = (nickname,email,now,userHash, \
        userPassword,'True')
        c.execute('INSERT into userTable (userNick, \
        userEmail, userSignup, userHash, userPassword, \
        userActive) values (?,?,?,?,?,?)', myTuple)   
        # Save ("commit") the changes to the database
        connection.commit()
        print "User successfully added to databases."
        
####################### FUNCTION TO VIEW ALL USERS #######################################

def view_users(c):
    """This function lists all users, emails, and statuses in the database"""
    c.execute('SELECT userNick, userEmail, userActive from userTable')
    data = c.fetchall()
    print "%1s%78s%1s" % ("+",78*"-","+")
    print "|%15s|%50s|%11s|" % ("userNick","email","active")
    print "%1s%74s%1s" % ("+",78*"-","+")
    for record in data:
        print "|%15s|%50s|%11s|" % (record[0],record[1],record[2])
    print "%1s%78s%1s" % ("+",78*"-","+")
    
    
######################## ADD COMMENT FUNCTION ##########################################

def add_comment(c,connection):
    """This function adds a comment from a user"""
    nickname = raw_input("Which user is adding the comment? ")
    # Check to get an id for that user
    c.execute('SELECT userID, userPassword from userTable WHERE userNick = ?', ([nickname]))
    data = c.fetchall()
    if len(data) == 1:
        userID = int(data[0][0])
    else:
        print "There was an error finding that user."
        return
    print "Password for",nickname,":",
    password = raw_input()
    password = hashlib.sha1(password).hexdigest()
    if password != data[0][1]:   # Password retrieved from database
        print "Password is incorrect."
        return
    comment = raw_input("What comment is that user adding? ")
    commentThread = input("What comment thread is this in response to, if any (0 if original)?")
    now = datetime.datetime.today()
    # create random 32-character hash to represent comment
    commentHash = hashlib.sha1(str(random.random())).hexdigest()
    myTuple = (commentThread,userID,now,commentHash, comment,'False')
    c.execute('INSERT into commentTable (commentThread, commentUserID, commentTime, commentHash, comment, commentFlagged) values (?,?,?,?,?,?)', myTuple)   
    # Save ("commit") the changes to the database
    connection.commit()


######################## VIEW COMMENT FUNCTION ##########################################

def view_comments(c):
    """This function allows the user to see comments, threaded by subject"""
    c.execute('SELECT userTable.userID, userTable.userNick, commentTable.commentID, commentTable.commentThread, commentTable.commentUserID, commentTable.commentTime, commentTable.comment \
    from userTable \
    JOIN commentTable \
    ON userTable.userID = commentTable.commentUserID \
    WHERE commentTable.commentFlagged == "False" \
    ORDER BY commentTable.commentTime') 
    data = c.fetchall()
    for record in data:
        if record[3] == 0:  # if thread originator
            print "\n============"
            print "Author:",record[1]
            print "Comment:",record[6]
            print "Time:",record[5]
            print "Replies:"
            for record2 in data:
                if record2[3] == record[2]:  # does thisID match Thread?
                    print "\n-------------"
                    print "\tAuthor:",record2[1]
                    print "\tComment:",record2[6]
                    print "\tTime:",record2[5]
    print # line spacer


####################### FUNCTIONS TO DEBUG PROGRAM #######################################

def view_user_table(c):
    c.execute('SELECT * FROM userTable')
    data = c.fetchall()
    for record in data:
        for field in record:
            print field,
        print "\n-------"
    
  
def view_comment_table(c):
    c.execute('SELECT * FROM commentTable')
    data = c.fetchall()
    for record in data:
        for field in record:
            print field,
        print "\n-------"
    
####################### MAIN PROGRAM, INCLUDING CONNECTING TO THE DATABASE ################

def main():
    c, connection = connect_to_database()
    choice = ""
    while choice != "5":
        print "1. Add User"
        print "2. View Users"
        print "3. Add Comment"
        print "4. View Comments"
        print "5. Quit"
        print "TEMPORARY DEBUG OPTIONS"
        print "6. View User Table"
        print "7. View Comments Table"
        choice = raw_input("> ")
        if choice == "1":
            add_user(c, connection)
        elif choice == "2":
            view_users(c)
        elif choice == "3":
            add_comment(c,connection)
        elif choice == "4":
            view_comments(c)
        elif choice == "5":
            break
        elif choice == "6":
            view_user_table(c)
        elif choice == "7":
            view_comment_table(c)
        else:
            print "Please enter a number 1-5."
    close_database(connection)

if __name__ == "__main__":
    main()
    
