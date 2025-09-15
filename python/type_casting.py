s ="250"
num = int(s)
print(num + 50)

#boolean to int
print(int(True))
print(int(False))

# string list to int
str_lst = ["20", "30","40"]
int_lst = [int(x) for x in str_lst]
print(int_lst)

#handling invalid conversion
s = "hello"
try:
    num = int(s)
    print(num)
except ValueError:
    print("cannot convert")