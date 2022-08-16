def inputnumber():
    n = int(input("number is : "))
    return n


def evennumber(array, n):
    even = []
    i = 0
    while i < n:
        if array[i] % 2 == 0:
            even.append(array[i])
        i += 1
    return even


def oddnumber(array, n):
    odd = []
    i = 0
    while i < n:
        if array[i] % 2 != 0:
            odd.append(array[i])
        i += 1
    return odd


def zeronumber(array, n):
    zero = []
    i = 0
    while i < n:
        if array[i] <= 0:
            zero.append(array[i])
        i += 1
    return zero


def printnumber(array):
    i = 0
    while i < len(array):
        print("%d" % array[i])
        i += 1


array = []
i = 0
n = int(input("Size of array "))
while i < n:
    array.append(inputnumber())
    i += 1
even = evennumber(array, n)
odd = oddnumber(array, n)
zero = zeronumber(array, n)
print(" Even number ")
printnumber(even)
print(" Odd number ")
printnumber(odd)
print(" Equal or less than zero number ")
printnumber(zero)
