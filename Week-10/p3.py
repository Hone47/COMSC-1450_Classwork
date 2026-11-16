import tkinter as tk 

def on_click():
  x = "You have selected allergies for"
  if chk_var.get() == 1:
    x += " Vegetarian"
  if chk_var2.get() == 1:
    x += " Gluten-Free"
  if chk_var3.get() == 1:
    x+= " Nut-Free"
  l2.config(text=x)


root = tk.Tk()

root.title("Allergies List")
root.geometry("300x150")
root.config(bg="lightblue")
#value for checkbox
chk_var = tk.IntVar()
chk_var2 = tk.IntVar()
chk_var3 = tk.IntVar()

l1 = tk.Label(root, text="pick a course")
l1.pack()





checkbox = tk.Checkbutton(root, bg="lightblue", text = "Vegetarian", variable=chk_var)
checkbox.pack()
checkbox2 = tk.Checkbutton(root, bg="lightblue",text = "Gluten-Free", variable=chk_var2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(root, bg="lightblue",text = "Nut-Free", variable=chk_var3)
checkbox3.pack()

b = tk.Button(root, text="Submit", command=on_click)
b.pack()
l2 = tk.Label(root,bg="lightblue", text="")
l2.pack()
# if(chk_var and chk_var2):

root.mainloop()