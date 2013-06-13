#!/usr/bin/python

import sys, math
from string import ascii_lowercase, ascii_uppercase

version = "0.1.0"
INIT_LEN = int(256)

def bflip(n): return (1-n)

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
        self.cells = [0 for x in xrange(INIT_LEN)]
        self.pointer = 0
    def __repr__(self):
        return "\nPointer:    \t"+str(self.pointer)+"\nTape:    \t"+str(self.cells[1:])
    def get_pointer(self): return self.pointer + 1

    def update(self):
        if len(self.cells) - self.pointer < (math.ceil(len(self.cells)**0.25)):
            for i in xrange(len(self.cells)):
                self.cells.append(0)
        for cell in self.cells:
            if cell > 1:
                print cell

    # derpcode commands
    def flip(self): self.cells[self.get_pointer()] = bflip(self.cells[self.get_pointer()]) 
    def inc(self): self.pointer += 1
    def dec(self): self.pointer -= 1
    def prt(self):
        if self.get_pointer < 0:
            return False
        binstr = ""
        for i in xrange(8):
            binstr+=(str(self.cells[self.get_pointer()+7-i]))
        self.printbuf+=str(chr(int(binstr,2)))
        return True
    def gtc(self):
        char = str(ord(sys.stdin.read(1)[0:1]))
        char = bin(int(char))[2:].zfill(8)
        print
        for i in xrange(len(char)):
            self.cells[self.pointer + i] = int(char[i])
    def brh(self):
        if self.cells[self.pointer] == 1:
            string = ""
            for i in xrange(8):
                string += str(self.cells[self.pointer+i])
            num = int(string,2)
            print num

def interpret(data):
    library = ["herp","derp","a-derp",".","?"]
    cmds = filter((lambda x : (x in library) or (x[0:-1] in library)), data.split())
    tape = Tape()
    for cmd in cmds:

#        uncomment this for detailed stats    
#        print cmd, "   \tPointer:",  tape.pointer, "\tBit:",  tape.cells[tape.pointer], "\tlen(tape):", len(tape.cells)

        if cmd == library[0]: tape.flip()
        elif cmd == library[1]: tape.inc()
        elif cmd == library[2]: tape.dec()
        elif cmd == library[3]: tape.prt()
        elif cmd == library[2]+library[3]:
            tape.dec()
            if (tape.cells[1]==0 and not tape.prt()): break
        elif cmd == library[2]+library[3]+library[3]:
            for i in xrange(3): tape.dec()
        elif cmd == library[4]: tape.gtc()
        tape.update()
    print(tape.printbuf)


def fherp(tape):
    tape.flip()

def derp(tape):
    tape.inc()

#
# MAIN FUNCTION
#

def main():
    data = fopen()
    # File verification
    if (data==False):
        print("\nUsage: python derpcode.py [file.derp]\nMake sure your .derp file is properly formatted.")
        sys.exit()
    else:
        interpret(data)

if __name__=="__main__": main()
