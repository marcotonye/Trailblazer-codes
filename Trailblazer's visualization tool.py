import tkinter as tk
from tkinter import ttk
from datetime import datetime
import yfinance as yf
from matplotlib import pyplot as plot
import seaborn as sns
from tkcalendar import Calendar, DateEntry
import requests
from matplotlib import pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from io import StringIO
import pandas as pd
from tkinter import messagebox

# NEEDS pip install tkcalendar


# Processing but needs more maybe
def data_process(data):
    data.fillna(data.mean(), inplace=True)
    return data


def appropriate_formats_for_UI():
    pass


def checking_correct_times():
    start_date = cal.get()
    end_date = end_date_entry.get()
    try:
        # Check start date format
        date_obj = datetime.strptime(start_date, "%m/%d/%y")
        start_formatted_date = date_obj.strftime("%Y-%m-%d")

        # Check end date format
        date_obj2 = datetime.strptime(end_date, "%m/%d/%y")
        end_formatted_date = date_obj2.strftime("%Y-%m-%d")

        print("Start date:", start_formatted_date)
        print("End date:", end_formatted_date)
        return "good"
    except ValueError:
        messagebox.showerror("Error", "Incorrect date format. Please use MM/DD/YY format.")
        return "bad"


def api_request(type_link):
    # Alpha api and api key
    company = symbol_set.get()
    start_date = cal.get()
    end_date = end_date_entry.get()

    date_obj = datetime.strptime(start_date, "%m/%d/%y")
    start_formatted_date = date_obj.strftime("%Y-%m-%d")

    date_obj2 = datetime.strptime(end_date, "%m/%d/%y")
    end_formatted_date = date_obj2.strftime("%Y-%m-%d")

    print("start_formatted_date",start_formatted_date)

    if type_link == "Alpha Vantage":
        ALPHA_VANTAGE_API_KEY = 'F7FWQ4EXBMGGTMNJ'
        ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
        #print("ts infomations",ts)
        data, meta_data = ts.get_daily(symbol=company, outputsize='full')
        data.sort_index(inplace=True)
        data = data.loc[start_formatted_date:end_formatted_date]
        print("data all of this ",data)
        return data

    elif type_link == "seeking-alpha":
        Seek_api = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"
        querystring = {"query":"apple","type":"people,symbols,pages","size":"5"}
        headers = {"X-RapidAPI-Key": "958633a3e3mshfc05924ce815d2cp1532f8jsn2adbe4e34d32","X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"}
        #data_test = """  """
        return data


def api_appropriate_formats():
    test = api_request(api_picker.get())
    return test


def make_graph():

   if checking_correct_times() == "good":
       data = api_appropriate_formats()
       plt.figure(figsize=(12, 6))
       sns.lineplot(x=data.index, y=data['4. close'])
       plt.title(f'Stock Prices for {symbol_set.get()}')
       plt.xlabel('Date')
       plt.ylabel('Price')
       plt.show()


# Clears the entry boxes and will use a button
def reset_boxes():
    start_date.delete(0, 'end')
    end_date_entry.delete(0, 'end')
    symbol_set.delete(0, 'end')


# Create main window
graph = tk.Tk()
graph.title("Trailblazer's Visualization tool")


# Creates the API picker combobox and places it on row 0
api_label = ttk.Label(graph, text="Pick the API data:")
api_label.grid(row=0, column=0, padx=10, pady=5)
# Define the default value for the combobox
default_value = tk.StringVar(value="Alpha Vantage")
# Define the combobox with options
api_picker = ttk.Combobox(graph, values=['Alpha Vantage'], width=18, textvariable=default_value)
api_picker.grid(row=0, column=1, padx=10, pady=5)


# Creates and places labels and talk boxes
start_date = ttk.Label(graph, text="Start at - (MM-DD-YY):")
start_date.grid(row=1, column=0, padx=10, pady=5)
cal = DateEntry(graph, width= 16, background= "magenta3", foreground= "white",bd=2)
cal.grid(row=1, column=1, padx=10, pady=5)
cal.insert(0, '')


end_date = ttk.Label(graph, text="End at - (MM-DD-YY):")
end_date.grid(row=2, column=0, padx=10, pady=5)
end_date_entry = DateEntry(graph, width= 16, background= "magenta3", foreground= "white",bd=2)
end_date_entry.grid(row=2, column=1, padx=10, pady=5)
end_date_entry.insert(0, '')


# Labels - Google = GOOGL, Microsoft = MSFT, Amazon = AMZN
symbol_label = ttk.Label(graph, text="Pick or Type the stock:")
symbol_label.grid(row=3, column=0, padx=10, pady=5)
symbol_set = ttk.Combobox(graph, values=["GOOGL", "AMZN", "MSFT","WMT","GME","FB"], width=10)
symbol_set.grid(row=3, column=1, padx=10, pady=5)
# Default option
symbol_set.set(" ")

# Creates the graph with the start button
start_button = ttk.Button(graph, text="Graph", command=make_graph)
start_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

# Clears all the boxes with a reset button
# reset_button = ttk.Button(graph, text="Clear", command=reset_boxes)
# reset_button.grid(row=4, column=1, padx=5, pady=20)

# Start the Tkinter event loop
graph.mainloop()
