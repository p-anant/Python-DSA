# Problem Statement
# You have been given an integer array/list (ARR) of size N. You have to return an array/list PRODUCT such that PRODUCT[i] 
# is equal to the product of all the elements of ARR except ARR[i]
#  Note : Each product can cross the integer limits, so we should take modulo of the operation. 
# Take MOD = 10^9 + 7 to always stay in the limits.

from sys import stdin

def getProductArrayExceptSelf(arr, n) :
    p = 1
    out = []
    for i in range(n):
        out.append(p)
        p = p*arr[i]
    for i in range(n-1,-1,-1):
        out[i] = out[i] * p
        p = p*arr[i]
        
    return out  


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)
    
    t -= 1
