##account = {'ac_id': [], 'ac_type': [], 'ac_deposit': [], 'ac_limit': [], }
customer = {
    'p_id': [],
    'p_name': [],
    'p_sername': [],
    'account': {'ac_id': [], 'ac_type': [], 'ac_deposit': [], 'ac_limit': [], },
}
n = int(input("n = "))
i = 0 
while n != 0 :
    print("\t\t\t\t\t\tInsert information of customer ")
    customer['p_id'].append(int(input("\t\t\t\t\t\tEnter customer ID :")))
    customer['p_name'].append(input("\t\t\t\t\t\tEnter customer name :"))
    customer['p_sername'].append(input("\t\t\t\t\t\tEnter customer sername :"))
    customer['account']['ac_id'].append(int(
        input("\t\t\t\t\t\tEnter customer account ID :")))
    print("\t\t\t\t\t\t 1 is Savings accoun")
    print("\t\t\t\t\t\t 2 is current account")
    customer['account']['ac_type'].append(int(
        input("\t\t\t\t\t\tPlase Select customer type account 1 or 2 :")))
    customer['account']['ac_deposit'].append(int(
        input("\t\t\t\t\t\tEnter deposit money :")))
    if customer['account']['ac_type'][i] == 2:
        customer['account']['ac_limit'].append(int(
            input("\t\t\t\t\t\tEnter customer credit limit :")))
    i=i+1
    n = int(input("n = "))
print(customer)
