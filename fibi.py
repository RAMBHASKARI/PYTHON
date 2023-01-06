# Fibonacci numbers module

def fibo(num):    # write Fibonacci series up to n
    a = 0
    b = 1
    fib = 0
    for i in range (num):
        print (fib,end=' ')
        a=b 
        b=fib 
        fib=a+b
