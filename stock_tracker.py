stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 200
}

total = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))

        value = stocks[stock] * quantity
        total += value

        print("Added:", stock)
        print("Value:", value)

    else:
        print("Stock not available!")

print("\nTotal Portfolio Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Portfolio Value = " + str(total))

print("Portfolio saved to portfolio.txt")