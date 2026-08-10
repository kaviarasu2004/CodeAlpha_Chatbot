"""
CodeAlpha - Task 2: Stock Portfolio Tracker
Calculates total investment value based on hardcoded stock prices
and saves a summary to a .txt file.
"""

import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
    "INFY": 1550,
    "TCS": 3850,
}


def get_portfolio_from_user():
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Enter stock name and quantity. Type 'done' as stock name to finish.\n")

    while True:
        stock = input("Stock symbol: ").upper().strip()
        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be positive.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock}.\n")

    return portfolio


def calculate_investment(portfolio):
    breakdown = []
    total = 0
    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        total += value
        breakdown.append((stock, quantity, price, value))
    return breakdown, total


def save_summary(breakdown, total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price per Share", "Value"])
        for stock, quantity, price, value in breakdown:
            writer.writerow([stock, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
        writer.writerow(["Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    print(f"\nSummary saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("No stocks added. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)

    print("\n--- Portfolio Summary ---")
    for stock, quantity, price, value in breakdown:
        print(f"{stock}: {quantity} shares x ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total}")

    save_summary(breakdown, total)


if __name__ == "__main__":
    main()
