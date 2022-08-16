employee = {
    'id': '',
    'name': '',
    'sername': '',
    'age': 0,
    'salary': 0.0,
    'department': '',
}


def create_employee_file():
    filename = input("Filename : ")
    f = open(filename, 'w')
    n = int(input("Number of employee is : "))
    i = 0
    while i < n:
        employee['id'] = input("Employee ID : ")
        employee['name'] = input("Employee Name : ")
        employee['sername'] = input("Employee Sername : ")
        employee['age'] = int(input("Employee Age : "))
        employee['salary'] = int(input("Employee Salary : "))
        employee['department'] = input("Employee Department : ")
        f.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
        print("\n")
        i = i + 1
    print('Writing to file completed')
    f.close


def display_employee_file(filename):
    f = open(filename, 'r')
    i = 1
    while (1):
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
    print("====== Read to file completed  =======")
    f.close


def update_employee(filename):
    print("[1] Add new employee information ")
    print("[2] Edit employee information ")
    n = int(input("Plaes select : "))
    if n == 1:
        f = open(filename, 'a')
        n = int(input("Number of employee is : "))
        i = 0
        while i < n:
            employee['id'] = input("Employee ID : ")
            employee['name'] = input("Employee Name : ")
            employee['sername'] = input("Employee Sername : ")
            employee['age'] = int(input("Employee Age : "))
            employee['salary'] = int(input("Employee Salary : "))
            employee['department'] = input("Employee Department : ")
            f.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                    + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
            print("\n")
            i = i + 1
        f.close
    '''if n == 2 :
        update_at_id = input("What are you want update Employee ID ? :")
        f1 = open(filename, 'r')
        f2 = open(filename, '')
        while (1):
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
            if update_at_id == employee['id'] :
                employee['id'] = input("Employee ID : ")
                employee['name'] = input("Employee Name : ")
                employee['sername'] = input("Employee Sername : ")
                employee['age'] = int(input("Employee Age : "))
                employee['salary'] = int(input("Employee Salary : "))
                employee['department'] = input("Employee Department : ")
                f2.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                    + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
        f1.close()
        f2.close()'''


def delete_employee(filename):
    del_id = input("What id do you want to delete?")
    f = open(filename, 'r')
    f1 = open('delete', 'w')
    while (1):
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
        if employee['id'] != del_id:
            f1.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                     + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
        else:
            print("error")
    f.close()
    f1.close()

    f2 = open('delete', 'r')
    f3 = open(filename, 'w')
    while (1):
        s = f2.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        employee['id'] = em[0]
        employee['name'] = em[1]
        employee['sername'] = em[2]
        employee['age'] = int(em[3])
        employee['salary'] = float(em[4])
        employee['department'] = em[5]
        if employee['id'] != del_id:
            f3.write(employee['id'] + ' , ' + employee['name'] + ' , ' + employee['sername'] + ' , ' + str(employee['age'])
                     + ' , ' + str(employee['salary']) + ' , ' + employee['department'] + '\n')
    f2.close()
    f3.close()


def search_employee(filename):
    f = open(filename, 'r')
    search = str(input("What id : "))
    while (1):
        s = f.readline()
        if s == '':
            break
        em = s.rstrip().split(',')
        if search == em[0]:
            employee['id'] = em[0]
            employee['name'] = em[1]
            employee['sername'] = em[2]
            employee['age'] = int(em[3])
            employee['salary'] = float(em[4])
            employee['department'] = em[5]
            print("Employee ID : %s" % employee['id'])
            print("Employee Name : %s" % employee['name'])
            print("Employee Sername : %s" % employee['sername'])
            print("Employee Age : %d" % employee['age'])
            print("Employee Salary : %.2f" % employee['salary'])
            print("Employee Department : %s" % employee['department'])
            print("\n")
            break
    f.close


def main():
    while (1):
        print("[ 0 ]  Open file ")
        print("[ 1 ]  create employee file")
        print("[ 2 ]  display employee file")
        print("[ 3 ]  update employee file")
        print("[ 4 ]  delete employee")
        print("[ 5 ]  search employee")
        print("[ 6 ]  stop program")
        n = int(input("Plese select : "))
        if n == 0:
            filename = input("Filename : ")
        if n == 1:
            create_employee_file()
        if n == 2:
            display_employee_file(filename)
        if n == 3:
            update_employee(filename)
        if n == 4:
            delete_employee(filename)
        if n == 5:
            search_employee(filename)
        if n == 6 or n > 6 or n < 0:
            break


if __name__ == "__main__":
    main()
