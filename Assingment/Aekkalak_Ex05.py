Rf = []
count = 12
#count = int(input("input number Rainfall ="))
i = 0
sum = 0
avg = 0
while i < count:
    n = float(input("Input Rainfall[%d] = " % i))
    while n < 0:
        print("** Warning Invalid Rainfall **")
        n = float(input("Input new Rainfall[%d] = " % i))
    sum = sum + n
    Rf.append(n)
    i = i+1
max = Rf[0]
min = Rf[0]
for a in Rf:
    if a >= max:
        max = a
    if a <= min:
        min = a
avg = sum / count
print("max = %.2f " % max)
print("min = %.2f " % min)
print("sum = %.2f " % sum)
print("avg = %.2f " % avg)
click = input("Press any key to exit...")
