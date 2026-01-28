x = int(input("enter the value of 'x' "))
n = int(input("enter the value of 'n' "))
sum= 1
for i in range(2,n):
    upper=x**i/i
    sum=sum+upper
print("series sum is",sum)
