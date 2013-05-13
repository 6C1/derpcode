#!/usr/bin/python

import sys
from string import ascii_lowercase, ascii_uppercase

version = "0.1.0"

def bflip(n):
    return (1-n)

def fopen():
    if len(sys.argv) < 2:
        return False
    elif sys.argv[1].partition('.')[2] == "derp":
        f = open(sys.argv[1],'r')
        f.seek(0,0)
        tape = f.read()
        f.close()
        return str(tape)
    return False

class Tape():
    def __init__(self):
        self.printbuf=""
        self.cells = [0 for x in xrange(256)]
        self.pointer = 0
    def __repr__(self):
        return "\nPointer:    \t"+str(self.pointer)+"\nTape:    \t"+str(self.cells[1:])
    def get_pointer(self): return self.pointer + 1

    # derpcode commands
    def flip(self): self.cells[self.get_pointer()] = bflip(self.cells[self.get_pointer()]) 
    def inc(self): self.pointer += 1
    def dec(self): self.pointer -= 1
    def prt(self):
        if self.get_pointer < 0:
            return False
        binstr = ""
        for i in xrange(8):
            binstr+=(str(self.cells[self.get_pointer()+i]))
        self.printbuf+=str(chr(int(binstr,2)))
        return True
def main():
    interpret()

def interpret():
    library = ["herp","derp","a-derp",".","?"]
    data = fopen()
    if (data==False):
        print("\nUsage: python derpcode.py [file.derp]\nMake sure your .derp file is properly formatted.")
        system.exit()
    else:
        cmds = filter((lambda x : (x in library) or (x[0:-1] in library)), data.split())
        tape = Tape()
        for cmd in cmds:
            if cmd == library[0]:
                tape.flip()
            elif cmd == library[1]:
                tape.inc()
            elif cmd == library[2]:
                tape.dec()
            elif cmd == library[3]:
                tape.prt()
            elif cmd == library[2]+library[3]:
                tape.dec()
                if (tape.cells[1]==0 and not tape.prt()):
                    break
            elif cmd == library[2]+library[3]+library[3]:
                tape.dec()
                tape.prt()
                tape.prt()
        print(tape.printbuf)
if __name__=="__main__": main()
