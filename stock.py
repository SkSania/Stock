#Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

# Dictionary to store user input
portfolio = {}

# Input stock information
while True:
    stock = input("Enter stock symbol (e.g., AAPL) or type 'done' to finish: ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found in price list.")

# Calculate total investment
total_investment = 0
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to {filename}")
