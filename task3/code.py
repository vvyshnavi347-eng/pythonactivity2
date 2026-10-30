

balance = float(input("Enter initial balance: "))
withdrawal_limit = float(input("Enter withdrawal limit: "))

n = int(input("Enter number of transactions: "))

successful = 0
rejected = 0

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdrawal")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid transaction amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        print("Deposit successful")
        successful += 1

    elif choice == 2:
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            print("Withdrawal successful")
            successful += 1

    else:
        print("Invalid transaction type")
        rejected += 1

print("\n----- ATM TRANSACTION SUMMARY -----")
print("Final Balance:", round(balance, 2))
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)

print("\nProgram Completed")
