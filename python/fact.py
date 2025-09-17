num = int(input("Enter a number :"))


def fact(a):
    if a == 0:
        return 1
    else:
        return ((a) * fact(a -1))
    

result = fact(num)
print("Factorial is:" , result)