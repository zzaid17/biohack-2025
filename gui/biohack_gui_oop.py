import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from functions import get_disease_risk

class DiseasePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zion Technology")
        self.root.geometry("550x830")
        self.root.resizable(False, False)
        self.root.configure(bg="#3498db")  # Dark Blue-Gray Background

        # Load Icon
        icon = Image.open("gui/zion-tech-app-icon.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.wm_iconphoto(True, self.icon)

        # Define Variables
        self.responses_dict = {}
        self.personal_history = {}
        self.family_history = {}
        self.prompt_vars = {}
        self.popup = None

        # Define Prompts
        self.prompts = ["5. Do you smoke?", "6. Do you drink?", "7. Do you have high blood pressure?", "8. Do you have Diabetes?", "9. What is your activity level?"]
        self.prompts_options = ["---", "Yes", "No"]
        self.prompt8_options = ["---", "Low", "Medium", "High"]
        self.prompt_keys = ["Blood Pressure", "Drink", "Smoke", "diabetes", "Activity Level"]
        self.diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]

        # Create GUI
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        """ Setup Tkinter Styles """
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", font=("Poppins", 12, "bold"), background="#3498db", foreground="#ffffff", padding=5)
        style.configure("TButton", font=("Poppins", 12, "bold"), background="#f39c12", foreground="white", padding=8, borderwidth=2)
        style.map("TButton", background=[("active", "#E54B5A")])

        style.configure("TEntry", font=("Poppins", 12), fieldbackground="#009900", foreground="#FFFFFF", borderwidth=2, padding=5)

        style.configure("TCheckbutton", font=("Poppins", 12), background="#3498db", foreground="#ffffff", padding=5)
        style.map("TCheckbutton", background=[("active", "#3498db")])

        style.configure("Custom.TCombobox", font=("Poppins", 12), fieldbackground="#009900", background="#009900", foreground="#FFFFFF", arrowcolor="#ffffff", borderwidth=2, padding=5)
        style.map("Custom.TCombobox", fieldbackground=[("readonly", "#009900")], foreground=[("readonly", "#FFFFFF")])

    def create_widgets(self):
        """ Create the main GUI components """
        tk.Label(self.root, text="Disease Prediction Model", font=("Poppins", 16, "bold"), bg="#3498db", fg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Please answer the questions below for a prediction.", font=("Poppins", 12), bg="#3498db", fg="#ffffff").grid(row=1, column=0, columnspan=2, pady=10)

        # Input Fields
        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar(value=0)
        self.gender_var = tk.StringVar(value="---")
        self.bmi_var = tk.DoubleVar(value=0.0)

        self.create_entry("1. What is your name?", self.name_var, 2)
        self.create_entry("2. What is your age?", self.age_var, 3, num=True)
        self.create_combobox("3. Choose gender:", ["---", "Male", "Female", "Other"], self.gender_var, 4)
        self.create_entry("4. What is your Body Mass Index (BMI):", self.bmi_var, 5, num=True)

        # Prompt Questions
        row_index = 6
        for i, prompt in enumerate(self.prompts):
            ttk.Label(self.root, text=prompt, style="TLabel").grid(row=row_index, column=0, sticky="w", pady=5)
            var = tk.StringVar(value="---")
            self.prompt_vars[self.prompt_keys[i]] = var
            self.create_combobox("", self.prompt8_options if prompt == self.prompts[-1] else self.prompts_options, var, row_index)
            row_index += 1

        # Disease Checkboxes
        self.create_checkboxes(row_index)

        # Buttons
        row_index += len(self.diseases) + 2
        ttk.Button(self.root, text="Submit Values", command=self.collect_responses, style="TButton").grid(row=row_index, column=0, columnspan=2, pady=10)
        row_index += 1
        ttk.Button(self.root, text="Close", command=self.root.quit, style="TButton").grid(row=row_index, column=0, columnspan=2, pady=10)

    def create_entry(self, label_text, var, row, num=False):
        ttk.Label(self.root, text=label_text, style="TLabel").grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(self.root, textvariable=var, style="TEntry")
        entry.grid(row=row, column=1, sticky="ew", pady=5)
        if num:
            entry.bind("<FocusIn>", lambda event: self.clear_entry(event, var))

    def create_combobox(self, label_text, options, var, row):
        if label_text:
            ttk.Label(self.root, text=label_text, style="TLabel").grid(row=row, column=0, sticky="w", pady=5)
        combobox = ttk.Combobox(self.root, values=options, textvariable=var, style="Custom.TCombobox", state="readonly")
        combobox.grid(row=row, column=1, sticky="ew", pady=5)

    def create_checkboxes(self, row):
        ttk.Label(self.root, text="Do you have a history with any disease below? Check all that apply.", style="TLabel").grid(row=row, column=0, columnspan=2, sticky="ew")
        row += 1
        for disease in self.diseases:
            self.personal_history[disease] = tk.BooleanVar()
            self.family_history[disease] = tk.BooleanVar()
            ttk.Checkbutton(self.root, variable=self.personal_history[disease], text=disease, style="TCheckbutton").grid(row=row, column=0, sticky="w")
            ttk.Checkbutton(self.root, variable=self.family_history[disease], text=disease, style="TCheckbutton").grid(row=row, column=1, sticky="w")
            row += 1

    def clear_entry(self, event, var):
        if isinstance(var.get(), (int, float)) and var.get() in (0, 0.0):
            event.widget.delete(0, tk.END)

    def collect_responses(self):
        """ Collect responses and display them in a popup """
        if self.popup:
            self.popup.destroy()
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Collected Data")
        self.popup.geometry("500x400")
        self.popup.configure(bg="#3498db")

        responses_text = "\n".join(f"{key}: {var.get()}" for key, var in self.prompt_vars.items())
        text_box = tk.Text(self.popup, font=("Poppins", 12), height=15, width=50, bg="#009900", fg="#FFFFFF", wrap="word", bd=0)
        text_box.insert(tk.END, responses_text)
        text_box.config(state=tk.DISABLED)
        text_box.pack(pady=5, padx=10)

        ttk.Button(self.popup, text="Close", command=self.popup.destroy, style="TButton").pack(pady=10)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = DiseasePredictionApp(root)
    root.mainloop()
