# Experiment 14: Warehouse Inventory Reconciliation

## 1. Problem Statement

Develop a Python program to compare opening stock, incoming quantities, dispatched quantities, and closing stock across multiple products. Detect inventory discrepancies and calculate the replenishment requirements for products with insufficient stock.

## 2. Algorithm

1. Start.
2. Enter the number of products.
3. For each product, enter:
   - Product name.
   - Opening stock.
   - Incoming quantity.
   - Dispatched quantity.
   - Actual closing stock.
   - Minimum required stock.
4. Calculate expected closing stock using:

&#x20;  Expected Closing Stock = Opening Stock + Incoming Stock − Dispatched Stock

5. Compare expected closing stock with actual closing stock.
6. If both are equal, display no discrepancy.
7. Otherwise, display inventory discrepancy.
8. Calculate replenishment quantity if actual closing stock is below minimum required stock.
9. Display the inventory summary.
10. Stop.

## 3. Flowchart – Mermaid Code

flowchart TD
 A([START]) --> B[/Enter Number of Products/]
 B --> C[Set i = 1]
 C --> D{i <= Number of Products?}
 D -- No --> M[/Display Inventory Summary/]
 M --> N([STOP])
 D -- Yes --> E[/Enter Product Name and Stock Details/]
 E --> F[Calculate Expected Stock]
 F --> G[Opening + Incoming - Dispatched]
 G --> H{Expected Stock = Actual Stock?}
 H -- Yes --> I[No Discrepancy]
 H -- No --> J[Display Stock Discrepancy]
 I --> K{Actual Stock < Minimum Stock?}
 J --> K
 K -- Yes --> L[Calculate Replenishment Quantity]
 K -- No --> P[No Replenishment Required]
 L --> Q[Display Product Details]
 P --> Q
 Q --> R[Increment i]
 R --> D



## 4. Python Source Code

```
# Warehouse Inventory Reconciliationn = int(input("Enter number of products: "))total_discrepancies = 0for i in range(n):    print("\nProduct", i + 1)    name = input("Enter product name: ")    opening = int(input("Enter opening stock: "))    incoming = int(input("Enter incoming quantity: "))    dispatched = int(input("Enter dispatched quantity: "))    closing = int(input("Enter actual closing stock: "))    minimum = int(input("Enter minimum required stock: "))    expected = opening + incoming - dispatched    print("\nProduct Name:", name)    print("Expected Closing Stock:", expected)    print("Actual Closing Stock:", closing)    if expected == closing:        print("Inventory Status: No Discrepancy")    else:        difference = expected - closing        print("Inventory Status: Discrepancy Detected")        print("Discrepancy Quantity:", abs(difference))        total_discrepancies += 1    if closing < minimum:        replenish = minimum - closing
```

## 5. Sample Input

```
Enter number of products: 3

Product 1
Enter product name: Rice
Enter opening stock: 100
Enter incoming quantity: 50
Enter dispatched quantity: 30
Enter actual closing stock: 120
Enter minimum required stock: 100

Product 2
Enter product name: Sugar
Enter opening stock: 80
Enter incoming quantity: 20
Enter dispatched quantity: 40
Enter actual closing stock: 50
Enter minimum required stock: 70

Product 3
Enter product name: Oil
Enter opening stock: 60
Enter incoming quantity: 30
Enter dispatched quantity: 20
Enter actual closing stock: 70
Enter minimum required stock: 50
```

## 6. Sample Output

```
Product 1
Product Name: Rice
Expected Closing Stock: 120
Actual Closing Stock: 120
Inventory Status: No Discrepancy
Replenishment Required: 0

Product 2
Product Name: Sugar
Expected Closing Stock: 60
Actual Closing Stock: 50
Inventory Status: Discrepancy Detected
Discrepancy Quantity: 10
Replenishment Required: 20

Product 3
Product Name: Oil
Expected Closing Stock: 70
Actual Closing Stock: 70
Inventory Status: No Discrepancy
Replenishment Required: 0

----- INVENTORY SUMMARY -----
Total Products: 3
Products with Discrepancies: 1
Inventory Reconciliation Completed
```

