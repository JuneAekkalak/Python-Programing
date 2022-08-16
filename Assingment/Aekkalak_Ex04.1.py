print(" !! Caution must be positive integers only.!! ")
x = int(input(" x = "))
y = int(input(" y = "))
while x < 1 or y < 1:
    print(" ** must be positive integers only. **")
    x = int(input(" x = "))
    y = int(input(" y = "))
a = x
b = y
while y != 0:
    z = y
    y = x % y
    x = z
print("Greatest Commond Division of %d and %d is %d" % (a, b, x))
c = input("pres any key to exit..")
