#!/usr/bin/python

import sys

version = "0.1.0"

def fopen():
    if len(sys.argv) < 2:
        return False
    elif sys.argv[1].partition('.')[2] == "derp":
        print ".\n.\n."
        f = open(sys.argv[1],'r')
        print "Loaded", f.name
        print "File verified. Reading..."
        f.seek(0,0)
        tape = f.read()
        f.close()
        return tape



    return False

def main():
    library = ["herp","derp","a-derp","."]

    print "Derpcode Interpreter", version
    data = fopen()
    if (not data):
        print "\nUsage: python derpcode.py [file.derp]\nMake sure your .derp file is properly formatted."
    else:
        data = data.split()
        for word in data:
            if word in library or (word+".") in library:
                print word
            else:
                data.remove(word)

if __name__=="__main__": main()
