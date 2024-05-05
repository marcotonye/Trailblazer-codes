import tkinter as tk
from tkinter import ttk
from alpha_vantage.timeseries import TimeSeries
import requests
from matplotlib import pyplot as plt
import seaborn as sns

# API keys
# Alpha Vantage API Key
ALPHA_VANTAGE_API_KEY = 'KCXVI4DZZZZDAGOP'

# Second API Key could go here


# Processing
def data_process(data):
    data.fillna(data.mean(), inplace=True)
    return data


# alpha vantage API
def get_alpha_vantage_data(symbol, start_date, end_date):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    data.sort_index(inplace=True)
    data = data.loc[start_date:end_date]
    return data


# Creates the graph
def make_graph():
    symbol = symbol_set.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    if api_picker.get() == 'Alpha Vantage':
        data = get_alpha_vantage_data(symbol, start_date, end_date)
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=data.index, y=data['4. close'])
        plt.title(f'Stock Prices for {symbol}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()


# Clears the entry boxes
def reset_boxes():
    start_date_entry.delete(0, 'end')
    end_date_entry.delete(0, 'end')
    symbol_set.delete(0, 'end')


# Name's the graph
graph = tk.Tk()
graph.title("Trailblazer's Visualization tool")

# Creates the API picker combobox and places it on row 0
api_label = ttk.Label(graph, text="Pick the API data:")
api_label.grid(row=0, column=0, padx=10, pady=5)
api_picker = ttk.Combobox(graph, values=['Alpha Vantage', 'Second API goes here'], width=18)
api_picker.grid(row=0, column=1, padx=10, pady=5)

# Creates the start date entry box at row 1
start_date = ttk.Label(graph, text="Start at - (YYYY-MM-DD):")
start_date.grid(row=1, column=0, padx=10, pady=5)
start_date_entry = ttk.Entry(graph, width=15)
start_date_entry.grid(row=1, column=1, padx=10, pady=5)
start_date_entry.insert(0, '')

# Creates the end date entry box at row 2
end_date = ttk.Label(graph, text="End at - (YYYY-MM-DD):")
end_date.grid(row=2, column=0, padx=10, pady=5)
end_date_entry = ttk.Entry(graph, width=15)
end_date_entry.grid(row=2, column=1, padx=10, pady=5)
end_date_entry.insert(0, '')

# Creates the symbol entry box at row 3
symbol_label = ttk.Label(graph, text="Enter a stock:\nExamples: AAPL, GME, MSFT")
symbol_label.grid(row=3, column=0, padx=10, pady=5)
symbol_set = ttk.Entry(graph, width=15)
symbol_set.grid(row=3, column=1, padx=10, pady=5)
symbol_set.insert(0, '')

# Start button that will make the graph
start_button = ttk.Button(graph, text="Graph", command=make_graph)
start_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

# Reset button/clear button that deletes the user input in the entry boxes.
reset_button = ttk.Button(graph, text="Clear", command=reset_boxes)
reset_button.grid(row=5, column=1, padx=5, pady=20)

# Loop
graph.mainloop()
