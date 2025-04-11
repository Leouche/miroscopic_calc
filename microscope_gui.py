

import tkinter as tk
from microscope_database import save_to_db, init_db
from microscope_calculator import calculate_real_size

def submit_data():
    username = entry_username.get()
    specimen_name = entry_specimen.get()
    microscope_size = float(entry_size.get())
    magnification = float(entry_magnification.get())

    actual_size = calculate_real_size(microscope_size, magnification)
    save_to_db(username, specimen_name, microscope_size, magnification, actual_size)

    result_label.config(text=f"Actual Size: {actual_size:.4f} mm")

# GUI setup
init_db()
root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Specimen Name").grid(row=1, column=0)
entry_specimen = tk.Entry(root)
entry_specimen.grid(row=1, column=1)

tk.Label(root, text="Microscope Size (mm)").grid(row=2, column=0)
entry_size = tk.Entry(root)
entry_size.grid(row=2, column=1)

tk.Label(root, text="Magnification").grid(row=3, column=0)
entry_magnification = tk.Entry(root)
entry_magnification.grid(row=3, column=1)

tk.Button(root, text="Calculate", command=submit_data).grid(row=4, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()
