
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