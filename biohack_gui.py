# Imports
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

# Responses
responses_dict = {}

# Name
name_var = tk.StringVar()
name_label = tk.Label(root, text="1. What is your name? ")
name_label.grid(row=0, column=0)

name = tk.Entry(root, textvariable=name_var)
name.grid(row=0, column=1)
responses_dict["Name"] = name.get()

# Age
age_var = tk.StringVar()
age_label = tk.Label(root, text="What is your age? ")
age_label.grid(row=1, column=0)

age = tk.Entry(root, textvariable=age_var)
age.grid(row=1, column=1)
responses_dict["Age"] = age_var.get()

# Gender
gender_var = tk.StringVar()
gender_label = tk.Label(root, text="Choose Gender: ")
gender_label.grid(row=2, column=0)

gender = ttk.Combobox(root, values=["Male", "Female", "Other"], textvariable=gender_var)
gender.grid(row=2, column=1)
gender.set("Male") # Set default value and gender.get() for chosen value
responses_dict["Gender"] = gender.get()

# BMI
bmi_var = tk.IntVar()
bmi_label = tk.Label(root, text="What is your Body Mass Index(BMI): ")
bmi_label.grid(row=3, column=0)

bmi = tk.Entry(root, textvariable=bmi_var)
bmi.grid(row=3, column=1)
responses_dict["BMI"] = bmi_var.get()

# Other prompts
prompts = [ "Do you smoke? ",
            "Do you drink? ", 
            "Do you have high blood pressure? ",
            "What is your cholesterol level? "]

prompts_options = ["Yes", "No"]

prompt_keys = ["Blood Pressure", "Cholesterol", "Drink", "Smoke"]

prompt_vars = {}

for i, prompt in enumerate(prompts):
   my_row = 4+i
   tk.Label(root, text=prompt).grid(row=my_row, column=0)

   var = tk.StringVar()
   prompt_vars[prompt_keys[i]] = var
   combobox = ttk.Combobox(root, values=prompt_keys, textvariable=var)
   combobox.grid(row=my_row, column=1)
   combobox.set(prompts_options[1])

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = tk.Label(root, text="Do you have a history with any disease below? Check all that apply.")
diseases_label.grid(row=4+len(prompt_keys), column=0)

for i, disease in enumerate(diseases):
    selected_diseases[disease] = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=disease, variable=selected_diseases[disease])
    chk.grid(row=4 +len(prompt_keys) + i, column=0, sticky="w")
   
# Functions
def collect_responses(): #This tests all values were properly gotten
    
    responses_dict["Name"] = name_var.get()
    responses_dict["Age"] = age_var.get()
    responses_dict["Gender"] = gender_var.get()
    responses_dict["BMI"] = bmi_var.get()

    for key in prompt_keys:
       responses_dict[key] = prompt_vars[key].get()

    for disease in diseases:
     responses_dict[disease] = selected_diseases[disease].get()

    print(responses_dict)

final_vals_button = tk.Button(root, text="final values: ", command=collect_responses)
final_vals_button.grid(row=9+len(diseases), column=0, sticky='e')

root.mainloop()
