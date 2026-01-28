n = int(input("enter the value"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print('*',end="")
    for j in range(1,i):
        print(" ",end="")
        print('*',end="")
    print()