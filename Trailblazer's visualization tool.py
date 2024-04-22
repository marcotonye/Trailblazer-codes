import tkinter as tk
from tkinter import ttk
from datetime import datetime
import yfinance as yf
from matplotlib import pyplot as plot
import seaborn as sns


# Processing but needs more maybe
def data_process(data):
    data.fillna(data.mean(), inplace=True)
    return data


def make_graph():
    symbol = symbol_set.get()
    # Google Graph
    if symbol == "GOOGL":
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # Collect the data from yfinance module using a symbol
        data = yf.download(symbol, start=start_date, end=end_date)

        # Visualize data by creating the graph
        plot.figure(figsize=(12, 6))
        sns.lineplot(x=data.index, y=data['Close'])
        plot.title(f'Stock Prices for GOOGLE')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()

    # Amazon Graph
    elif symbol == "AMZN":
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # Collect the data from yfinance module using a symbol
        data = yf.download(symbol, start=start_date, end=end_date)

        # Visualize data by creating the graph
        plot.figure(figsize=(12, 6))
        sns.lineplot(x=data.index, y=data['Close'])
        plot.title(f'Stock Prices for AMAZON')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()
    # Microsoft Graph goes here.
    elif symbol == "MSFT":
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # Collect the data from yfinance module using a symbol
        data = yf.download(symbol, start=start_date, end=end_date)

        # Visualize data by creating the graph
        plot.figure(figsize=(12, 6))
        sns.lineplot(x=data.index, y=data['Close'])
        plot.title(f'Stock Prices for Microsoft')
        plot.xlabel('Date')
        plot.ylabel('Price')
        plot.show()


# Clears the entry boxes and will use a button
def reset_boxes():
    start_date_entry.delete(0, 'end')
    end_date_entry.delete(0, 'end')
    # symbol_set.delete(0, 'end')


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

# Labels - Google = GOOGL, Microsoft = MSFT, Amazon = AMZN
symbol_label = ttk.Label(graph, text="Pick the stock:")
symbol_label.grid(row=2, column=0, padx=10, pady=5)
symbol_set = ttk.Combobox(graph, values=["GOOGL", "AMZN", "MSFT"], width=10)
symbol_set.grid(row=2, column=1, padx=10, pady=5)
# Default option
symbol_set.set(" ")

# Creates the graph with the start button
start_button = ttk.Button(graph, text="Graph", command=make_graph)
start_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Clears all the boxes with a reset button
reset_button = ttk.Button(graph, text="Clear", command=reset_boxes)
reset_button.grid(row=3, column=1, padx=5, pady=20)

# Start the Tkinter event loop
graph.mainloop()
