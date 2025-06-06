import tkinter as tk
from tkinter import ttk, messagebox
import subprocess


def run_scan():
    target = target_entry.get().strip()
    if not target:
        messagebox.showerror("Error", "Please enter an IP address or domain")
        return

    # Build nmap command
    cmd = ["nmap", "-Pn", "-sV", target]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, e.output)
        messagebox.showerror("Error", f"Failed to run nmap: {e}")


def create_gui():
    root = tk.Tk()
    root.title("Nmap Port Scanner")

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky="NSEW")

    label = ttk.Label(frame, text="Enter IP address or domain:")
    label.grid(row=0, column=0, sticky="W")

    global target_entry
    target_entry = ttk.Entry(frame, width=40)
    target_entry.grid(row=1, column=0, sticky="EW")

    scan_button = ttk.Button(frame, text="Scan", command=run_scan)
    scan_button.grid(row=1, column=1, padx=5)

    global output_text
    output_text = tk.Text(frame, width=80, height=20)
    output_text.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
