n = int(input("Input number 1-99 : "))
while n < 1 or n > 99:
    n = int(input("Input number 1-99 : "))
front = n / 10
back = n % 10
if front == 7 or back == 7:
    print("Buzz")
elif n % 7 == 0:
    print("Buzz Buzz")
else:
    print(n)
a = int(input())
