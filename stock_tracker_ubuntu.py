import tkinter as tk
import yfinance as yf

def update_stock():
    stock = entry_symbol.get().upper().strip()
    try:
        data = yf.Ticker(stock)
        info = data.info
        price = info.get("currentPrice")  # Check if 'currentPrice' is available
        if price is None:
            label_price.config(text="No Data Available")
        else:
            label_price.config(text=f"{stock}: ₹{price:.2f}")
    except Exception as e:
        label_price.config(text="Invalid Symbol")

    root.after(2000, update_stock)

# GUI setup
root = tk.Tk()
root.title("Stock Tracker")
root.geometry("200x100")
root.attributes('-topmost', 1)
root.configure(bg="black")

entry_symbol = tk.Entry(root, font=("Arial", 12), width=10)
entry_symbol.pack()

label_price = tk.Label(root, text="Enter a Stock", font=("Arial", 14), fg="white", bg="black")
label_price.pack()

btn_update = tk.Button(root, text="Track", command=update_stock)
btn_update.pack()

root.mainloop()
#import tkinter as tk
#from nsepython import nse_eq
#
#def update_stock():
#    symbol = entry_symbol.get().upper().strip()
#    try:
#        data = nse_eq(symbol)
#        price = data['priceInfo']['lastPrice']
#        label_price.config(text=f"{symbol}: ₹{price}")
#    except Exception as e:
#        label_price.config(text="Invalid or No Data")
#
#    root.after(30000, update_stock)
#
## GUI setup
#root = tk.Tk()
#root.title("Live NSE Stock Tracker")
#root.geometry("250x120")
#root.attributes('-topmost', 1)
#root.configure(bg="black")
#
#entry_symbol = tk.Entry(root, font=("Arial", 12), width=12)
#entry_symbol.pack(pady=5)
#
#label_price = tk.Label(root, text="Enter NSE Symbol", font=("Arial", 13), fg="white", bg="black")
#label_price.pack(pady=5)
#
#btn_update = tk.Button(root, text="Track", font=("Arial", 10), command=update_stock)
#btn_update.pack(pady=5)
#
#root.mainloop()

