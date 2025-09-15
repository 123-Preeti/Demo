x = int(input("Enter number  :"))

if x == 1 :
    print(x, "is not a prime number")
if x > 1:
    for i in range (2, x):
        if x % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is prime number")

