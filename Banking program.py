def show_balance():
    print(f"YOur balance is ${balance:.2f}\n\n-------------------------")
def deposit():
    amount=float(input("Enter a amount to be deposited: "))
    if amount<0:
        print("That is not a valid amount/n\n--------------------------")
    else:
        return amount
def withdraw():
    pass
balance=0
is_running=True


while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Dopsit")
    print("3.Withdraw")
    print("4.Exit")

    choice=int(input("Enter your choice(1-4)"))

    if choice==1:
        show_balance()
    elif choice==2:
        balance+=deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        print()
        is_running=False
    else:
        print(f"{choice} that is invalid")

        
print("---------Thank you! have a nice day!--------------------")
