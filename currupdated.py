from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()
window = tk.Tk()
window.geometry("550x350")
window.title("Currency Converter")
window.resizable(False, False)
window.iconbitmap(r"D:\VS\Python\Class 78 (Currency Converter Project - UPDATED)\icon.ico")

             ####### Dictionary mapping descriptive currency names to standard currency codes ########

currency_mapping = {
    "US Dollar (USD)": "USD",
    "Euro (EUR)": "EUR",
    "Pound Sterling (GBP)": "GBP",
    "Indian Rupee (INR)": "INR",
    "Australian Dollar (AUD)": "AUD",
    "Canadian Dollar (CAD)": "CAD",
    "Swiss Franc (CHF)": "CHF",
    "Chinese Yuan (CNY)": "CNY",
    "Japanese Yen (JPY)": "JPY",
    "South Korean Won (KRW)": "KRW",
    "Russian Ruble (RUB)": "RUB",
    "Brazilian Real (BRL)": "BRL",

    ###### Add more mappings as needed ########

}

          ########## Get currency list for dropdown ##########

currency_list = list(currency_mapping.keys())

def clicked():
    amount = float(e1.get())
    cur1 = currency_mapping[var1.get()]
    cur2 = currency_mapping[var2.get()]
    data = round(c.convert(amount, cur1, cur2), 2)  # Round the result to 2 decimal places
    l5.config(text=str(data))

                   ############### LABELS ###############

l1 = tk.Label(text="Currency Converter", font="Times 28 bold")
l1.place(x=78, y=30)

l2 = tk.Label(window, text="Enter amount here:- ", font="Times 18 bold")
l2.place(x=75, y=85)
e1 = tk.Entry(window)

l3 = tk.Label(window, text="Select source Currency:- ", font="Times 18 bold")
l3.place(x=75, y=130)

                  ############### Dropdown for source currency ###############

var1 = tk.StringVar(window)
var1.set("US Dollar (USD)")  # Set default value
option_menu1 = tk.OptionMenu(window, var1, *currency_list)
option_menu1.place(x=340, y=130)

l4 = tk.Label(window, text="Select target Currency:- ", font="Times 18 bold")
l4.place(x=75, y=170)

               ############### Dropdown for target currency ################

var2 = tk.StringVar(window)
var2.set("Euro (EUR)")  # Set default value
option_menu2 = tk.OptionMenu(window, var2, *currency_list)
option_menu2.place(x=340, y=170)

b1 = tk.Button(window, text="Submit", command=clicked)
b1.place(x=240, y=230)

e1.place(x=300, y=92)

l5 = tk.Label(window, text="", font="Times 20 bold")
l5.place(x=200, y=280)

window.mainloop()
