A = []
B = []
sum = []
negative = []
r = int(input("Enter the number of rows "))
c = int(input("Enter the number of columns "))
while r < 1 or c < 1 :
    r = int(input("Enter the number of New rows "))
    c = int(input("Enter the number of New columns "))
# รับตัวเลขมาเก็บ ใน Metrix A start
print("Enter elements of 1st matrix:")
for i in range(r):
    a = []
    for j in range(c):
        n = int(input("Enter element A [%d][%d]" % (i, j)))
        a.append(n)
    A.append(a)
# รับตัวเลขมาเก็บ ใน Metrix A end
# รับตัวเลขมาเก็บ ใน Metrix B start
print("Enter elements of 2st matrix:")
for i in range(r):
    b = []
    for j in range(c):
        n = int(input("Enter element B [%d][%d]" % (i, j)))
        b.append(n)
    B.append(b)
# รับตัวเลขมาเก็บ ใน Metrix B end
# แสดงค่าตัวเลขที่เก็บ ใน Metrix A start
print("elements of 1st matrix:")
for i in A:
    for j in i:
        print(j, end=" ")
    print()
# แสดงค่าตัวเลขที่เก็บ ใน Metrix A end
# แสดงค่าตัวเลขที่เก็บ ใน Metrix B start
print("elements of 2st matrix:")
for i in B:
    for j in i:
        print(j, end=" ")
    print()
# แสดงค่าตัวเลขที่เก็บ ใน Metrix B end
# บวกค่าตัวเลขที่เก็บ ใน Metrix A กับ B start
for i in range(r):
    s = []
    for j in range(c):
        s.append(A[i][j] + B[i][j])
    sum.append(s)
# บวกค่าตัวเลขที่เก็บ ใน Metrix A กับ B end
# ลบค่าตัวเลขที่เก็บ ใน Metrix A กับ B start
for i in range(r):
    d = []
    for j in range(c):
        d.append(A[i][j] - B[i][j])
    negative .append(d)
# ลบค่าตัวเลขที่เก็บ ใน Metrix A กับ B end
# แสดงค่าตัวเลขที่บวกเสร็จ ใน Metrix sum start
print("sum result elements of 1st and 2st matrix:")
for i in sum:
    for j in i:
        print(j, end=" ")
    print()
# แสดงค่าตัวเลขที่บวกเสร็จ ใน Metrix sum end
# แสดงค่าตัวเลขที่ลบเสร็จ ใน Metrix negative start
print("negative result elements of 1st and 2st matrix:")
for i in negative:
    for j in i:
        print(j, end=" ")
    print()
# แสดงค่าตัวเลขที่ลบเสร็จ ใน Metrix negative end
c  = input("press any key to exit..")