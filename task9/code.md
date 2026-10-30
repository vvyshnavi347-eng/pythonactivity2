

## 1. Problem Statement

Evaluate a shopping basket containing multiple products and their quantities. Calculate the total cost, apply discount conditions, compare the final amount with a fixed budget, and reduce product quantities when necessary to stay within the budget.

## 2. Algorithm

1. Start.
2. Input the shopping budget.
3. Input the number of products.
4. For each product, input its name, price, and quantity.
5. Calculate the subtotal of all products.
6. Check whether the subtotal meets the discount condition.
7. Apply a 10% discount if the subtotal is ₹1000 or more.
8. Compare the final bill with the available budget.
9. If the bill exceeds the budget, reduce the quantity of the costliest product.
10. Recalculate the subtotal and discount.
11. Repeat until the bill is within the budget or all quantities become zero.
12. Display the final products, quantities, discount, and total bill.
13. Stop.

## 3. Flowchart (Copyable Text)

```

                 START
                   |
                   v
              INPUT BUDGET
                   |
                   v
             INPUT PRODUCTS
                   |
                   v
        INPUT PRICE AND QUANTITY
                   |
                   v
           CALCULATE SUBTOTAL
                   |
                   v
        IS SUBTOTAL >= 1000?
             /          \
           YES           NO
            |             |
            v             |
       APPLY 10%          |
        DISCOUNT          |
            |             |
            +------+------+
                   |
                   v
        CALCULATE FINAL BILL
                   |
                   v
        IS BILL WITHIN BUDGET?
              /         \
            YES          NO
             |            |
             v            v
       DISPLAY BILL   FIND COSTLIEST
                         PRODUCT
                            |
                            v
                     REDUCE QUANTITY
                            |
                            v
                     RECALCULATE BILL
                            |
                            +---- REPEAT
                   |
                   v
                  STOP

```

## 4. Python Source Code

```
# Multi-Product Shopping Budget Constraintbudget = float(input("Enter your shopping budget: Rs. "))n = int(input("Enter number of products: "))names = []prices = []quantities = []for i in range(n):    print("\nProduct", i + 1)    name = input("Enter product name: ")    price = float(input("Enter product price: Rs. "))    quantity = int(input("Enter quantity: "))    names.append(name)    prices.append(price)    quantities.append(quantity)def calculate_total():    subtotal = 0    for i in range(n):        subtotal += prices[i] * quantities[i]    if subtotal >= 1000:        discount = subtotal * 0.10    else:        discount = 0    total = subtotal - discount    return subtotal, discount, total
```

## 5. Sample Input

```
Enter your shopping budget: Rs. 1500
Enter number of products: 3

Product 1
Enter product name: Shoes
Enter product price: Rs. 800
Enter quantity: 2

Product 2
Enter product name: Bag
Enter product price: Rs. 500
Enter quantity: 2

Product 3
Enter product name: Bottle
Enter product price: Rs. 200
Enter quantity: 1
```

## 6. Sample Output

```
Initial Shopping Total: 2070.0
Reduced quantity of: Shoes
Reduced quantity of: Bag

----- FINAL SHOPPING BILL -----

Shoes Quantity: 1 Amount: 800.0
Bag Quantity: 1 Amount: 500.0
Bottle Quantity: 1 Amount: 200.0

Subtotal: 1500.0
Discount: 150.0
Final Bill: 1350.0
Budget: 1500.0

Status: Within Budget
Program Completed
```

Note: The program applies a 10% discount when the subtotal is ₹1000 or more. If the budget is exceeded, it reduces one unit at a time from the costliest available product.
