# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

# Taking stock details from user
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity

# Calculating total investment
print("\nPortfolio Details:")
for stock, quantity in portfolio.items():
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock} -> Quantity: {quantity}, "
              f"Price: {stock_prices[stock]}, "
              f"Investment: {investment}")
    else:
        print(f"{stock} is not available in stock list.")

# Display total investment
print("\nTotal Investment Value =", total_investment)

# Optional: Save result to a file
choice = input("\nDo you want to save the result in a file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Details\n")
        file.write("-------------------------\n")

        for stock, quantity in portfolio.items():
            if stock in stock_prices:
                investment = stock_prices[stock] * quantity
                file.write(
                    f"{stock} -> Quantity: {quantity}, "
                    f"Price: {stock_prices[stock]}, "
                    f"Investment: {investment}\n"
                )

        file.write(f"\nTotal Investment Value = {total_investment}")

    print("Portfolio saved successfully in portfolio.txt")