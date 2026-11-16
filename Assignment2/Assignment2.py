import tkinter as tk 
from tkinter import messagebox


root = tk.Tk()

root.title("Personal Health & Travel Assistant")
root.geometry("500x400")



def reset_logs():
  with open("user_logs.txt", "w") as file:
        pass

  systemStatusLabel.config(
      text="System Activity Logs Reset Successfully!",
      fg="dark green"
    )

def calculate_fare():
  if baseFlightPrice.get()  == "":
    messagebox.showwarning("Error","Base ticket price is required")
  else:
    try:
      total = 0
      base = int(baseFlightPrice.get())
      if baggageVal.get() == 1:
          total += 35
      if inflightmealVal.get() == 1:
          total += 15

      if priorityVal.get() == 1:
          total += 20
      total += base
      total = round(total, 2)
      fareresultLabel.config(text = f"[FLIGHT]Base : {base}| Total Fare: {total}")
      with open("user_logs.txt", "a") as file:
        file.write(f"[FLIGHT]Base : {base}| Total Fare: {total}")
    except:
      messagebox.showwarning("Error","Please enter a numeric base price!")

def show_page(frame_to_show):
  '''Hides all application pages, then packs the chosen one.'''
  fitness_page.pack_forget()
  flight_page.pack_forget()
  frame_to_show.pack(fill="both", expand=True, padx=20, pady=20)
  #centered version
  # frame_to_show.pack(anchor="center", expand=True, padx=20, pady=20)


def log_workout():
  radio = radioVal.get()
  act =  activityEnt.get()
  duration = durationEnt.get()
  
  if(duration =="" or act ==""):
    messagebox.showwarning("Error","Input a Value")
    return
  else:
    if radio == "low":
      result = int(duration) * 5
    elif radio == "medium":
      result = int(duration) * 8
    elif radio == "high":
      result = int(duration) * 12
  resultLabel.config(text = f"Logged: {act} for {result} Calories")
  with open("user_logs.txt", "a") as file:
    file.write(f"[FITNESS] Activity: {act} | Calories Burned: {result}\n")
   

fitness_page = tk.Frame(root)

label = tk.Label(fitness_page, text='Fitness')
label.grid(pady=5)

activityLab = tk.Label(fitness_page,text ='Activity Name (e.g., /n"Running" )')
activityLab.grid()
activityEnt = tk.Entry(fitness_page)
activityEnt.grid()

durationLab = tk.Label(fitness_page,text= 'Duration (Minutes)')
durationLab.grid()
durationEnt =tk.Entry(fitness_page)
durationEnt.grid()


radioVal = tk.StringVar(value="low")
radioButton = tk.Radiobutton(fitness_page, text = "Low", variable=radioVal, value="low")
radioButton.grid()
radioButton2 = tk.Radiobutton(fitness_page, text = "Medium", variable=radioVal, value="medium")
radioButton2.grid()
radioButton3 = tk.Radiobutton(fitness_page, text = "High", variable=radioVal, value="high")
radioButton3.grid()

log_workout = tk.Button(fitness_page, command= log_workout, text="Submit", width=10)
log_workout.grid()
resultLabel = tk.Label(fitness_page, text="")
resultLabel.grid()





flight_page = tk.Frame(root)
label = tk.Label(flight_page, text='Base Ticket Price ($)')
label.grid(pady=5)
baseFlightPrice = tk.Entry(flight_page)
baseFlightPrice.grid()

baggageVal = tk.IntVar(value = 0)
inflightmealVal = tk.IntVar(value = 0)
priorityVal = tk.IntVar(value = 0)

checkbaggage = tk.Checkbutton(flight_page, text="Checked Baggage (Adds $35.00)", variable=baggageVal)
checkbaggage.grid()
checkFlightMeal = tk.Checkbutton(flight_page, text="In-Flight Meal (Adds $15.00)", variable=inflightmealVal)
checkFlightMeal.grid()
checkPriority = tk.Checkbutton(flight_page, text="Priority Boarding (Adds $20.00)", variable=priorityVal)
checkPriority.grid()

calcFare = tk.Button(flight_page, command= calculate_fare, text="Submit", width=10)
calcFare.grid()
fareresultLabel = tk.Label(
    flight_page,
    text="",
    font=("", 12, "bold")
)
fareresultLabel.grid()


main_menubar = tk.Menu(root)
file_dropdown = tk.Menu(main_menubar, tearoff=0)
file_dropdown.add_command(label="Reset Activity Logs", command=reset_logs)
file_dropdown.add_command(label="Exit Program", command=root.quit)
file_dropdown.add_separator()
file_dropdown.add_command(label="Fitness Tracker", command=lambda:show_page(fitness_page))
file_dropdown.add_command(label="Flight Fare Estimator", command=lambda:show_page(flight_page))
main_menubar.add_cascade(label="File", menu=file_dropdown)
root.config(menu=main_menubar)


show_page(fitness_page)

systemStatusLabel = tk.Label(root,text="")
systemStatusLabel.pack() 


root.mainloop()