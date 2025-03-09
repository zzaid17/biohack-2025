import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class DiseasePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Prediction Model")
        self.root.geometry("570x700")
        self.root.resizable(False, False)
        self.configure_ui()
        self.create_widgets()

    def configure_ui(self):
        """Configure UI settings like colors and styles."""
        self.BG_COLOR = "#3498db"
        self.TEXT_COLOR = "#ffffff"
        self.BUTTON_COLOR = "#f39c12"
        self.BUTTON_HOVER = "#E54B5A"
        self.INPUT_BG = "#009900"
        self.INPUT_FG = "#FFFFFF"
        
        self.root.configure(bg=self.BG_COLOR)
        
        icon = Image.open("zion-tech-app-icon.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.wm_iconphoto(True, self.icon)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Poppins", 12, "bold"), background=self.BG_COLOR, foreground=self.TEXT_COLOR, padding=5)
        style.configure("TButton", font=("Poppins", 12, "bold"), background=self.BUTTON_COLOR, foreground="white", padding=8, borderwidth=2)
        style.map("TButton", background=[("active", self.BUTTON_HOVER)])
        style.configure("TEntry", font=("Poppins", 12), fieldbackground=self.INPUT_BG, foreground=self.INPUT_FG, borderwidth=2, padding=5)
        style.configure("TCheckbutton", font=("Poppins", 12), background=self.BG_COLOR, foreground=self.TEXT_COLOR, padding=5)
        style.map("TCheckbutton", background=[("active", self.BG_COLOR)])
        style.configure("Custom.TCombobox", font=("Poppins", 12), fieldbackground=self.INPUT_BG, background=self.INPUT_BG, foreground=self.INPUT_FG, arrowcolor=self.TEXT_COLOR, borderwidth=2, padding=5)

    def create_widgets(self):
        """Create and arrange widgets in the application."""
        ttk.Label(self.root, text="Disease Prediction Model", style="TLabel", font=("Poppins", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        self.name_var = tk.StringVar()
        self.create_entry("1. What is your name?", self.name_var, 1)

        self.age_var = tk.IntVar()
        self.create_entry("2. What is your age?", self.age_var, 2)

        self.gender_var = tk.StringVar()
        self.create_combobox("3. Choose gender:", ["---", "Male", "Female", "Other"], self.gender_var, 3)

        self.bmi_var = tk.IntVar()
        self.create_entry("4. What is your Body Mass Index (BMI):", self.bmi_var, 4)

        self.prompt_keys = ["Smoke", "Drink", "Blood Pressure"]
        self.prompt_vars = {}
        prompts = ["5. Do you smoke?", "6. Do you drink?", "7. Do you have high blood pressure?"]
        for i, prompt in enumerate(prompts):
            self.prompt_vars[self.prompt_keys[i]] = tk.StringVar()
            self.create_combobox(prompt, ["---", "Yes", "No"], self.prompt_vars[self.prompt_keys[i]], i + 5)
        
        self.selected_diseases = {}
        diseases = ["Cancer", "Diabetes", "Heart Diseases", "Liver Problems", "Stroke"]
        ttk.Label(self.root, text="Do you have a history with any disease below? Check all that apply.", style="TLabel").grid(row=8, column=0, columnspan=2, sticky="ew")
        self.checkbox_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.checkbox_frame.grid(row=9, column=0, columnspan=2, pady=5)
        for disease in diseases:
            self.selected_diseases[disease] = tk.BooleanVar()
            chk = ttk.Checkbutton(self.checkbox_frame, text=disease, style="TCheckbutton", variable=self.selected_diseases[disease])
            chk.pack(fill="x", anchor="w", padx=20, pady=2)
        
        ttk.Button(self.root, text="Submit Values", command=self.collect_responses, style="TButton").grid(row=10, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

    def create_entry(self, label_text, var, row):
        """Create an entry field with a label."""
        ttk.Label(self.root, text=label_text, style="TLabel").grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(self.root, textvariable=var, style="TEntry")
        entry.grid(row=row, column=1, sticky="ew", columnspan=2, pady=5)

    def create_combobox(self, label_text, values, var, row):
        """Create a combobox with a label."""
        ttk.Label(self.root, text=label_text, style="TLabel").grid(row=row, column=0, sticky="w", pady=5)
        combobox = ttk.Combobox(self.root, values=values, textvariable=var, style="Custom.TCombobox")
        combobox.grid(row=row, column=1, sticky="ew", columnspan=2)
        combobox.set(values[0])

    def collect_responses(self):
        """Collect user responses and display them in a messagebox."""
        responses_dict = {
            "Name": self.name_var.get(),
            "Age": self.age_var.get(),
            "Gender": self.gender_var.get(),
            "BMI": self.bmi_var.get(),
        }
        for key in self.prompt_keys:
            responses_dict[key] = self.prompt_vars[key].get()
        for disease, var in self.selected_diseases.items():
            responses_dict[disease] = var.get()
        messagebox.showinfo("Collected Data", f"Here are your final responses: {responses_dict}")
        self.clear_fields()

    def clear_fields(self):
        """Clear all input fields after submission."""
        self.name_var.set("")
        self.age_var.set(0)
        self.gender_var.set("---")
        self.bmi_var.set(0)
        for key in self.prompt_keys:
            self.prompt_vars[key].set("---")
        for var in self.selected_diseases.values():
            var.set(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiseasePredictionApp(root)
    root.mainloop()
