num_1 = int(input("enter the first number"))
num_2 = int(input("enter the second number"))

if num_1>num_2:
    min=num_2
else:
    min=num_1
for i in range(1,min+1):
    if num_1%i==0 and num_2%i==0:
        hcf=i
        mul=num_1*num_2
        lcm=mul/hcf
print(f'the HCF IS :-{hcf} and the LCM is :-{lcm}')
