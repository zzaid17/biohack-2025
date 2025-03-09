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
root.title("Zion Technology")
root.geometry("550x830")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

icon = Image.open("zion-tech-app-icon.png")
icon = ImageTk.PhotoImage(icon)  # Convert to Tkinter format
root.wm_iconphoto(True, icon)  # Set the icon

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

style.map("Custom.TCombobox",
    fieldbackground=[("readonly", INPUT_BG)],
    foreground=[("readonly", INPUT_FG)]
)

# Responses
responses_dict = {}

# Save Selections
personal_history = {}
family_history = {}

# Other prompts
prompts = [ "5. Do you smoke? ",
            "6. Do you drink? ", 
            "7. Do you have high blood pressure? ",
            "8. Do you have Diabetes? ",
            "9. What is your activity level? "]

prompts_options = ["---", "Yes", "No"]

prompt8_options = ["---", "Low", "Medium", "High"]

prompt_keys = ["Blood Pressure", "Drink", "Smoke", "diabetes", "Activity Level"]

prompt_vars = {}

# Functions

def clear_entry(event):
    """ Clears the entry field when the user clicks on it. """
    widget = event.widget
    if widget.get() == "0" or widget.get() == "0.0":
        widget.delete(0, tk.END)

def map_prompt(value):
    mapping = {
        "---": None,
        "Low": 0,
        "Medium": 0.5,
        "High": 1
    }
    return mapping.get(value)

popup = None

