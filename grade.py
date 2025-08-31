import tkinter as tk
from tkinter import messagebox

def calculate_grades():
    try:
        mid = float(mid_entry.get())
        end = float(end_entry.get())
        
        final_grade = (mid + end) / 2
        
        # Update result with color based on grade
        result_text = f"Final Grade: {final_grade:.1f}%"
        result_label.config(text=result_text)
        
        # Add letter grade
        if final_grade >= 90:
            letter = "A"
            color = "#4ade80"  # Green
        elif final_grade >= 80:
            letter = "B" 
            color = "#60a5fa"  # Blue
        elif final_grade >= 70:
            letter = "C"
            color = "#fbbf24"  # Yellow
        elif final_grade >= 60:
            letter = "D"
            color = "#f97316"  # Orange
        else:
            letter = "F"
            color = "#ef4444"  # Red
            
        letter_label.config(text=f"Letter Grade: {letter}", fg=color)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear_all():
    mid_entry.delete(0, tk.END)
    end_entry.delete(0, tk.END)
    result_label.config(text="Final Grade: --")
    letter_label.config(text="Letter Grade: --", fg="#ffffff")

# Create main window
window = tk.Tk()
window.title("Simple Grade Calculator")
window.config(bg="#1a1a2e")
window.resizable(True, True)

# Set window size AFTER creating it
window.geometry("350x380")

# Simple centering
window.update_idletasks()

# Title
title = tk.Label(window, text="Grade Calculator", 
                font=("Poppins", 18, "bold"), 
                bg="#1a1a2e", fg="#ffffff")
title.pack(pady=20)

# Input frame
input_frame = tk.Frame(window, bg="#1a1a2e")
input_frame.pack(pady=10)

# Midterm input
tk.Label(input_frame, text="Midterm Grade:", 
         font=("Poppins", 11), bg="#1a1a2e", fg="#ffffff").grid(row=0, column=0, sticky="w", pady=8)
mid_entry = tk.Entry(input_frame, font=("Poppins", 11), width=15, 
                    bg="#16213e", fg="#ffffff", insertbackground="#ffffff")
mid_entry.grid(row=0, column=1, padx=10, pady=8)

# Endterm input  
tk.Label(input_frame, text="Endterm Grade:", 
         font=("Poppins", 11), bg="#1a1a2e", fg="#ffffff").grid(row=1, column=0, sticky="w", pady=8)
end_entry = tk.Entry(input_frame, font=("Poppins", 11), width=15,
                    bg="#16213e", fg="#ffffff", insertbackground="#ffffff")
end_entry.grid(row=1, column=1, padx=10, pady=8)

# Buttons
button_frame = tk.Frame(window, bg="#1a1a2e")
button_frame.pack(pady=15)

calculate_btn = tk.Button(button_frame, text="Calculate", 
                         command=calculate_grades,
                         font=("Poppins", 11, "bold"),
                         bg="#0ea5e9", fg="#ffffff",
                         padx=20, pady=5, cursor="hand2")
calculate_btn.pack(side="left", padx=5)

clear_btn = tk.Button(button_frame, text="Clear", 
                     command=clear_all,
                     font=("Poppins", 11, "bold"), 
                     bg="#ef4444", fg="#ffffff",
                     padx=20, pady=5, cursor="hand2")
clear_btn.pack(side="left", padx=5)

# Results
result_label = tk.Label(window, text="Final Grade: --", 
                       font=("Poppins", 14, "bold"),
                       bg="#1a1a2e", fg="#ffffff")
result_label.pack(pady=10)

letter_label = tk.Label(window, text="Letter Grade: --", 
                       font=("Poppins", 12),
                       bg="#1a1a2e", fg="#ffffff") 
letter_label.pack(pady=5)

# Bind Enter key to calculate
mid_entry.bind('<Return>', lambda e: calculate_grades())
end_entry.bind('<Return>', lambda e: calculate_grades())

# Start the app
window.mainloop()