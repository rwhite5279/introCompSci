#!/usr/bin/python

"""FIX EXCEL CALENDAR EXPORT, by Richard White, 2010-01-25
   This program fixes Excels "export for web" results by:
   a) Converting all '.5pt' occurences to '1px'
   b) Removing 'table-layout:fixed' from table header, and
   c) Removing all 'width=' specifications
   d) Remove a:link {...} and a:visited {...}  NOT YET IMPLEMENTED
"""

import sys
import string
import re

def main(arg):
    print "Opening file",arg
    infile = open(arg,"r")
    lines = infile.read()
    infile.close()
    
    # Convert .5pt to 1px
    lines = string.replace(lines,'.5pt','1px')  # .5pt doesn't show up on some browsers
    
    # Remove table-layout:fixed
    lines = string.replace(lines, 'table-layout:fixed','')
    
    # Remove width specifications
    lines = re.sub('width=\d*','',lines)
    
    # Remove a:link {} and a:visited {}
    # This turns out to be really hard!
    
    # Write to a new file, with '-processed' in the filename
    infile_name = string.split(arg,'.')
    newfile_name = infile_name[-2] + '-processed.' + infile_name[-1]
    outfile = open(newfile_name,"w")
    outfile.write(lines)
    outfile.close()

if __name__ == "__main__":
    main(sys.argv[1])