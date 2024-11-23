import http.client
import json

# Initialize portfolio
portfolio = {}

def fetch_stock_price(ticker):
    """Fetch the current stock price using a public financial API."""
    conn = http.client.HTTPSConnection("api.twelvedata.com")
    api_key = "your_api_key_here"  # Replace with your Twelve Data API key
    endpoint = f"/price?symbol={ticker}&apikey={api_key}"

    conn.request("GET", endpoint)
    response = conn.getresponse()
    if response.status == 200:
        data = json.loads(response.read().decode())
        return float(data.get("price", 0))
    else:
        print(f"Error fetching data for {ticker}: {response.status}")
        return None

def add_stock(ticker, quantity):
    """Add a stock to the portfolio with the specified quantity."""
    ticker = ticker.upper()
    if ticker in portfolio:
        portfolio[ticker] += quantity
    else:
        portfolio[ticker] = quantity
    print(f"Added {quantity} shares of {ticker}.")

def remove_stock(ticker):
    """Remove a stock from the portfolio."""
    ticker = ticker.upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from the portfolio.")
    else:
        print(f"{ticker} is not in the portfolio.")

def display_portfolio():
    """Display the portfolio with real-time stock data."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nFetching real-time data...")
    total_portfolio_value = 0
    for ticker, quantity in portfolio.items():
        price = fetch_stock_price(ticker)
        if price is not None:
            total_value = price * quantity
            total_portfolio_value += total_value
            print(f"{ticker}: {quantity} shares @ ${price:.2f} = ${total_value:.2f}")
        else:
            print(f"Could not fetch price for {ticker}.")

    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

# Menu-driven tool
def menu():
    """Display the menu and interact with the user."""
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add a stock")
        print("2. Remove a stock")
        print("3. Display portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            ticker = input("Enter the stock ticker symbol: ")
            quantity = int(input("Enter the quantity of shares: "))
            add_stock(ticker, quantity)
        elif choice == "2":
            ticker = input("Enter the stock ticker symbol to remove: ")
            remove_stock(ticker)
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the tool
if __name__ == "__main__":
    menu()

                            


                                  
    
