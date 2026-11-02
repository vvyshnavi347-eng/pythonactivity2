

## 1. Problem Statement

Develop a Python program to reconcile warehouse inventory for multiple products. The program compares opening stock, incoming quantities, dispatched quantities, and actual closing stock. It identifies stock discrepancies and calculates the additional quantity required to replenish inventory.

## 2. Algorithm

1. Start the program.
2. Read the number of products.
3. For each product, enter:
   - Product name
   - Opening stock
   - Incoming quantity
   - Dispatched quantity
   - Actual closing stock
4. Calculate expected closing stock using:

`Expected Closing Stock = Opening Stock + Incoming Stock - Dispatched Stock`

5. Compare expected closing stock with actual closing stock.
6. Calculate the stock discrepancy.
7. If actual stock is less than expected stock, identify a shortage.
8. If actual stock is greater than expected stock, identify excess stock.
9. Calculate replenishment quantity if stock is below the minimum required level.
10. Display the inventory report.
11. Stop the program.

## 3. Flowchart
             ┌───────────────┐
             │     START     │
             └───────┬───────┘
                     │
             ┌───────▼────────┐
             │ Enter Number   │
             │  of Products   │
             └───────┬────────┘
                     │
             ┌───────▼────────┐
             │ Enter Product  │
             │ Stock Details  │
             └───────┬────────┘
                     │
             ┌───────▼────────┐
             │ Calculate      │
             │ Expected Stock │
             └───────┬────────┘
                     │
             ┌───────▼────────┐
             │ Compare Actual │
             │ and Expected   │
             │     Stock      │
             └───────┬────────┘
                     │
               ┌─────▼─────┐
               │ Discrepancy│
               │   Found?   │
               └──┬─────┬──┘
                Yes│     │No
             ┌─────▼──┐ ┌▼────────────┐
             │Identify│ │Stock Balanced│
             │Shortage│ └──────┬──────┘
             │or Excess│       │
             └─────┬──┘       │
                   │          │
                   ▼          ▼
             ┌──────────────────┐
             │ Calculate        │
             │ Replenishment    │
             │ Quantity         │
             └────────┬─────────┘
                      │
               ┌──────▼──────┐
               │ More Products?│
               └───┬──────┬──┘
                 Yes│      │No
              ┌─────▼──┐   │
              │ Enter  │   │
              │ Next   │   │
              │ Product│   │
              └───┬────┘   │
                  │        │
                  └───┐    │
                      │    ▼
                ┌─────▼────────┐
                │ Display Final│
                │ Inventory    │
                │    Report    │
                └──────┬───────┘
                       │
                ┌──────▼───────┐
                │     STOP     │
                └──────────────┘

## 4. Sample Input

```
Enter number of products: 3

Product 1:
Product name: Laptop
Opening stock: 50
Incoming quantity: 20
Dispatched quantity: 30
Actual closing stock: 38

Product 2:
Product name: Keyboard
Opening stock: 100
Incoming quantity: 50
Dispatched quantity: 40
Actual closing stock: 110

Product 3:
Product name: Mouse
Opening stock: 80
Incoming quantity: 20
Dispatched quantity: 30
Actual closing stock: 70
```

## 5. Sample Output

```


Product: Laptop
Expected Closing Stock: 40
Actual Closing Stock: 38
Discrepancy: -2
Status: Stock Shortage

Product: Keyboard
Expected Closing Stock: 110
Actual Closing Stock: 110
Discrepancy: 0
Status: Stock Balanced

Product: Mouse
Expected Closing Stock: 70
Actual Closing Stock: 70
Discrepancy: 0
Status: Stock Balanced

=
