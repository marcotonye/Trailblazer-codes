import tkinter as tk
from tkinter import ttk
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from matplotlib import pyplot as plt
import seaborn as sns

# Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = 'KCXVI4DZZZZDAGOP'


# Processing but needs more maybe
def data_process(data):
    data.fillna(data.mean(), inplace=True)
    return data


def make_graph():
    symbol = symbol_set.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Initialize Alpha Vantage TimeSeries using the API key
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    # collects the stock data
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

    # sorts in ascending order
    data.sort_index(inplace=True)

    # Filter the data using the start and end date
    data = data.loc[start_date:end_date]

    # creates the graph
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=data.index, y=data['4. close'])
    plt.title(f'Stock Prices for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()


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

# Labels - Google = GOOGL, Microsoft = MSFT, Amazon = AMZN
symbol_label = ttk.Label(graph, text="Pick the stock:")
symbol_label.grid(row=2, column=0, padx=10, pady=5)
symbol_set = ttk.Entry(graph, width=10)
symbol_set.grid(row=2, column=1, padx=10, pady=5)
# Default option
symbol_set.insert(0, '')

# Creates the graph with the start button
start_button = ttk.Button(graph, text="Graph", command=make_graph)
start_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Clears all the boxes with a reset button
reset_button = ttk.Button(graph, text="Clear", command=reset_boxes)
reset_button.grid(row=3, column=1, padx=5, pady=20)

# Start the Tkinter event loop
graph.mainloop()
