# Imports
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Color Scheme
BG_COLOR = "#3498db"   # Dark Blue-Gray Background
TEXT_COLOR = "#ffffff" # Light Gray Text
BUTTON_COLOR = "#f39c12"  # Coral Red (For Main Buttons)
BUTTON_HOVER = "#E54B5A"  # Slightly Darker Coral Red
INPUT_BG = "#009900" # Dark Gray-Blue for Input Fields
INPUT_FG = "#FFFFFF" # White Text for Inputs

# GUI initialization
root = tk.Tk()
root.title("Disease Prediction Model")
root.geometry("570x700")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

icon = Image.open("zion-tech-app-icon.png")
icon = ImageTk.PhotoImage(icon)  # Convert to Tkinter format
root.wm_iconphoto(True, icon)  # Set the icon

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
style.theme_use("clam")

# Label Style
style.configure(
    "TLabel",
    font=("Poppins", 12, "bold"),
    background=BG_COLOR,
    foreground=TEXT_COLOR,
    padding=5
)

# Button Style
style.configure(
    "TButton",
    font=("Poppins", 12, "bold"),
    background=BUTTON_COLOR,
    foreground="white",
    padding=8,
    borderwidth=2
)
style.map("TButton", background=[("active", BUTTON_HOVER)])  # Hover Effect

# Entry Style (Textboxes)
style.configure(
    "TEntry",
    font=("Poppins", 12),
    fieldbackground=INPUT_BG,  # Textbox background
    foreground=INPUT_FG,       # Text color
    borderwidth=2,
    padding=5
)

# Checkbox Style
style.configure(
    "TCheckbutton",
    font=("Poppins", 12),
    background=BG_COLOR,
    foreground=TEXT_COLOR,
    padding=5
)
style.map("TCheckbutton", background=[("active", BG_COLOR)])  # Ensures no color change on hover

style.configure(
    "Custom.TCombobox",
    font=("Poppins", 12),
    fieldbackground=INPUT_BG,  # Background inside the combobox
    background=INPUT_BG,       # Background of the dropdown
    foreground=INPUT_FG,       # Text color
    arrowcolor=TEXT_COLOR,     # Dropdown arrow color
    borderwidth=2,
    padding=5
)

'''
# Create a frame for inputs
frame = tk.Frame(root, bg="#f5f5f5", bd=2, relief="ridge")
frame_id = canvas.create_window(350, 400, window=frame, width=600, height=700, anchor="center")  # Centers it
frame.pack_propagate(False)

# Example of Adjusting Transparency (Using Label Instead of Frame)
frame_label = tk.Label(frame, text="Disease Prediction Model", font=("General Sans", 16, "bold"), bg="#ffffff", anchor="w")
frame_label.grid(row=1, column=0, pady=10)
'''
'''
# Global font selection
LABEL_FONT = ("General Sans", 12, "bold")
ENTRY_FONT = ("General Sans", 12, "bold")
BUTTON_FONT = ("General Sans", 12,"bold")
'''

# Responses
responses_dict = {}

#Current prompts
curr_prompts = ["Name", "Age", "BMI", "Gender"]

