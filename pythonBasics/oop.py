def menu():
    print("banking system")
    menu()
    choice=int(input("enter your choice"))
    if choice==1:
        print("balance:",balance)
    elif choice==2:
        amount=int(input("enter the amount you want to deposit:"))
        balance+=amount
        print("balance after depositing:",balance)
    elif choice==3:
        amount=int(input("enter you withdrawl amount:"))
        if amount>balance:
            print("insuffcient balance")
        else:
            balance -= amount
            print("withddrawl successful",balance)   