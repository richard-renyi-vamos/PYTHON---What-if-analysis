import tkinter as tk
import pandas as pd

# Create a simple What-If analysis function
def perform_analysis():
    try:
        # Retrieve the user input data
        original_value = float(entry_original_value.get())
        change_percent = float(entry_change_percent.get())

        # Calculate the new value after change
        new_value = original_value * (1 + change_percent / 100)

        # Display the result in the result label
        result_label.config(text=f"New Value: {new_value:.2f}")
        
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create the Tkinter window
window = tk.Tk()
window.title("What-If Analysis App")

# Original Value input
tk.Label(window, text="Original Value:").grid(row=0, column=0)
entry_original_value = tk.Entry(window)
entry_original_value.grid(row=0, column=1)

# Change Percent input
tk.Label(window, text="Change Percent (%):").grid(row=1, column=0)
entry_change_percent = tk.Entry(window)
entry_change_percent.grid(row=1, column=1)

# Perform button
perform_button = tk.Button(window, text="Perform What-If", command=perform_analysis)
perform_button.grid(row=2, column=0, columnspan=2)

# Result display
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
