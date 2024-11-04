import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from tkcalendar import Calendar
from PIL import Image, ImageTk
import random

class HealthTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker")
        self.root.geometry("1000x1000")
        
        # Default light mode
        self.is_dark_mode = False
        self.set_theme()

        # Initialize health-related variables
        self.steps = tk.IntVar()
        self.water = tk.DoubleVar()
        self.sleep = tk.DoubleVar()
        self.doctor_name = tk.StringVar()
        self.medical_records = ""

        # BMI variables
        self.weight = tk.DoubleVar()
        self.height = tk.DoubleVar()

        # Totals
        self.total_steps = 0
        self.total_water = 0.0
        self.total_sleep = 0.0

        # Recommended amounts
        self.recommended_steps = 10000
        self.recommended_water = 2.0
        self.recommended_sleep = 8.0

        # Daily health tips
        self.health_tips = [
            "Stay hydrated! Drink at least 8 cups of water daily.",
            "Aim for 7-8 hours of sleep each night for optimal health.",
            "Take a short walk after meals to aid digestion.",
            "Incorporate fruits and vegetables into your diet.",
            "Limit screen time before bed for better sleep."
        ]
        
        # Create the UI
        self.create_widgets()

    def set_theme(self):
        # Define colors for light and dark mode
        if self.is_dark_mode:
            self.root.config(bg="#2e2e2e")
            self.bg_color = "#2e2e2e"
            self.text_color = "#f0f4f7"
        else:
            self.root.config(bg="#f0f4f7")
            self.bg_color = "#f0f4f7"
            self.text_color = "#000000"

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.set_theme()
        self.update_ui_theme()

    def update_ui_theme(self):
        # Update all widget themes based on current mode
        self.root.config(bg=self.bg_color)
        for widget in self.root.winfo_children():
            widget.config(bg=self.bg_color)
            if isinstance(widget, ttk.Label):
                widget.config(foreground=self.text_color)

    def create_widgets(self):
        # Dark mode toggle
        self.dark_mode_button = ttk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=0, column=0, columnspan=2, pady=10)

        # Daily Health Tip
        daily_tip = random.choice(self.health_tips)
        self.tip_label = ttk.Label(self.root, text="Health Tip: " + daily_tip, font=("Helvetica", 10, "italic"), wraplength=400)
        self.tip_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Load and display the logo
        try:
            logo_image = Image.open("logo.png")  # Replace with your logo file name
            logo_image = logo_image.resize((100, 100), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_image)
            logo_label = ttk.Label(self.root, image=self.logo, background=self.bg_color)
            logo_label.grid(row=2, column=0, columnspan=2, pady=10)
        except Exception as e:
            print(f"Logo not found: {e}")

        # Steps
        ttk.Label(self.root, text="Steps:").grid(row=3, column=0, padx=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.steps).grid(row=3, column=1, padx=10)
        ttk.Button(self.root, text="Add Steps", command=self.add_steps).grid(row=3, column=2, padx=10)

        # Water Intake
        ttk.Label(self.root, text="Water (liters):").grid(row=4, column=0, padx=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.water).grid(row=4, column=1, padx=10)
        ttk.Button(self.root, text="Add Water", command=self.add_water).grid(row=4, column=2, padx=10)

        # Sleep
        ttk.Label(self.root, text="Sleep (hours):").grid(row=5, column=0, padx=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.sleep).grid(row=5, column=1, padx=10)
        ttk.Button(self.root, text="Add Sleep", command=self.add_sleep).grid(row=5, column=2, padx=10)

        # Show Summary
        ttk.Button(self.root, text="Show Summary", command=self.show_summary).grid(row=6, column=0, columnspan=3, pady=10)

        # Appointment Scheduling
        ttk.Label(self.root, text="Select Doctor:").grid(row=7, column=0, padx=10, sticky="e")
        doctors = ['Dr. Smith', 'Dr. Johnson', 'Dr. Lee']
        self.doctor_dropdown = ttk.Combobox(self.root, textvariable=self.doctor_name, values=doctors)
        self.doctor_dropdown.grid(row=7, column=1, padx=10)

        ttk.Label(self.root, text="Select Appointment Date:").grid(row=8, column=0, padx=10, sticky="e")
        self.cal = Calendar(self.root, selectmode='day', date_pattern='y-mm-dd')
        self.cal.grid(row=8, column=1, padx=10)

        ttk.Button(self.root, text="Schedule Appointment", command=self.schedule_appointment).grid(row=8, column=2, padx=10)

        # Upload Medical Records
        ttk.Button(self.root, text="Upload Medical Records", command=self.upload_records).grid(row=9, column=0, columnspan=3, pady=10)

        # AI Assistant
        ttk.Label(self.root, text="Describe your symptoms:").grid(row=10, column=0, padx=10, sticky="e")
        self.symptom_input = tk.Text(self.root, height=4, width=40)
        self.symptom_input.grid(row=10, column=1, padx=10)
        ttk.Button(self.root, text="Get Advice", command=self.get_advice).grid(row=10, column=2, padx=10)

        # BMI Calculator
        ttk.Label(self.root, text="BMI Calculator", font=("Helvetica", 14, "bold")).grid(row=11, column=0, columnspan=3, pady=10)
        
        ttk.Label(self.root, text="Weight (kg):").grid(row=12, column=0, padx=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.weight).grid(row=12, column=1, padx=10)

        ttk.Label(self.root, text="Height (cm):").grid(row=13, column=0, padx=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.height).grid(row=13, column=1, padx=10)

        ttk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi).grid(row=14, column=0, columnspan=3, pady=10)

    def add_steps(self):
        steps = self.steps.get()
        self.total_steps += steps
        messagebox.showinfo("Info", f"Added {steps} steps. Total steps: {self.total_steps}")

    def add_water(self):
        water = self.water.get()
        self.total_water += water
        messagebox.showinfo("Info", f"Added {water} liters of water. Total water: {self.total_water} liters")

    def add_sleep(self):
        sleep = self.sleep.get()
        self.total_sleep += sleep
        messagebox.showinfo("Info", f"Added {sleep} hours of sleep. Total sleep: {self.total_sleep} hours")

    def show_summary(self):
        steps_comparison = "✓" if self.total_steps >= self.recommended_steps else "✗"
        water_comparison = "✓" if self.total_water >= self.recommended_water else "✗"
        sleep_comparison = "✓" if self.total_sleep >= self.recommended_sleep else "✗"

        summary = (
            f"Total steps: {self.total_steps} (Recommended: {self.recommended_steps}) [{steps_comparison}]\n"
            f"Total water intake: {self.total_water} liters (Recommended: {self.recommended_water} liters) [{water_comparison}]\n"
            f"Total sleep: {self.total_sleep} hours (Recommended: {self.recommended_sleep} hours) [{sleep_comparison}]"
        )
        messagebox.showinfo("Health Summary", summary)

    def get_advice(self):
        symptoms = self.symptom_input.get("1.0", tk.END).strip()
        if symptoms:
            advice = self.generate_advice(symptoms)
            messagebox.showinfo("AI Assistant Advice", advice)
        else:
            messagebox.showwarning("Warning", "Please enter your symptoms.")

    def generate_advice(self, symptoms):
        symptoms = symptoms.lower()
        advice = []

        symptom_dict = {
            "headache": "For headaches, try resting in a dark room and staying hydrated. If the pain persists, consider consulting a doctor.",
            "fever": "For a fever, rest and drink plenty of fluids. If the fever exceeds 101°F, seek medical attention.",
            "cough": "For a cough, stay hydrated and consider using a humidifier. If it lasts more than a week, consult a doctor.",
            "nausea": "For nausea, try ginger tea and avoid heavy meals. If it persists, see a healthcare provider.",
            "fatigue": "For fatigue, ensure you are getting enough sleep and nutrition. If extreme, consult a doctor.",
            "sore throat": "For a sore throat, warm salt water gargles and staying hydrated can help. Consult a doctor if it persists.",
            "runny nose": "For a runny nose, try antihistamines and keep hydrated. If symptoms worsen, see a healthcare professional."
        }

        for symptom, suggestion in symptom_dict.items():
            if symptom in symptoms:
                advice.append(suggestion)

        if not advice:
            advice.append("I cannot provide specific advice for those symptoms. Please consult a healthcare professional.")

        return "\n".join(advice)

    def schedule_appointment(self):
        doctor = self.doctor_name.get()
        date = self.cal.get_date()
        messagebox.showinfo("Appointment Scheduled", f"Appointment with {doctor} on {date}.")

    def upload_records(self):
        file_path = filedialog.askopenfilename(title="Select Medical Record File")
        if file_path:
            self.medical_records = file_path
            messagebox.showinfo("Success", f"Uploaded medical records from {file_path}.")

    def calculate_bmi(self):
        weight = self.weight.get()
        height = self.height.get() / 100  # convert height from cm to meters
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            interpretation = self.interpret_bmi(bmi)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {interpretation}")
        else:
            messagebox.showwarning("Input Error", "Please enter valid weight and height values.")

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()
