account = {
    'ac_id': '',
    'ac_type': 0,
    'ac_deposit': 0,
    'ac_credit_limit': 0,
}
customer = {
    'cus_id': '',
    'cus_name': '',
    'cus_sername': '',
    'account': account,
}
print("\t\t\t\t\t\tInsert information of customer ")
customer['cus_id'] = input("\t\t\t\t\t\tEnter customer ID :")
customer['cus_name'] = input("\t\t\t\t\t\tEnter customer name :")
customer['cus_sername'] = input("\t\t\t\t\t\tEnter customer sername :")
customer['account']['ac_id'] = input("\t\t\t\t\t\tEnter customer account ID :")
print("\t\t\t\t\t\t 1 is Savings accoun")
print("\t\t\t\t\t\t 2 is current account")
customer['account']['ac_type'] = int(
    input("\t\t\t\t\t\tPlase Select customer type account 1 or 2 :"))
customer['account']['ac_deposit'] = int(
    input("\t\t\t\t\t\tEnter deposit money :"))
if customer['account']['ac_type'] == 2:
    customer['account']['ac_credit_limit'] = int(
        input("\t\t\t\t\t\tEnter customer credit limit :"))
while(1):
    print("")
    print("\t\t\t\t\t\t[1] Deposit money")
    print("\t\t\t\t\t\t[2] Withdraw money ")
    print("\t\t\t\t\t\t[3] Show detail customer")
    print("\t\t\t\t\t\t[4] Insert new customer ")
    print("\t\t\t\t\t\t[5] Exit programe ")
    n = int(input("\t\t\t\t\t\t Please select"))
    if n == 1:
        print("")
        print("\t\t\t\t\t\t[1] Deposit money")
        a = int(input("\t\t\t\t\t\tHow much will you Deposit money?"))
        account['ac_deposit'] += a
    elif n == 2:
        print("")
        print("\t\t\t\t\t\t[2] Withdraw money ")
        b = int(input("\t\t\t\t\t\tHow much will you withdraw money?"))
        account['ac_deposit'] -= b
    elif n == 3:
        print("")
        print("\t\t\t\t\t\t[3] Show detail customer")
        print("\t\t\t\t\t\tcustomer ID : %s " % customer['cus_id'])
        print("\t\t\t\t\t\tcustomer name : %s " % customer['cus_name'])
        print("\t\t\t\t\t\tcustomer sername : %s " % customer['cus_sername'])
        print("\t\t\t\t\t\tcustomer account ID : %s " %
              customer['account']['ac_id'])
        if account['ac_type'] == 1:
            print("\t\t\t\t\t\tcustomer account type : Savings account ")
        else:
            print("\t\t\t\t\t\tcustomer account type : current account ")
        print("\t\t\t\t\t\tdeposit money : %d" %
              customer['account']['ac_deposit'])
        if account['ac_type'] == 2:
            print("\t\t\t\t\t\tcredit limit : %d" %
                  customer['account']['ac_credit_limit'])
    elif n == 4:
        print("")
        print("\t\t\t\t\t\t[4] Insert new customer ")
        customer['cus_id'] = input("\t\t\t\t\t\tEnter customer ID :")
        customer['cus_name'] = input("\t\t\t\t\t\tEnter customer name :")
        customer['cus_sername'] = input("\t\t\t\t\t\tEnter customer sername :")
        customer['account']['ac_id'] = input(
            "\t\t\t\t\t\tEnter customer account ID :")
        print("\t\t\t\t\t\t 1 is Savings accoun")
        print("\t\t\t\t\t\t 2 is current account")
        customer['account']['ac_type'] = int(
            input("\t\t\t\t\t\tPlase Select customer type account 1 or 2 :"))
        customer['account']['ac_deposit'] = int(
            input("\t\t\t\t\t\tEnter deposit money :"))
        if customer['account']['ac_type'] == 2:
            customer['account']['ac_credit_limit'] = int(
                input("\t\t\t\t\t\tEnter customer credit limit :"))
    elif n == 5:
        break
    else:
        if n < 1 or n > 5:
            print("")
            print("\t\t\t\t\t\tInvalid number!! please select new number..  ")
            print("")