def collect_responses():
    global popup
    
    # Validation: Check if required fields are changed from default values
    if name_var.get().strip() == "":
        messagebox.showerror("Input Error", "Please enter your name.")
        return
    if age_var.get() == 0 or age_var.get() == "":
        messagebox.showerror("Input Error", "Please enter your age.")
        return
    if gender_var.get() == "---":
        messagebox.showerror("Input Error", "Please select a gender.")
        return
    if bmi_var.get() == 0.0 or bmi_var.get() == "":
        messagebox.showerror("Input Error", "Please enter your BMI.")
        return
    for key in prompt_keys:
        if prompt_vars[key].get() == "---":  # Ensuring dropdowns are changed
            messagebox.showerror("Input Error", f"Please provide an answer for {key}.")
            return
        
    if popup is not None:
        popup.destroy()
        popup = None

    # Create a new popup window
    popup = tk.Toplevel(root)
    popup.title("Collected Data")
    popup.geometry("500x400")
    popup.configure(bg=BG_COLOR)

    # Store responses in a dictionary
    responses_dict["Name"] = name_var.get()
    responses_dict["Gender"] = gender_var.get()
    responses_dict["Age"] = age_var.get() if age_var.get() != "" else 0 
    responses_dict["BMI"] = bmi_var.get() if bmi_var.get() != "" else 0.0  

    for key in prompt_keys:
        responses_dict[key] = prompt_vars[key].get()
        if key == prompt_keys[3]:   
            activity_int = map_prompt(responses_dict[key]) # map value
            print(f"User selected: {responses_dict[key]}, Mapped to: {activity_int}")

    disease_rows = []
    for disease in diseases:
        personal = "Yes" if personal_history[disease].get() else "No"
        family = "Yes" if family_history[disease].get() else "No"
        disease_rows.append(f"{disease:<20} {personal:<10} {family}")

    general_responses = "\n".join([
        f"{key}: {value}" for key, value in responses_dict.items() if "Personal" not in key and "Family" not in key
    ])

    response_text = "\n".join([
        general_responses,
        "",  # Line break before disease table
        "Disease History:",
        f"{'Disease':<20} {'Personal':<10} Family",
        "-" * 40,  # Separator line
        *disease_rows
    ])

    # Clear Entries
    name_var.set("")  
    age_var.set(0)  
    gender_var.set("---")  
    bmi_var.set(0.0)  

    for key in prompt_keys:
        prompt_vars[key].set("---")  # Reset dropdowns to default option

    # 3️⃣ Uncheck Checkboxes
    for disease in diseases:
        personal_history[disease].set(False)  # Uncheck "Personal" checkboxes
        family_history[disease].set(False)  # Uncheck "Family" checkboxes
    
    # Popup Title
    title_label = ttk.Label(popup, text="Your Submitted Responses", style="TLabel", font=("Poppins", 14, "bold"))
    title_label.pack(pady=10)

    # Create a frame to hold text + scrollbar
    frame = tk.Frame(popup, bg=BG_COLOR)
    frame.pack(fill="both", expand=True, padx=10, pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # Create a Textbox to show the responses
    text_box = tk.Text(
        popup, font=("Poppins", 12), height=15, width=50, 
        bg=INPUT_BG, fg=TEXT_COLOR, wrap="word", bd=0
    )
    
    text_box.pack(pady=5, padx=10)
  
    scrollbar.config(command=text_box.yview)

    text_box.insert(tk.END, response_text)
    text_box.config(state=tk.DISABLED)  # Prevent Editing

    # Close Button
    close_button = ttk.Button(popup, text="Close", command=popup.destroy, style="TButton")
    close_button.pack(pady=10)

def confirm_close():
    response = messagebox.askyesno("Confirm Exit", "Are you sure you want to close the application?")
    if response:  # If user clicks "Yes"
        root.destroy()

#Current prompts
curr_prompts = ["Name", "Age", "BMI", "Gender"]

# Top Label
title_label = tk.Label(root, text="Disease Prediction Model", font=("Poppins", 16, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Sub title
title_label1 = tk.Label(root, text="Please answer the questions below for a prediction.", font=("Poppins", 12), bg=BG_COLOR, fg=TEXT_COLOR)
title_label1.grid(row=1, column=0, columnspan=2, pady=10)

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
age.bind("<FocusIn>", clear_entry)

# Gender
gender_var = tk.StringVar()
gender_label = ttk.Label(root, text="3. Choose gender: ", style="TLabel")
gender_label.grid(row=4, column=0, sticky="w", pady=5)

gender_values = ["---", "Male", "Female", "Other"]

gender = ttk.Combobox(root, values=gender_values, textvariable=gender_var, style="Custom.TCombobox")
gender.grid(row=4, column=1, sticky="ew", columnspan=2)
gender.set(gender_values[0]) # Set default value and gender.get() for chosen value

# BMI
bmi_var = tk.DoubleVar()
bmi_label = ttk.Label(root, text="4. What is your Body Mass Index (BMI): ", style="TLabel")
bmi_label.grid(row=5, column=0, sticky="w", pady=5)

bmi = ttk.Entry(root, textvariable=bmi_var, style="TEntry")
bmi.grid(row=5, column=1, sticky="ew", columnspan=2, pady=5)
bmi_var.set(0.0)
bmi.bind("<FocusIn>", clear_entry)

curr_len = len(curr_prompts) + 2

for i, prompt in enumerate(prompts):
   curr_len = curr_len+i
   ttk.Label(root, text=prompt, style="TLabel").grid(row=curr_len, column=0, sticky="w", pady=5)
   var = tk.StringVar()
   prompt_vars[prompt_keys[i]] = var

   if prompt == prompts[4]:
        combobox = ttk.Combobox(root, values=prompt8_options, textvariable=var, style="Custom.TCombobox", state="readonly")
        combobox.grid(row=curr_len, column=1, sticky="ew", columnspan=2)
        combobox.set(prompt8_options[0])

        continue

   combobox = ttk.Combobox(root, values=prompts_options, textvariable=var, style="Custom.TCombobox", state="readonly")
   combobox.grid(row=curr_len, column=1, sticky="ew", columnspan=2)
   combobox.set(prompts_options[0])

curr_len = curr_len+len(prompt_keys) + 1

# Diseases 
selected_diseases = {}
diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

diseases_label = ttk.Label(root, text="Do you have a history with any disease below? Check all that apply.", style="TLabel")
diseases_label.grid(row=curr_len, column=0, columnspan=2, sticky="ew")

curr_len += 1

personal_label = ttk.Label(root, text="Personal", style="TLabel")
personal_label.grid(row=curr_len, column=0, sticky='w')

family_label = ttk.Label(root, text="Family", style="TLabel")
family_label.grid(row=curr_len, column=1, sticky='w')

curr_len += 1

'''
checkbox_frame = tk.Frame(root, bg=BG_COLOR)
checkbox_frame.grid(row=curr_len, column=0, columnspan=2, pady=5)

checkbox_frame2 = tk.Frame(root, bg=BG_COLOR)
checkbox_frame2.grid(row=curr_len, column=1, columnspan=2, pady=5)
'''
# Add Buttons to frame
i, j = 0, 0



for i, disease in enumerate(diseases):
    #curr_len = curr_len + i + 1
    #selected_diseases[disease] = tk.BooleanVar()

    personal_history[disease] = tk.BooleanVar()
    family_history[disease] = tk.BooleanVar()

    # Checkboxes
    chk_personal = ttk.Checkbutton(root, variable=personal_history[disease], 
                          text=disease, style="TCheckbutton")  # Removes white select box
    chk_personal.grid(row=curr_len, column=0, columnspan=2, sticky="w")

    chk_family = ttk.Checkbutton(root, variable=family_history[disease], 
                          text=disease, style="TCheckbutton")  # Removes white select box
    chk_family.grid(row=curr_len, column=1, sticky='w')

    curr_len += 1
    #chk.pack(fill="x", anchor="w", padx=20, pady=2)

   
curr_len = curr_len+1

final_vals_button = ttk.Button(root, text="Submit Values", command=collect_responses, style="TButton")
final_vals_button.grid(row=curr_len, column=0, sticky='ew', columnspan=3, pady=10, padx=20)

curr_len+=1
# Close Button
close_button = ttk.Button(root, text="Close", command=confirm_close, style="TButton")
close_button.grid(row=curr_len, column=0, sticky='ew', columnspan=3, pady=10, padx=20)

root.mainloop()
