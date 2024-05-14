try:
    ans=10/0
    num=int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)