brand = []
model = []
color = []
cost = []
cardata = {
    'brand': brand,
    'model': model,
    'color': color,
    'cost': cost,
}
n = int(input("\t\t\t   Enter number of car is : "))
print("")
i = 1
while i <= n:
    print("            \t\t\tINSERT CARDATA |%d| \n" % i)
    brand.append(input("\t\t\tEnter brand name of car is : "))
    model.append(input("\t\t\tEnter model name of car is : "))
    color.append(input("\t\t\tEnter color of car is : "))
    cost.append(int(input("\t\t\tEnter cost of car is : ")))
    print("")
    i += 1
print(cardata)
j = 1
i = 0
print("")
while i < n:
    print("             \t\t\tCARDATA |%d| \n" % j)
    print("\t\t\tBrand name is %s" % cardata['brand'][i])
    print("\t\t\tModel name is %s" % cardata['model'][i])
    print("\t\t\tColor of car is %s" % cardata['color'][i])
    print("\t\t\tCost of car is $ %d \n" % cardata['cost'][i])
    i += 1
    j += 1
c = input("\t\t\tPrass any key to exit..")
print(c)
