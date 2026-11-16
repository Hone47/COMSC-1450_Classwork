import tkinter as tk 


def on_click():
  
  x = float(e.get())
  if radioVal.get() == "EURO":
    result = x * .92
  elif radioVal.get() == "CAD":
    result = x * .52
  elif radioVal.get() == "AUD":
    result = x * .62
  else:
    result = "Select a currency"
  l2.config(text = round(result, 2))
root = tk.Tk()
root.title("e-commerce shipping")
root.geometry("400x300")


l1 = tk.Label(root, text= "Enter an amount in USD")
l1.pack()

e = tk.Entry(root)
e.pack()
radioVal = tk.StringVar(value="")

radioButton = tk.Radiobutton(root, text = "EURO", variable=radioVal, value="EURO")
radioButton.pack()
radioButton2 = tk.Radiobutton(root, text = "CAD", variable=radioVal, value="CAD")
radioButton2.pack()
radioButton3 = tk.Radiobutton(root, text = "AUD", variable=radioVal, value="AUD")
radioButton3.pack()

b = tk.Button(root, text="Ok", command=on_click)
b.pack()

l2 = tk.Label(root,text="")
l2.pack()
root.mainloop()