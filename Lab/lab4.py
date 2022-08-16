n = int(input("input number"))
if n > 0:
    print("Positive number")
    for i in range(1, n+1):
        print("n = %d" % i)
elif n <= -1:
    print("Negative number")
    i = -1
    while i >= n:
        print("n = %d" % i)
        i = i - 1
else:
    print("It is zero number")
c = input("press any key to exit..")
