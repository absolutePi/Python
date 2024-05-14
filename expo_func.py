def raise_to_power(num,power):
    res=1
    for i in range(power):
        res*=num
    return res
num=int(input("Enter a number: "))
power=int(input("Enter the power: "))
print(raise_to_power(num,power))