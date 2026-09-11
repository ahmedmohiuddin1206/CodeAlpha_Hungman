# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 190,
    "MSFT": 420
}

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable stocks:")

for stock in stock_prices:
    print(f"{stock}: ${stock_prices[stock]}")

total_investment = 0

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print(f"{stock} price: ${price}")
        print(f"Quantity: {quantity}")
        print(f"Investment in {stock}: ${investment}")

    except ValueError:
        print("Please enter a valid number for quantity.")

print("\n" + "=" * 45)
print(f"TOTAL INVESTMENT: ${total_investment}")
print("=" * 45)

# Save the result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=" * 30 + "\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("\nPortfolio summary saved to portfolio.txt")