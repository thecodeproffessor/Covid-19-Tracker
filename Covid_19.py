"""
Covid-19 Tracker using python
"""


# importing the libraries
import tkinter as tk
from covid import Covid
import matplotlib.pyplot as plt

cov = tk.Tk()
cov.title("Covid_19 Tracker")
cov.geometry("400x400")
cov.configure(bg="cyan")


def details():
    word = entry.get()
    covid = Covid()
    data = covid.get_status_by_country_name(word)
    card = {
        key:data[key]
        for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
    }

    dict_key = list(card.keys())
    dict_value = list(card.values())
    print(card)
    label1 = tk.Label(cov, text=f"Results: {card}", bg="cyan")
    label1.grid(row=3, column=0)

    # chart
    plt.title(word)
    plt.bar(range(len(card)), dict_key, tick_label=dict_value)
    plt.show()


label = tk.Label(cov, text="Country name: ")
label.grid(row=0, column=0, sticky="w")
entry = tk.Entry(cov)
entry.grid(row=1, column=0)
button = tk.Button(cov, text="Enter", command=details)
button.grid(row=1, column=2)

cov.mainloop()
