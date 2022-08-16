class node:
    def __init__(self,number,expo):
        self.number = number
        self.expo = expo
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, number , expo):
        newnode = node(number,expo)
        newnode.next = first.head
        first.head = newnode

    def printdata(self):
        num = self.head
        while num != None:
            print("%.1f|%d" % (num.number, num.expo))
            num = num.next


first = linkedlist()
while(1):
    number = float(input("Enter value coefficient :"))
    expo = int(input("Enter value Exponent :"))
    first.insert(number,expo)
    if expo == 0:
        break

first.printdata()

a = input("press any key to exit .. ")
print(a)