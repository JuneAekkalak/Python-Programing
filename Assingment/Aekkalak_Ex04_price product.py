num = int(input("input num product is : "))
while num <= 0:
    num = int(input("input number product is : "))
i = 0
sumprice = 0
change = 0
while i < num:
    price = int(input("Input product price : "))
    sumprice = sumprice + price
    i += 1
print("sumprice is ", sumprice)
money = int(input("input your money is : "))
while money < sumprice:
    print("your money less than price of product")
    money = int(input("input your money is : "))
if (money >= sumprice):
    change = money - sumprice
print("your change is ", change)
c = input("pres any key to exit..")
