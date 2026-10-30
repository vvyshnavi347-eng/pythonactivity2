

## 1. Problem Statement

Develop a Python program to simulate ATM transactions. The program should process a sequence of deposits and withdrawals, maintain the account balance, enforce withdrawal limits, reject invalid transactions, and display a summary of all successful and rejected transactions.

## 2. Algorithm

1. Start.
2. Enter the initial account balance.
3. Enter the maximum withdrawal limit.
4. Enter the number of transactions.
5. Repeat for each transaction:
   - Select deposit or withdrawal.
   - Enter the transaction amount.
   - Check whether the amount is valid.
   - For deposits, add the amount to the balance.
   - For withdrawals, check the balance and withdrawal limit.
   - If valid, process the transaction; otherwise, reject it.
6. Display the final balance.
7. Display successful and rejected transaction counts.
8. Stop.

## 3. Flowchart (Mermaid Code)

             START
               |
               v
      Enter Initial Balance
               |
               v
      Enter Withdrawal Limit
               |
               v
     Enter Number of Transactions
               |
               v
       Enter Transaction Type
          and Amount
               |
               v
         Is Amount > 0?
          /         \
        No           Yes
        |             |
        v             v
  Reject Transaction  Transaction Type?
        |             |
        |       +-----+------+
        |       |            |
        |     Deposit     Withdrawal
        |       |            |
        |       v            v
        |  Add Amount    Amount <= Limit?
        |  to Balance      /       \
        |                No         Yes
        |                |           |
        |                v           v
        |           Reject      Amount <= Balance?
        |                       /          \
        |                     No            Yes
        |                     |              |
        |                     v              v
        |                  Reject       Subtract Amount
        |                               from Balance
        |                                    |
        +----------------+-------------------+
                         |
                         v
                Update Transaction Count
                         |
                         v
                 More Transactions?
                    /        \
                  Yes         No
                   |           |
                   v           v
             Enter Next    Display Final Balance
             Transaction   and Transaction Summary
                                |
                                v
                               STOP



## 4. Python Source Code

```
# ATM Transaction Sequence Simulationbalance = float(input("Enter initial balance: "))limit = float(input("Enter withdrawal limit: "))n = int(input("Enter number of transactions: "))successful = 0rejected = 0for i in range(n):    print("\nTransaction", i + 1)    print("1. Deposit")    print("2. Withdrawal")    choice = int(input("Enter your choice: "))    amount = float(input("Enter transaction amount: "))    if amount <= 0:        print("Invalid transaction amount")        rejected += 1    elif choice == 1:        balance += amount        print("Deposit successful")        successful += 1    elif choice == 2:        if amount > limit:            print("Withdrawal limit exceeded")            rejected += 1        elif amount > balance:            print("Insufficient balance")            rejected += 1
```

## 5. Sample Input

```
Enter initial balance: 5000
Enter withdrawal limit: 2000
Enter number of transactions: 4

Transaction 1
Enter your choice: 1
Enter transaction amount: 1000

Transaction 2
Enter your choice: 2
Enter transaction amount: 1500

Transaction 3
Enter your choice: 2
Enter transaction amount: 3000

Transaction 4
Enter your choice: 2
Enter transaction amount: 6000
```

## 6. Sample Output

```
Transaction 1
Deposit successful

Transaction 2
Withdrawal successful

Transaction 3
Withdrawal limit exceeded

Transaction 4
Withdrawal limit exceeded

----- ATM TRANSACTION SUMMARY -----
Final Balance: 4500.0
Successful Transactions: 2
Rejected Transactions: 2

Program Completed
```

For your flowchart: Copy only the Mermaid code inside the flowchart box, open Mermaid Live Editor, paste it into the left-side editor, and the diagram will appear on the right.
