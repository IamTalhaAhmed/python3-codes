#This program gets an integer and returns the value of a fibonacci series at that position
import sys
def fibonacci(n):
    first = 0
    second = 1
    num = n
    if (num == 1):
        val = int(first)
    elif (num == 2):
        val = int(second)
    else:
        for i in range(num-2):
            val= first + second
            first =  second
            second = val
    return val

if __name__ == '__main__':
    n=int(sys.argv[1])
    val=fibonacci(n)
    print("The value at position {0} of fibonacci series is {1}".format(n,val))