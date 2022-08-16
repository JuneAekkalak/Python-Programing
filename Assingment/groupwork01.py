d = int(input("day is "))
m = int(input("month is "))
y = int(input("year is "))
while d <= 0 or d > 31 or m <= 0 or m > 12 or y == 0:
    d = int(input("day is "))
    m = int(input("month is "))
    y = int(input("year is "))
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    dim = 31
elif m == 2:
    if y % 4 == 0:
        dim = 29
    else:
        dim = 28
else:
    dim = 30

if d < dim:
    d = d + 1
elif d == dim and m != 12:
    d = 1
    m = m + 1
elif d == dim and m == 12:
    d = 1
    m = 1
    y = y + 1
else:
    print("invalid day ")
print("Tomorrow is %d / %d / %d " % (d, m, y))
c = input("press any key to exit..")
