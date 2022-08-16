import os


def openfile():
    filename = input("Filename : ")
    return filename


def create():
    filename = input("create filename : ")
    f = open(filename, 'w')
    n = int(input("Number employee is : "))
    i = 1
    while i <= n:
        id = input("Employee ID : ")
        name = input("Employee name : ")
        sername = input("Employee sername : ")
        age = int(input("Employee age : "))
        salary = int(input("Employee salary : "))
        department = input("Employee department : ")
        f.write(id + ',' + name + ',' + sername + ',' +
                str(age) + ',' + str(salary) + ',' + department + '\n')
        i = i + 1
    f.close()


def display(filename):
    f = open(filename, 'r')
    while(1):
        s = f.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        print("id = ", em[0])
        print("name = ", em[1])
        print("sername = ", em[2])
        print("age = ", em[3])
        print("salary = ", em[4])
        print("department = ", em[5])
    f.close()


def update(filename):
    print("[ 1 ] Edit employee in record ")
    print("[ 2 ] Inseart employee ")
    n = int(input("Select :"))
    if n == 1:
        print("[ 1 ] Edit employee in record ")
        fr = open(filename, 'r')
        fw = open("temp.dat", 'w')
        up_id = input("Update at ID : ")
        while(1):
            s = fr.readline()
            if s == '':
                break
            em = s.rstrip().split(',')
            id = em[0]
            name = em[1]
            sername = em[2]
            age = em[3]
            salary = em[4]
            department = em[5]
            if up_id == id:
                id = input("Employee ID : ")
                name = input("Employee name : ")
                sername = input("Employee sername : ")
                age = int(input("Employee age : "))
                salary = int(input("Employee salary : "))
                department = input("Employee department : ")
            fw.write(id + ',' + name + ',' + sername + ',' +
                     str(age) + ',' + str(salary) + ',' + department + '\n')
        fr.close()
        fw.close()
        fr1 = open('temp.dat', 'r')
        fw1 = open(filename, 'w')
        while(1):
            s = fr1.readline()
            if s == '':
                break
            em = s.rstrip().split(',')
            id = em[0]
            name = em[1]
            sername = em[2]
            age = em[3]
            salary = em[4]
            department = em[5]
            fw1.write(id + ',' + name + ',' + sername + ',' +
                      str(age) + ',' + str(salary) + ',' + department + '\n')
        fr1.close()
        fw1.close()
        os.remove("temp.dat")
    if n == 2:
        print("[ 2 ] Inseart employee ")
        f = open(filename, 'a')
        n = int(input("Number employee is : "))
        i = 1
        while i <= n:
            id = input("Employee ID : ")
            name = input("Employee name : ")
            sername = input("Employee sername : ")
            age = int(input("Employee age : "))
            salary = int(input("Employee salary : "))
            department = input("Employee department : ")
            f.write(id + ',' + name + ',' + sername + ',' +
                    str(age) + ',' + str(salary) + ',' + department + '\n')
            i = i + 1
        f.close()


def delete(filename):
    d_id = input("Delete at ID : ")
    f = open(filename, 'r')
    f1 = open('temp.dat', 'w')
    while(1):
        s = f.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        id = em[0]
        name = em[1]
        sername = em[2]
        age = em[3]
        salary = em[4]
        department = em[5]
        if id != d_id:
            f1.write(id + ',' + name + ',' + sername + ',' +
                     str(age) + ',' + str(salary) + ',' + department + '\n')
    f.close()
    f1.close()

    f2 = open('temp.dat', 'r')
    f3 = open(filename, 'w')
    while(1):
        s = f2.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        id = em[0]
        name = em[1]
        sername = em[2]
        age = em[3]
        salary = em[4]
        department = em[5]
        f3.write(id + ',' + name + ',' + sername + ',' +
                 str(age) + ',' + str(salary) + ',' + department + '\n')
    f2.close()
    f3.close()
    os.remove("temp.dat")


def search(filename):
    s_id = input("Search at ID : ")
    f = open(filename, 'r')
    while(1):
        s = f.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        if s_id == em[0]:
            print("id = %s" % em[0])
            print("name = %s " % em[1])
            print("sername = %s " % em[2])
            print("age = %s" % em[3])
            print("salary = %s" % em[4])
            print("department = %s" % em[5])
            break
    f.close()


def main():
    while (1):
        print("[ 1 ]  create employee file")
        print("[ 2 ]  display employee file")
        print("[ 3 ]  update employee file")
        print("[ 4 ]  delete employee")
        print("[ 5 ]  search employee")
        print("[ 6 ]  stop program")
        n = int(input("Plese select : "))
        if n == 1:
            create()
        if n == 2:
            filename = openfile()
            display(filename)
        if n == 3:
            filename = openfile()
            update(filename)
        if n == 4:
            filename = openfile()
            delete(filename)
        if n == 5:
            filename = openfile()
            search(filename)
        if n == 6 or n > 6 or n < 1:
            break


if __name__ == "__main__":
    main()