# Top Label
title_label = tk.Label(root, text="Disease Prediction Model", font=("Poppins", 16, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Name
name_var = tk.StringVar()
name_label = ttk.Label(root, text="1. What is your name? ", style="TLabel")
name_label.grid(row=2, column=0, sticky="w", pady=(20,5))

name = ttk.Entry(root, textvariable=name_var, style="TEntry")
name.grid(row=2, column=1, sticky="ew", columnspan=2, pady=5)

# Age
age_var = tk.IntVar()
age_label = ttk.Label(root, text="2. What is your age? ", style="TLabel")
age_label.grid(row=3, column=0, sticky="w", pady=5)

age = ttk.Entry(root, textvariable=age_var, style="TEntry")
age.grid(row=3, column=1, sticky="ew", columnspan=2, pady=5)
age_var.set(0)

# Gender
gender_var = tk.StringVar()
gender_label = ttk.Label(root, text="3. Choose gender: ", style="TLabel")
gender_label.grid(row=4, column=0, sticky="w", pady=5)

gender_values = ["---", "Male", "Female", "Other"]

gender = ttk.Combobox(root, values=gender_values, textvariable=gender_var, style="Custom.TCombobox")
gender.grid(row=4, column=1, sticky="ew", columnspan=2)
gender.set(gender_values[0]) # Set default value and gender.get() for chosen value

# BMI
bmi_var = tk.IntVar()
bmi_label = ttk.Label(root, text="4. What is your Body Mass Index (BMI): ", style="TLabel")
bmi_label.grid(row=5, column=0, sticky="w", pady=5)

bmi = ttk.Entry(root, textvariable=bmi_var, style="TEntry")
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
   ttk.Label(root, text=prompt, style="TLabel").grid(row=curr_len, column=0, sticky="w", pady=5)
   var = tk.StringVar()
   prompt_vars[prompt_keys[i]] = var
   combobox = ttk.Combobox(root, values=prompts_options, textvariable=var, style="Custom.TCombobox")
   combobox.grid(row=curr_len, column=1, sticky="ew", columnspan=2)
   combobox.set(prompts_options[0])

curr_len = curr_len+len(prompt_keys) +1

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = ttk.Label(root, text="Do you have a history with any disease below? Check all that apply.", style="TLabel")
diseases_label.grid(row=curr_len, column=0, columnspan=2, sticky="ew")

curr_len += 1

checkbox_frame = tk.Frame(root, bg=BG_COLOR)
checkbox_frame.grid(row=curr_len, column=0, columnspan=2, pady=5)

# Add Buttons to frame
for i, disease in enumerate(diseases):
    #curr_len = curr_len + i + 1
    selected_diseases[disease] = tk.BooleanVar()
    chk = ttk.Checkbutton(checkbox_frame, variable=selected_diseases[disease], 
                          text=disease, style="TCheckbutton")  # Removes white select box

    chk.pack(fill="x", anchor="w", padx=20, pady=2)
   
# Functions

def collect_responses():  
    # Store responses in a dictionary
    responses_dict["Name"] = name_var.get()
    responses_dict["Age"] = age_var.get()
    responses_dict["Gender"] = gender_var.get()
    responses_dict["BMI"] = bmi_var.get()

    for key in prompt_keys:
        responses_dict[key] = prompt_vars[key].get()

    for disease in diseases:
        responses_dict[disease] = "Yes" if selected_diseases[disease].get() else "No"

    # Create a new popup window
    popup = tk.Toplevel(root)
    popup.title("Collected Data")
    popup.geometry("500x400")
    popup.configure(bg=BG_COLOR)
    
    # Popup Title
    title_label = ttk.Label(popup, text="Your Submitted Responses", style="TLabel", font=("Poppins", 14, "bold"))
    title_label.pack(pady=10)

    # Format the response text
    response_text = "\n".join([f"{key}: {value}" for key, value in responses_dict.items()])

    # Create a Textbox to show the responses
    text_box = tk.Text(
        popup, font=("Poppins", 12), height=15, width=50, 
        bg=INPUT_BG, fg=TEXT_COLOR, wrap="word", bd=0
    )
    text_box.insert(tk.END, response_text)
    text_box.pack(pady=5, padx=10)
    text_box.config(state=tk.DISABLED)  # Prevent Editing

    # Close Button
    close_button = ttk.Button(popup, text="Close", command=popup.destroy, style="TButton")
    close_button.pack(pady=10)

def confirm_close():
    response = messagebox.askyesno("Confirm Exit", "Are you sure you want to close the application?")
    if response:  # If user clicks "Yes"
        root.destroy()

curr_len = curr_len+1

final_vals_button = ttk.Button(root, text="Submit Values", command=collect_responses, style="TButton")
final_vals_button.grid(row=curr_len, column=0, sticky='ew', columnspan=3, pady=10, padx=20)

curr_len+=1
# Close Button
close_button = ttk.Button(root, text="Close", command=confirm_close, style="TButton")
close_button.grid(row=curr_len, column=0, sticky='ew', columnspan=3, pady=10, padx=20)

root.mainloop()
