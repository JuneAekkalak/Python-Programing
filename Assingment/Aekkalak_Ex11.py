employee = {
    'id': '',
    'name': '',
    'sername': '',
    'age': 0,
    'salary': 0.0,
    'department': '',
}


def inputfilename():
    filename = input("File name for read : ")
    filename2 = input("File name for write : ")
    return filename, filename2


def editfile(name1, name2):
    f1 = open(name1, 'r')
    f2 = open(name2, 'w')
    i = 0
    while(1):
        s = f1.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        employee['id'] = em[0]
        employee['name'] = em[1]
        employee['sername'] = em[2]
        employee['age'] = int(em[3])
        employee['salary'] = float(em[4])
        employee['department'] = em[5]
        employee['salary'] = employee['salary'] + (employee['salary'] * 0.05)
        f2.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                 + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
        i = i + 1
    f1.close
    f2.close


def printfile(name):
    f = open(name, 'r')
    i = 0
    while(1):
        s = f.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        employee['id'] = em[0]
        employee['name'] = em[1]
        employee['sername'] = em[2]
        employee['age'] = int(em[3])
        employee['salary'] = float(em[4])
        employee['department'] = em[5]
        print("Employee No.[%d]" % i)
        print("Employee ID : %s" % employee['id'])
        print("Employee Name : %s" % employee['name'])
        print("Employee Sername : %s" % employee['sername'])
        print("Employee Age : %d" % employee['age'])
        print("Employee Salary : %.2f" % employee['salary'])
        print("Employee Department : %s" % employee['department'])
        print("\n")
        i = i + 1
    f.close


def main():
    f1, f2 = inputfilename()
    editfile(f1, f2)
    print("INFOMATION OF EMPLOYEE FROM [%s]" % f1)
    printfile(f1)
    print("INFOMATION OF EMPLOYEE FROM [%s]" % f2)
    printfile(f2)
    a = input("Press any key to exit..")
    print(a)


if __name__ == "__main__":
    main()
