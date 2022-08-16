employee = {
    'id': '',
    'name': '',
    'sername': '',
    'age': 0,
    'salary': 0.0,
    'department': '',
}


def file_name():
    filename = input("Input filename and location : ")
    return filename


def write_employee(filename):
    f = open(filename, 'w')
    print("====== WriteFile Start =======")
    i = 1
    while(1):
        print("Employee No.[%d]" % i)
        employee['id'] = input("Employee ID ( 0 = quit ) : ")
        if employee['id'] == '0':
            break
        employee['name'] = input("Employee Name : ")
        employee['sername'] = input("Employee Sername : ")
        employee['age'] = int(input("Employee Age : "))
        employee['salary'] = int(input("Employee Salary : "))
        employee['department'] = input("Employee Department : ")
        f.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
        print("\n")
        i += 1
    print("====== WriteFile End =======")
    print('Writing to file completed')
    f.close


def read_employee(filename):
    f = open(filename, 'r')
    print("====== ReadFile Start =======")
    i = 1
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
        i += 1
    print("====== ReadFile End =======")
    f.close


def main():
    filename = file_name()
    write_employee(filename)
    print("\n")
    read_employee(filename)
    a = input("Press any key to exit..")
    print(a)


if __name__ == "__main__":
    main()
