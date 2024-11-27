#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length ==1:
        print([0])
    else:
        fib = [0,1]
        
        for i in range(2, length):
            next_number = fib[i-1] + fib[i-2]
            fib.append(next_number)
            
        print (fib)
print_fibonacci(8)
