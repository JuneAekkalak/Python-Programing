def inputarray(size):
    n = size
    i = 0
    array = []
    while i < n:
        array.append(int(input("Input element of array at [%d]: " % i)))
        i += 1
    evennumber(array, n)
    oddnumber(array, n)


def evennumber(array, size):
    i = 0
    even = []
    evenposition = []
    while i < size:
        if array[i] % 2 == 0:
            n = array[i]
            even.append(n)
            evenposition.append(i)
        i += 1
    outputevennumber(even, evenposition)


def oddnumber(array, size):
    i = 0
    odd = []
    oddposition = []
    while i < size:
        if array[i] % 2 != 0:
            n = array[i]
            odd.append(n)
            oddposition.append(i)
        i += 1
    outputoddnumber(odd, oddposition)


def outputevennumber(even, position):
    j = 0
    print("<<<<<<== Evennumber ==>>>>>>")
    for i in even:
        print("even is %d" % i)
        print("Position is %d" % position[j])
        j += 1
    print("Total even is %d" % j)


def outputoddnumber(odd, position):
    j = 0
    print("<<<<<<== Oddnumber ==>>>>>>")
    for i in odd:
        print("odd is %d" % i)
        print("Position is %d" % position[j])
        j += 1
    print("Total odd is %d" % j)


def main():
    print("=======================================")
    print("* Programe find even and odd in array *")
    print("=======================================")
    n = int(input("Enter size of array ==> "))
    inputarray(n)
    a = input("Press any key to exit...")
    print(a)


if __name__ == "__main__":
    main()
