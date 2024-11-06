

from currency_converter import CurrencyConverter
import tkinter as tk
import tkinter.font as tkFont

c = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

window.configure(background='pink')
def clicked():
    amount = float(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window,text=data, font = font ).place(x=200,y=300)

font = tkFont.Font(family="italic",size=12,weight="normal")
label = tk.Label(window,text= "Currency Converter",font = "Times 20 bold").place(x=120,y=40)
label1 = tk.Label(window,text = "Enter Your Amount: ",font = font).place(x=70,y=100)

entry1  = tk.Entry(window)

label2= tk.Label(window, text ='Enter Your Currency: ', font = font).place(x=70, y=150)
entry2= tk.Entry(window)

label3 = tk.Label(window,text = "Enter Desired currency: ",font = font ).place(x=70,y=200)
entry3  = tk.Entry(window)

button = tk.Button(window,text = "click",font= font,command = clicked).place(x=365,y=250)
entry1.place(x=270,y=100)
entry2.place(x=270,y=150)
entry3.place(x=270,y=200)
window.mainloop()