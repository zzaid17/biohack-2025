# Imports
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Color Scheme
BG_COLOR = "#1E1E2E"   # Dark Blue-Gray Background
TEXT_COLOR = "#E0E0E0" # Light Gray Text
BUTTON_COLOR = "#FF5F6D"  # Coral Red (For Main Buttons)
BUTTON_HOVER = "#E54B5A"  # Slightly Darker Coral Red
INPUT_BG = "#2A2D3E" # Dark Gray-Blue for Input Fields
INPUT_FG = "#FFFFFF" # White Text for Inputs

# GUI initialization
root = tk.Tk()
root.title("Disease Prediction Model")
root.iconbitmap("download.jpeg")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

'''
# Background Image
bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((700, 750))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=700, height=750)
canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")
#canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
'''

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Poppins", 12), background=BG_COLOR, foreground=TEXT_COLOR, padding=5)
style.configure("TButton", font=("Poppins", 12), background=BUTTON_COLOR, foreground="white", padding=5)
style.configure("TEntry", font=("Poppins", 12), background=INPUT_BG, foreground=INPUT_FG)
style.configure("TCombobox", font=("Poppins", 12), background=INPUT_BG, foreground=INPUT_FG)

'''
# Create a frame for inputs
frame = tk.Frame(root, bg="#f5f5f5", bd=2, relief="ridge")
frame_id = canvas.create_window(350, 400, window=frame, width=600, height=700, anchor="center")  # Centers it
frame.pack_propagate(False)

# Example of Adjusting Transparency (Using Label Instead of Frame)
frame_label = tk.Label(frame, text="Disease Prediction Model", font=("General Sans", 16, "bold"), bg="#ffffff", anchor="w")
frame_label.grid(row=1, column=0, pady=10)
'''

# Global font selection
LABEL_FONT = ("General Sans", 12, "bold")
ENTRY_FONT = ("General Sans", 12, "bold")
BUTTON_FONT = ("General Sans", 12,"bold")

# Responses
responses_dict = {}

#Current prompts
curr_prompts = ["Name", "Age", "BMI", "Gender"]

# Name
name_var = tk.StringVar()
name_label = tk.Label(root, text="1. What is your name? ", font=LABEL_FONT, padx=10, anchor="w", bg=BG_COLOR, fg=TEXT_COLOR)
name_label.grid(row=2, column=0, sticky="w", pady=(20,5))

name = tk.Entry(root, textvariable=name_var, font=ENTRY_FONT, bg=INPUT_BG, fg=INPUT_FG)
name.grid(row=2, column=1, sticky="ew", columnspan=2, pady=5)

# Age
age_var = tk.IntVar()
age_label = tk.Label(root, text="2. What is your age? ", font=LABEL_FONT, padx=10, anchor="w")
age_label.grid(row=3, column=0, sticky="w", pady=5)

age = tk.Entry(root, textvariable=age_var, bg=INPUT_BG, fg=INPUT_FG)
age.grid(row=3, column=1, sticky="ew", columnspan=2, pady=5)
age_var.set(0)

# Gender
gender_var = tk.StringVar()
gender_label = tk.Label(root, text="3. Choose gender: ", font=LABEL_FONT, padx=10, anchor="w")
gender_label.grid(row=4, column=0, sticky="w", pady=5)

gender_values = ["---", "Male", "Female", "Other"]

gender = ttk.Combobox(root, values=gender_values, textvariable=gender_var, bg=INPUT_BG, fg=INPUT_FG)
gender.grid(row=4, column=1, sticky="ew", columnspan=2)
gender.set(gender_values[0]) # Set default value and gender.get() for chosen value

# BMI
bmi_var = tk.IntVar()
bmi_label = tk.Label(root, text="4. What is your Body Mass Index (BMI): ", font=LABEL_FONT, padx=10, anchor="w")
bmi_label.grid(row=5, column=0, sticky="w", pady=5)

bmi = tk.Entry(root, textvariable=bmi_var, bg=INPUT_BG, fg=INPUT_FG)
bmi.grid(row=5, column=1, sticky="ew", columnspan=2, pady=5)
bmi_var.set(0)

# Other prompts
prompts = [ "5. Do you smoke? ",
            "6. Do you drink? ", 
            "7. Do you have high blood pressure? "]

prompts_options = ["---", "Yes", "No"]

prompt_keys = ["Blood Pressure", "Drink", "Smoke"]

prompt_vars = {}

curr_len = len(curr_prompts) + 2

for i, prompt in enumerate(prompts):
   curr_len = curr_len+i
   tk.Label(root, text=prompt, font=LABEL_FONT, padx=10, anchor="w").grid(row=curr_len, column=0, sticky="w", pady=5)
   var = tk.StringVar()
   prompt_vars[prompt_keys[i]] = var
   combobox = ttk.Combobox(root, values=prompts_options, textvariable=var)
   combobox.grid(row=curr_len, column=1, sticky="ew", columnspan=2)
   combobox.set(prompts_options[0])

curr_len = curr_len+len(prompt_keys)

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = tk.Label(root, text="Do you have a history with any disease below? Check all that apply.", pady=5, padx=10, anchor="center", font=LABEL_FONT)
diseases_label.grid(row=curr_len, column=0, columnspan=2, sticky="ew")

curr_len += 1

checkbox_frame = tk.Frame(root, bg=BG_COLOR)
checkbox_frame.grid(row=curr_len, column=0, columnspan=2, pady=5)

# Add Buttons to frame
for i, disease in enumerate(diseases):
    #curr_len = curr_len + i + 1
    selected_diseases[disease] = tk.BooleanVar()
    chk = tk.Checkbutton(checkbox_frame, text=disease, font=BUTTON_FONT, variable=selected_diseases[disease],
                     anchor="w", bg=BG_COLOR, fg=TEXT_COLOR, activebackground=BG_COLOR,
                     activeforeground=TEXT_COLOR, selectcolor=BG_COLOR)  # Removes white select box

    chk.pack(fill="x", anchor="w", padx=20, pady=2)
   
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

    #tk.Label(frame, text=f"{responses_dict}").grid(row = curr_len+1, column=0)
    messagebox.showinfo("Collected Data", f"Here are your final responses: {responses_dict}")

    # Clear boxes
    name_var.set("")
    age_var.set(0)
    gender_var.set()
    bmi_var.set(0)

curr_len = curr_len+1
final_vals_button = tk.Button(root, text="Submit Values", command=collect_responses, font=BUTTON_FONT, bg="blue", fg="white", padx=10, pady=5)
final_vals_button.grid(row=curr_len, column=0, sticky='ew', columnspan=3, pady=10, padx=20)

root.mainloop()
