import tkinter as tk
from tkinter import messagebox

class HealthTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker")

        # Initialize variables
        self.steps = tk.IntVar()
        self.water = tk.DoubleVar()
        self.sleep = tk.DoubleVar()

        # Create the UI
        self.create_widgets()

    def create_widgets(self):
        # Steps
        tk.Label(self.root, text="Steps:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.steps).grid(row=0, column=1)
        tk.Button(self.root, text="Add Steps", command=self.add_steps).grid(row=0, column=2)

        # Water Intake
        tk.Label(self.root, text="Water (liters):").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.water).grid(row=1, column=1)
        tk.Button(self.root, text="Add Water", command=self.add_water).grid(row=1, column=2)

        # Sleep
        tk.Label(self.root, text="Sleep (hours):").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.sleep).grid(row=2, column=1)
        tk.Button(self.root, text="Add Sleep", command=self.add_sleep).grid(row=2, column=2)

        # Show Summary
        tk.Button(self.root, text="Show Summary", command=self.show_summary).grid(row=3, columnspan=3)

    def add_steps(self):
        steps = self.steps.get()
        messagebox.showinfo("Info", f"Added {steps} steps.")

    def add_water(self):
        water = self.water.get()
        messagebox.showinfo("Info", f"Added {water} liters of water.")

    def add_sleep(self):
        sleep = self.sleep.get()
        messagebox.showinfo("Info", f"Added {sleep} hours of sleep.")

    def show_summary(self):
        steps = self.steps.get()
        water = self.water.get()
        sleep = self.sleep.get()
        summary = f"Total steps: {steps}\nTotal water intake: {water} liters\nTotal sleep: {sleep} hours"
        messagebox.showinfo("Health Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()