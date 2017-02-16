# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "eshan"
__date__ = "$Jan 25, 2016 11:52:47 PM$"

import Queue
import collections
import itertools

def consume(iterator, n):
    collections.deque(itertools.islice(iterator, n))
    
def check(ar, s):
    v = 0
    for a in range(len(ar)):
        if ar[a] == s:
            v = 1
            break
    
    return v         
                        
                    
                    
def index(ar, s):
    v = -1
    for a in range(len(ar)):
        if ar[a] == s:
            v = a
            break
    
    return v      
    
if __name__ == "__main__":    
    n = input()
    array = []
    val = []

    for a in range(n):
        i = raw_input()
        list = i.split(' = ')
        array.append(list[0])
        val.append(int(list[1]))
        
    m = input()
    string = []

    while len(string) < m:
        string.append(raw_input())
 
    
    for a in range(len(string)):
        com = 0
        stack = [] 
        sign = Queue.Queue()
        word = string[a].split(" ")
        iter = range(len(word)).__iter__()
        for i in iter:
            if word[i] != 'x' and word[i] != '+' and word[i] != '-' and word[i] != '/':
                if check(array, word[i]) == 1:
                    m = index(array, word[i])
                    stack.append(val[m])
                else:
                    com = 1
            elif word[i] == 'x':
                a = stack.pop()
                b = word[i + 1]
                if check(array, b) == 1:
                    m = index(array, b)
                    if m != -1:
                        stack.append(a * val[m])
                        consume(iter, 1)
                else:
                    com = 1
            elif word[i] == '/':
                a = stack.pop()
                b = word[i + 1]
                if check(array, b) == 1:
                    m = index(array, b)
                    if m != -1:
                        stack.append(a / val[m])
                        consume(iter, 1)
                else:
                    com = 1
            elif word[i] == '+' or word[i] == '-':
                sign.put(word[i]);
        b = 0
        out = []
    
        for i in range(len(stack)):
            if b == 0:
                out.append(stack[0])
                b = 1
            else:    
                a = sign.get()
                x = out.pop()
                y = stack[i]
                if a == '+':
                    out.append(x + y)
                elif a == '-':
                    out.append(x - y)
        
        if com == 0: 
            for i in range(len(out)):
                print out[i]
        else:
            print "Compilation Error"