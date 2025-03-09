# Imports
import tkinter as tk
from tkinter import ttk, messagebox

# GUI initialization
root = tk.Tk()
root.title("BioHack 2025")
root.iconbitmap("download.jpeg")
root.geometry("550x400")
root.resizable(False, False)

# Global font selection
LABEL_FONT = ("Arial", 10, "bold")
ENTRY_FONT = ("Arial", 10, "bold")
BUTTON_FONT = ("Arial", 10, "bold")

# Responses
responses_dict = {}

#Current prompts
curr_prompts = ["Name", "Age", "BMI", "Gender"]

# Name
name_var = tk.StringVar()
name_label = tk.Label(root, text="1. What is your name? ")
name_label.grid(row=0, column=0, sticky="w")

name = tk.Entry(root, textvariable=name_var)
name.grid(row=0, column=1, columnspan=2)

# Age
age_var = tk.StringVar()
age_label = tk.Label(root, text="2. What is your age? ")
age_label.grid(row=1, column=0, sticky="w")

age = tk.Entry(root, textvariable=age_var)
age.grid(row=1, column=1, sticky="ew", columnspan=2)

# Gender
gender_var = tk.StringVar()
gender_label = tk.Label(root, text="3. Choose Gender: ")
gender_label.grid(row=2, column=0, sticky="w")

gender = ttk.Combobox(root, values=["Male", "Female", "Other"], textvariable=gender_var)
gender.grid(row=2, column=1, sticky="ew", columnspan=2)
gender.set("Male") # Set default value and gender.get() for chosen value

# BMI
bmi_var = tk.IntVar()
bmi_label = tk.Label(root, text="4. What is your Body Mass Index(BMI): ")
bmi_label.grid(row=3, column=0, sticky="w")

bmi = tk.Entry(root, textvariable=bmi_var)
bmi.grid(row=3, column=1, sticky="ew", columnspan=2)

# Other prompts
prompts = [ "5. Do you smoke? ",
            "6. Do you drink? ", 
            "7. Do you have high blood pressure? "]

prompts_options = ["Yes", "No"]

prompt_keys = ["Blood Pressure", "Drink", "Smoke"]

prompt_vars = {}

curr_len = len(curr_prompts)

for i, prompt in enumerate(prompts):
   curr_len = curr_len+i
   tk.Label(root, text=prompt).grid(row=curr_len, column=0, sticky="w")
   var = tk.StringVar()
   prompt_vars[prompt_keys[i]] = var
   combobox = ttk.Combobox(root, values=prompts_options, textvariable=var)
   combobox.grid(row=curr_len, column=1, sticky="ew", columnspan=2)
   combobox.set(prompts_options[1])

curr_len = curr_len+len(prompt_keys)

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = tk.Label(root, text="Do you have a history with any disease below? Check all that apply.")
diseases_label.grid(row=curr_len, column=0, sticky="w")

for i, disease in enumerate(diseases):
    curr_len = curr_len + i
    selected_diseases[disease] = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=disease, variable=selected_diseases[disease])
    chk.grid(row=curr_len, column=0, sticky="ew", columnspan=2)
   
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

    #tk.Label(root, text=f"{responses_dict}").grid(row = curr_len+1, column=0)
    messagebox.showinfo("Collected Data", f"Here are your final responses: {responses_dict}")

curr_len = curr_len+1
final_vals_button = tk.Button(root, text="final values: ", command=collect_responses)
final_vals_button.grid(row=curr_len, column=0, sticky='ew', columnspan=2)

root.mainloop()
