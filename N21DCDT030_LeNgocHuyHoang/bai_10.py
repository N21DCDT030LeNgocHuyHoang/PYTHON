def decTobin(n):
    if n==0:
        return 0
    else:
        return n%2 + 10 * decTobin(n//2)
def printdecTobin(n):
    if n==0:
        print(0)
    else: 
        bin=decTobin(n)
        print(bin)
printdecTobin(20)
        