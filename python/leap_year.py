year = int(input("Enter year"))
if year < 1000 or year > 9999:
    print("Give valid year")
elif (year % 400 == 0) and (year % 100==0):
    print(year, " is leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(year, "is leap year")
else:
    print("not a leap year")

# square root

num = 64 
num1 = int(input("Enter a number here"))
sqrt = num1 ** (1/2)
print("Square root is: ", sqrt)