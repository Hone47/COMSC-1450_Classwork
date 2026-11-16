import tkinter as tk 

def on_click():
   x = "You have accepted terms and conditions"
   if chk_var.get() and chk_var2.get() == 1:
     l2.config(text=x)

root = tk.Tk()

root.title("checkbox Example")
root.geometry("300x150")
root.config(bg="lightblue")
#value for checkbox
chk_var = tk.IntVar()
chk_var2 = tk.IntVar()

l1 = tk.Label(root, text="pick a course")
l1.pack()





checkbox = tk.Checkbutton(root, bg="lightblue", text = "Accept Terms & Conditions", variable=chk_var)
checkbox.pack()
checkbox2 = tk.Checkbutton(root, bg="lightblue",text = "Accept Terms & Conditions", variable=chk_var2)
checkbox2.pack()


b = tk.Button(root, text="Confirm", command=on_click)
b.pack()
l2 = tk.Label(root,bg="lightblue", text="")
l2.pack()
# if(chk_var and chk_var2):

root.mainloop()