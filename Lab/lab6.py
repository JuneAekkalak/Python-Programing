ar = []
sumN = []
n = int(input("Input number of size array : "))
while n < 1 :
    n = int(input("Input number of size array : "))
i = 0
while i < n :
    a = int(input("Input number :"))
    while a < 1:
        a = int(input("Input number :"))
    ar.append(a)
    i = i + 1 
sum = 0
for i in ar :
    if i % 2 == 0 :
        sum = sum + 1
        sumN.append(i)
print(ar)
print("Number of Positive integer" )
print(sumN)
print("Sum Positive integers = %d"%sum)
