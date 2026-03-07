# Bank Management System 💰

# Create Account
# Deposit
# Withdraw
# Check Balance
# Delete Account


# REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO CREATE ACCOUNT--
def createAccount():
    file = open('account.bin', 'ab')

    acc_no = input("\nEnter Account Number: ")
    name = input("Enter Name: ")
    mobile = input("Enter Mobile: ")

    account = {
        "acc_no": acc_no,
        "name": name,
        "mobile":  mobile,
        "balance": 0.0
    }

    pickle.dump(account, file)
    file.close()

    print("\n\tAccount Created Successfully")
    input("\tPRESS ENTER TO CONTINUE...")

# VIEW ALL ACCOUNTS--
def viewAllAccount():
    file = open('account.bin', 'rb')
    try:
        print(f"{'ACC_NO':<10} {'NAME':<15} {'MOBILE':<15} {'BALANCE':<10}")
        while True:
            data = pickle.load(file)
            print(f"{data["acc_no"]:<10} {data["name"]:<15} {data["mobile"]:<15} {data["balance"]:<10}")
            
    except EOFError:
        pass

    file.close()
    print("\n\tHERE IS YOUR ALL ACCOUNTS")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO DEPOSIT AMMOUNT--
def deposit():
    acc_no = input("Enter account Number: ")
    amount = float(input("Enter deposit ammount: "))

    if amount <= 0:
        print("INVALID AMOUNT")
        return
    
    file1 = open('account.bin', 'rb')
    file2 = open('temp.bin', 'ab')
    found = False

    try:
        while True:
            data = pickle.load(file1)
            if data['acc_no'] == acc_no:
                data['balance'] += amount
                found = True

            pickle.dump(data, file2)

    except:
        pass

    file1.close()
    file2.close()

    os.remove('account.bin')
    os.rename('temp.bin', 'account.bin')

    if found:
        print("\n\tAMOUNT DEPOSITED SUCCESSESFULLY 💰")
    else:
        print("\n\tAccount not found ❌")

    input("\tPRESS ENTER TO CONTINUE...")

#  A METHOD TO WITHDRAW AMMOUNT--
def withdraw():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter withdraw amount: "))

    if amount <= 0:
        print("INVALID AMOUNT")
        return

    file1 = open('account.bin', 'rb')
    file2 = open('temp.bin', 'wb')
    found= False
    insufficient = False

    try:
        while True:
            data = pickle.load(file1)

            if data['acc_no'] == acc_no:
                found = True

                if data['balance'] < amount:
                    print("Insufficient amount")
                    insufficient = True

                else:
                    data['balance'] -= amount
                    print("\tWithdraw Successfully")
            
            pickle.dump(data, file2)
    
    except:
        pass

    file1.close()
    file2.close()    

    if found:
        os.remove('account.bin')   
        os.rename('temp.bin', 'account.bin')
    else:
        os.remove('temp.bin')
        print("\tACCOUNT NOT FOUND")

# A METHOD TO CHECK BALANCE--
def checkBalance():
    acc_no = input("Enter account number: ")

    file = open('account.bin', 'rb')

    found = False

    while True:
        data = pickle.load(file)

        if data['acc_no'] == acc_no:
            print(f"Avalaible Balance: {data['balance']}")
            found = True
            break

    if not found:
        print("Account NOT found")
    
    file.close()

    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO DELETE ACCOUNT--
def DeleteAccount():
    acc_no = input("Enter account number: ")

    file1 = open('account.bin', 'rb')
    file2 = open('temp.bin', 'wb' )

    found = False

    try:
        while True:
            data = pickle.load(file1)

            if data['acc_no'] == acc_no:
                pickle.load(file1)
                found = True
            else:
                pickle.dump(data, file2)
    except:
        pass

    file1.close()
    file2.close()

    os.remove('account.bin')
    os.rename('temp.bin', 'account.bin')

    if found:
        print("\tAccount Deleted successesfully")
    else:
        print("\tAccount NOT Found")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO VIEW ACCOUNT DETAILS 
def viewAccount():
    acc_no = input("Enter account number: ")

    file = open('account.bin', 'rb')
    found = False
    
    try:
        while True:
            data = pickle.load(file)
            if data['acc_no'] == acc_no:
                print("\n-----ACCOUNT DETAILS-----")
                print("Account no:", data['acc_no'])
                print("Name:", data['name'])
                print("Balance:", data['balance'])
                found = True
                break
                
    except:
        pass
    file.close()

    if not found:
        print("Account not Found")
    input("\tPRESS ENTER TO CONTINUE...")

# A METHOD TO TRANSFER MONEY
def transferMoney():
    sdr_acc = input("Enter your account number: ")
    rcvr_acc = input("Enter receiver account number: ")
    amount = float(input("Enter amount to transfer: "))

    if sdr_acc == rcvr_acc:
        print("Cannot Transfer to same account")
        return

    file1 = open('account.bin', 'rb')
    file2 = open('temp.bin', 'wb')

    sender_found = False
    receiver_found = False
    sufficient_balance = True

    try:
        while True:
            data = pickle.load(file1)
            if data['acc_no'] == sdr_acc:
                sender_found = True

                if data['balance'] < amount:
                    print("\tInsuffiecient Amount")
                    sufficient_balance = False
                    break
                else:
                    data['balance'] -= amount

            elif data['acc_no'] == rcvr_acc:
                receiver_found = True
                data['balance'] += amount

            pickle.dump(data, file2)

    except EOFError:
        pass

    file1.close()
    file2.close()

    if not sender_found:
        print("\n\tSender account NOT found")
        os.remove('temp.bin')
        return
    
    if not receiver_found:
        print("\n\tReceiver account NOT found")
        os.remove('temp.bin')
        return
    
    if not sufficient_balance:
        os.remove('temp.bin')
        return
    
    os.remove('account.bin')
    os.rename('temp.bin', 'account.bin')

    print("\tMoney transferred successfully 💰")

    input("\tPress Enter to continue...")


# # DASHBOARD--
print("\n\tBank Management System") 
while True:
    print("\t---------------------------")
    print("""\t1- Create Account
    2- View All Accounts
    3- Deposit
    4- Withdraw
    5- Check Balance
    6- Delete Account
    7- View account details
    8- Transfer Money
    0- Exit\n""")
    ch = int(input("Enter Your Choice : "))
    if ch == 0:
        print("\n\tTHANK YOU")
        break
    elif ch == 1:
        createAccount()
    elif ch == 2:
        viewAllAccount()
    elif ch == 3:
        deposit()
    elif ch == 4:
        withdraw()
    elif ch == 5:
        checkBalance()
    elif ch == 6:
        DeleteAccount()
    elif ch== 7:
        viewAccount()
    elif ch == 8:
        transferMoney()
    else:
        input("\n\tWRONG CHOICE\n\tTRY AGAIN") 