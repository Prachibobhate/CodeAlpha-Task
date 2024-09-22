#TASK 2
#STOCK PORTFOLIO TRACKER
import tkinter as tk
from tkinter import messagebox
import requests

class StockPortfolio:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Portfolio Tracker")
        self.stocks = {}

        self.symbol_label = tk.Label(master, text="Stock Symbol:")
        self.symbol_label.grid(row=0, column=0)
        self.symbol_entry = tk.Entry(master)
        self.symbol_entry.grid(row=0, column=1)

        self.add_button = tk.Button(master, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=0, column=2)

        self.stock_listbox = tk.Listbox(master, width=40)
        self.stock_listbox.grid(row=1, columnspan=3)

        self.remove_button = tk.Button(master, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=2, column=1)

        self.refresh_button = tk.Button(master, text="Refresh Prices", command=self.refresh_prices)
        self.refresh_button.grid(row=2, column=2)

        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=3, columnspan=3)

    def add_stock(self):
        symbol = self.symbol_entry.get().upper()
        if not symbol:
            self.message_label.config(text="Stock symbol cannot be empty.")
            return
        
        if symbol in self.stocks:
            self.message_label.config(text="Stock already exists in the portfolio.")
            return

        try:
            price = self.get_stock_price(symbol)
            self.stocks[symbol] = price
            self.update_listbox()
            self.message_label.config(text="Stock added successfully.")
        except Exception as e:
            self.message_label.config(text=f"Failed to add stock: {e}")

    def remove_stock(self):
        selected_index = self.stock_listbox.curselection()
        if not selected_index:
            self.message_label.config(text="Please select a stock to remove.")
            return

        symbol = self.stock_listbox.get(selected_index[0]).split(":")[0].strip()
        del self.stocks[symbol]
        self.update_listbox()
        self.message_label.config(text="Stock removed successfully.")

    def refresh_prices(self):
        for symbol in list(self.stocks.keys()):  # Use list to avoid RuntimeError
            try:
                price = self.get_stock_price(symbol)
                self.stocks[symbol] = price
            except Exception as e:
                self.message_label.config(text=f"Failed to refresh price for {symbol}: {e}")
        self.update_listbox()

    def get_stock_price(self, symbol):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            raise Exception("Invalid response from API")

    def update_listbox(self):
        self.stock_listbox.delete(0, tk.END)
        for symbol, price in self.stocks.items():
            self.stock_listbox.insert(tk.END, f"{symbol}: ${price:.2f}")

def main():
    root = tk.Tk()
    app = StockPortfolio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
