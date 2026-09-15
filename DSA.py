# ALL CREATED DSAs WILL BE PUT HERE, INCLUDING CLASSES FOR NODES
# THEN JUST IMPORTING TO MAIN TO DISPLAY OUT
from DSA_InputSpecs import *
global dsa_id
dsa_id = None

class stack:
    def __init__(self):
        self.stack = []
        set_id("Stacks")

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            return "Empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)
        

    def isEmpty(self):
        return len(self.stack) == 0



def set_id(str):
    global dsa_id
    dsa_id = str
    
def get_id():
    return dsa_id