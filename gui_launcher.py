import tkinter as tk
import threading
import subprocess

def run_scanner():
    subprocess.call(["python", "malware_detection_tool.py"])

def start_scan():
    log_area.insert(tk.END, "Starting Malware Scanner...\n")
    threading.Thread(target=run_scanner, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Malware Detection Tool")
root.geometry("400x300")

title = tk.Label(root, text="🛡️ Malware Detection Tool", font=("Arial", 16))
title.pack(pady=10)

start_btn = tk.Button(root, text="Start Scan", command=start_scan, bg="green", fg="white")
start_btn.pack(pady=10)

log_area = tk.Text(root, height=10, width=45)
log_area.pack(pady=10)

root.mainloop()
