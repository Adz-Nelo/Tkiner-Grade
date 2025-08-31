import tkinter as tk

def grades():
    try:
        mid = float(mid_entry.get())
        end = float(end_entry.get())

        final_term = mid + end
        final_term = final_term / 2

        result.config(text="Result: " + "{:.2f}".format(final_term) + "%")

    except ValueError:
        result.config(text="Please input numbers only...")


# Creates the main window
window = tk.Tk()
window.title("Midterm and Endterm grades")
window.geometry("200x100")
window.config(bg="#00c1ff")

mid = tk.Label(window, text="Midterm: ", bg="#00fff3")
end = tk.Label(window, text="Endterm: ", bg="#00fff3")

mid_entry = tk.Entry(window)
end_entry = tk.Entry(window)

mid.grid(row=0, column=0, sticky="e")
mid_entry.grid(row=0, column=1)

end.grid(row=1, column=0, sticky="e")
end_entry.grid(row=1, column=1)

calculate_button = tk.Button(
    window, text="Convert to Final Grade", bg="#8dd2f0", command=grades
)
calculate_button.grid(row=2, column=0, columnspan=2)

result = tk.Label(window, text="Result:", bg="#00fff3")
result.grid(row=9, column=1, sticky="w")

# Start the Tkinter event loop
window.mainloop()