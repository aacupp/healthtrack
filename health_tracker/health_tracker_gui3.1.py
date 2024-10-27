import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar
from PIL import Image, ImageTk

class HealthTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker")
        self.root.geometry("600x600")
        self.root.config(bg="#f0f4f7")

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self.root, bg="#f0f4f7")
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Configure the scrollable frame
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind mouse wheel scrolling
        self.root.bind_all("<MouseWheel>", self.on_mouse_wheel)  # Windows
        self.root.bind_all("<Button-4>", self.on_mouse_wheel)  # Linux
        self.root.bind_all("<Button-5>", self.on_mouse_wheel)  # Linux

        # Initialize variables
        self.steps = tk.IntVar()
        self.water = tk.DoubleVar()
        self.sleep = tk.DoubleVar()
        self.doctor_name = tk.StringVar()
        self.medical_records = ""

        # Totals
        self.total_steps = 0
        self.total_water = 0.0
        self.total_sleep = 0.0

        # Recommended amounts
        self.recommended_steps = 10000
        self.recommended_water = 2.0
        self.recommended_sleep = 8.0

        # Create the UI
        self.create_widgets()

    def create_widgets(self):
        # Load and display the logo
        logo_image = Image.open("logo.png")  # Replace with your logo file name
        logo_image = logo_image.resize((100, 100), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(self.scrollable_frame, image=self.logo, background="#f0f4f7")
        logo_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Style configuration
        style = ttk.Style()
        style.configure("TLabel", background="#f0f4f7", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 10))

        # Steps
        ttk.Label(self.scrollable_frame, text="Steps:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(self.scrollable_frame, textvariable=self.steps).grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.scrollable_frame, text="Add Steps", command=self.add_steps).grid(row=1, column=2, padx=10, pady=5)

        # Water Intake
        ttk.Label(self.scrollable_frame, text="Water (liters):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(self.scrollable_frame, textvariable=self.water).grid(row=2, column=1, padx=10, pady=5)
        ttk.Button(self.scrollable_frame, text="Add Water", command=self.add_water).grid(row=2, column=2, padx=10, pady=5)

        # Sleep
        ttk.Label(self.scrollable_frame, text="Sleep (hours):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(self.scrollable_frame, textvariable=self.sleep).grid(row=3, column=1, padx=10, pady=5)
        ttk.Button(self.scrollable_frame, text="Add Sleep", command=self.add_sleep).grid(row=3, column=2, padx=10, pady=5)

        # Show Summary
        ttk.Button(self.scrollable_frame, text="Show Summary", command=self.show_summary).grid(row=4, column=0, columnspan=3, pady=20)

        # Appointment Scheduling
        ttk.Label(self.scrollable_frame, text="Select Doctor:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        doctors = ['Dr. Smith', 'Dr. Johnson', 'Dr. Lee']
        self.doctor_dropdown = ttk.Combobox(self.scrollable_frame, textvariable=self.doctor_name, values=doctors)
        self.doctor_dropdown.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self.scrollable_frame, text="Select Appointment Date:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.cal = Calendar(self.scrollable_frame, selectmode='day', date_pattern='y-mm-dd')
        self.cal.grid(row=6, column=1, padx=10, pady=5)
        ttk.Button(self.scrollable_frame, text="Schedule Appointment", command=self.schedule_appointment).grid(row=6, column=2, padx=10, pady=5)

        # Upload Medical Records
        ttk.Button(self.scrollable_frame, text="Upload Medical Records", command=self.upload_records).grid(row=7, column=0, columnspan=3, pady=20)

        # AI Assistant
        ttk.Label(self.scrollable_frame, text="Describe your symptoms:").grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.symptom_input = tk.Text(self.scrollable_frame, height=4, width=40)
        self.symptom_input.grid(row=8, column=1, padx=10, pady=5)
        ttk.Button(self.scrollable_frame, text="Get Advice", command=self.get_advice).grid(row=8, column=2, padx=10, pady=5)

    def on_mouse_wheel(self, event):
        # Scroll the canvas
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

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
        # Simple keyword-based advice (this is just an example)
        if "headache" in symptoms.lower():
            return "For headaches, try resting in a dark room and staying hydrated. If the pain persists, consider consulting a doctor."
        elif "fever" in symptoms.lower():
            return "For a fever, rest and drink plenty of fluids. If the fever exceeds 101°F, seek medical attention."
        elif "cough" in symptoms.lower():
            return "For a cough, stay hydrated and consider using a humidifier. If it lasts more than a week, consult a doctor."
        else:
            return "I cannot provide specific advice for those symptoms. Please consult a healthcare professional."

    def schedule_appointment(self):
        doctor = self.doctor_name.get()
        date = self.cal.get_date()
        messagebox.showinfo("Appointment Scheduled", f"Appointment with {doctor} on {date}.")

    def upload_records(self):
        file_path = filedialog.askopenfilename(title="Select Medical Record File")
        if file_path:
            self.medical_records = file_path
            messagebox.showinfo("Success", f"Uploaded medical records from {file_path}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()
