# Imports
import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Widgets: Entry, Labels, Buttons, and Grids

# Name
name_label = tk.Label(root, text="What is your name? ")
name_label.grid()

name = tk.Entry(root)
name.grid()

# Age
age_var = tk.StringVar()
age_label = tk.Label(root, text="What is your age? ")
age_label.grid()

age = tk.Entry(root, age_var)
age.grid()

# Gender
gender_label = tk.Label(root, text="Choose Gender: ")
gender_label.grid()

gender = ttk.Combobox(root, values=["Male", "Female", "Other"])
gender.grid()
gender.set("Male") # Set default value and gender.get() for chosen value

# BMI
bmi_var = tk.IntVar()
bmi_label = tk.Label(root, text="What is your Body Mass Index(BMI): ")
bmi_label.grid()

bmi = tk.Entry(root, textvariable=bmi_var)
bmi.grid()

# Other prompts
prompts = [ "Do you smoke? ",
            "Do you drink? ", 
            "Do you have high blood pressure? ",
            "What is your cholesterol level? "]

prompts_options = ["Yes", "No"]

# Smoke
smoke_label = tk.Label(root, text=prompts[0])
smoke_label.grid()

smoke = ttk.Combobox(root, values=prompts_options)
smoke.grid()
smoke.set(prompts_options[0]) # Set default value and gender.get() for chosen value

# Drink
drink_label = tk.Label(root, text=prompts[1])
drink_label.grid()

drink = ttk.Combobox(root, values=prompts_options)
drink.grid()
drink.set(prompts_options[0]) # Set default value and gender.get() for chosen value

# Blood Pressure
bp_label = tk.Label(root, text=prompts[2])
bp_label.grid()

bp = ttk.Combobox(root, values=prompts_options)
bp.grid()
bp.set(prompts_options[0]) # Set default value and gender.get() for chosen value

# Cholesterol
cholesterol_label = tk.Label(root, text=prompts[3])
cholesterol_label.grid()

cholesterol = ttk.Combobox(root, values=prompts_options)
cholesterol.grid()
cholesterol.set(prompts_options[0]) # Set default value and gender.get() for chosen value

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = tk.Label(root, text="Do you have a history with any disease below? Check all that apply.")
diseases_label.grid()

for disease in diseases:
    selected_diseases[disease] = tk.BooleanVar
    chk = tk.Checkbutton(root, text=disease, variable=selected_diseases[disease])
    chk.anchor("w")

# Functions

def run_model():
    pass

root.mainloop()