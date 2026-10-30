

n = int(input("Enter number of products: "))

total_discrepancies = 0
total_replenishment = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")

    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum required stock: "))

    expected = opening + incoming - dispatched

    print("\nProduct Name:", name)
    print("Expected Closing Stock:", expected)
    print("Actual Closing Stock:", closing)

    if expected == closing:
        print("Inventory Status: No Discrepancy")

    else:
        difference = abs(expected - closing)
        print("Inventory Status: Discrepancy Detected")
        print("Discrepancy Quantity:", difference)
        total_discrepancies += 1

    if closing < minimum:
        replenish = minimum - closing
        print("Replenishment Required:", replenish)
        total_replenishment += replenish

    else:
        print("Replenishment Required: 0")

print("\n----- INVENTORY SUMMARY -----")
print("Total Products:", n)
print("Products with Discrepancies:", total_discrepancies)
print("Total Replenishment Quantity:", total_replenishment)
print("Inventory Reconciliation Completed")

