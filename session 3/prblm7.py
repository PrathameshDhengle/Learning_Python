n =int(input("enter the decimal number"))
binary =" "
while n>=1:
    reminder=n%2
    binary = binary + str(reminder)
    n= n//2
print("without format",binary)
print("actual binarry after down to up",binary[::-1])# for binary number reminder are arrange in down to upper direction
