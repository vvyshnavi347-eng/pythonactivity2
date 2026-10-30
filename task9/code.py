

budget = float(input("Enter your shopping budget: Rs. "))
n = int(input("Enter number of products: "))

names = []
prices = []
quantities = []

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: Rs. "))
    quantity = int(input("Enter quantity: "))

    names.append(name)
    prices.append(price)
    quantities.append(quantity)

def calculate_total():
    subtotal = 0

    for i in range(n):
        subtotal += prices[i] * quantities[i]

    if subtotal >= 1000:
        discount = subtotal * 0.10
    else:
        discount = 0

    total = subtotal - discount

    return subtotal, discount, total


subtotal, discount, total = calculate_total()

print("\nInitial Shopping Total:", round(total, 2))

while total > budget:
    max_price = -1
    index = -1

    for i in range(n):
        if quantities[i] > 0 and prices[i] > max_price:
            max_price = prices[i]
            index = i

    if index == -1:
        break

    quantities[index] -= 1

    print("Reduced quantity of:", names[index])

    subtotal, discount, total = calculate_total()

print("\n----- FINAL SHOPPING BILL -----")

for i in range(n):
    print(names[i], "Quantity:", quantities[i],
          "Amount:", round(prices[i] * quantities[i], 2))

print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
print("Final Bill:", round(total, 2))
print("Budget:", round(budget, 2))

if total <= budget:
    print("Status: Within Budget")
else:
    print("Status: Budget Cannot Be Met")

print("Program Completed")

