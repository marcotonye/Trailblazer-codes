import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# Function to collect data from Alpha Vantage API
# I used 'symbol' instead of setting the symbol as "AAPL". you can change it if you want.
def collect_stock_data_alpha_vantage(symbol, start_date, end_date):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=Insert api key here'
    r = requests.get(url)
    data = r.json()
    stock_data = data.get('Time Series (Daily)', {})
    # Filter the collected data
    filtered_data = {date: stock_data[date] for date in stock_data if start_date <= date <= end_date}
    return filtered_data


# Function used to make graph
def make_graph():
    symbol = symbol_set.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get() \

    # Get the API choice
    api_provider = api_collector_combobox.get()

    if api_provider == "Alpha Vantage":
        data = collect_stock_data_alpha_vantage(symbol, start_date, end_date)

# Another API provider?
    # elif api_provider == "Seeking Alpha":
    #    data = fetch_stock_data_seeking_alpha(symbol, start_date, end_date)

    else:
        print("Invalid API selected.")
        return

    if data:
        stock_df = pd.DataFrame(data).T
        stock_df.index = pd.to_datetime(stock_df.index)

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=stock_df['4. close'])
        plt.title(f'Stock Prices for {symbol}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()
    else:
        print("Failed")


# Clears the entry boxes and will use a button
def reset_boxes():
    start_date_entry.delete(0, 'end')
    end_date_entry.delete(0, 'end')


# Create main window
graph = tk.Tk()
graph.title("Trailblazer's Visualization tool")

# Creates and places labels and talk boxes
start_date = ttk.Label(graph, text="Start at - (YYYY-MM-DD):")
start_date.grid(row=0, column=0, padx=10, pady=5)
start_date_entry = ttk.Entry(graph, width=15)
start_date_entry.grid(row=0, column=1, padx=10, pady=5)
start_date_entry.insert(0, '')

end_date = ttk.Label(graph, text="End at - (YYYY-MM-DD):")
end_date.grid(row=1, column=0, padx=10, pady=5)
end_date_entry = ttk.Entry(graph, width=15)
end_date_entry.grid(row=1, column=1, padx=10, pady=5)
end_date_entry.insert(0, '')

# Labels examples - Google = GOOGL, Microsoft = MSFT, Amazon = AMZN
symbol_label = ttk.Label(graph, text="Pick the stock:")
symbol_label.grid(row=3, column=0, padx=10, pady=5)
symbol_set = ttk.Entry(graph, width=10)
symbol_set.grid(row=3, column=1, padx=10, pady=5)
# Default option
symbol_set.insert(0, '')

# Label and combobox for selecting API
api_provider_label = ttk.Label(graph, text="Select API:")
api_provider_label.grid(row=2, column=0, padx=10, pady=5)
api_collector_combobox = ttk.Combobox(graph, values=["Alpha Vantage"], width=15)
api_collector_combobox.grid(row=2, column=1, padx=10, pady=5)
api_collector_combobox.set("")  # Default option

# Creates the graph with the graph button
start_button = ttk.Button(graph, text="Graph", command=make_graph)
start_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

# Clears all the boxes with a clear button
reset_button = ttk.Button(graph, text="Clear", command=reset_boxes)
reset_button.grid(row=4, column=1, padx=5, pady=20)

# Start the Tkinter event loop
graph.mainloop()
