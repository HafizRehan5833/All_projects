def shoe_balance():
   print(f"Your balance is {balance}")
    

def deposit():
    amount=int(input("Enter an amount to be deposit:"))
    if amount<=0:
        print("Your balance is less than zero..")
        return 0
    else:
        print( f"\nYour balance is {amount + balance}")
        return amount    

def withdraw():
    amount=int(input("\nEnter how much amount you want to withdraw: "))

    if amount>balance:
        print("Insufficient balance..")
    elif amount<0:
        print("Amount must be greater than zero..")
        return 0
    else:
        #return f"Your balance is {amount - balance}"
        print(f"\n\t\t\t\tYour balance after withdrawal: {balance-amount}")
        return amount


balance=0
is_running=True

print("\t\t\t\t\tBannking program")

while is_running:
    #print("\t\t\t\t\tBannking program")
    print("\n1.show balance\t\t\t\t2.Deposit\n3.Withdrawal\t\t\t\t4.Exit")


    choice=input("\t\t\tenter option: ")


    if choice =="1":
        shoe_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        break

    else:
        print("\t\t\tThis is not a valid option")      

print("\n\t\t\t\tThank you for using this machine...")