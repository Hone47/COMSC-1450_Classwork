import tkinter as tk 
from tkinter import messagebox
def on_click():
    if e.get() == "":
      messagebox.showwarning("Error","⚠️Input a Value⚠️")
    else:
      x = float(e.get())
      if radioVal.get() == "Standard":
        result = x + 5
      elif radioVal.get() == "Express":
        result = x + 15
      elif radioVal.get() == "Overnight":
        result = x + 30
      else:
       messagebox.showwarning("Error","⚠️Select a Service⚠️")
    l2.config(text = round(result, 2))


  
  
root = tk.Tk()
root.title("ECommerce Shippping APP")
root.geometry("400x300")


l1 = tk.Label(root, text= "Core order amount")
l1.pack()

e = tk.Entry(root)
e.pack()
radioVal = tk.StringVar()

radioButton = tk.Radiobutton(root, text = "Standard", variable=radioVal, value="Standard")
radioButton.pack()
radioButton2 = tk.Radiobutton(root, text = "Express", variable=radioVal, value="Express")
radioButton2.pack()
radioButton3 = tk.Radiobutton(root, text = "Overnight", variable=radioVal, value="Overnight")
radioButton3.pack()

b = tk.Button(root, text="Calculate Order", command=on_click)
b.pack()

l2 = tk.Label(root,text="")
l2.pack()
root.mainloop()