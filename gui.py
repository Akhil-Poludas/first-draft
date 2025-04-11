import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib
import uuid

# Load trained model
model = joblib.load("models/classifier.pkl")

# Team routing map
ROUTE_MAP = {
    "Technical": "Tech Support Team",
    "Billing/Payments": "Billing & Payments Team",
    "Sales/Upgrade": "Customer Success Team",
    "Account Update": "Accounts/Onboarding Team",
    "General": "General Support Team"
}

def classify_message():
    msg = entry.get("1.0", "end-1c").strip()
    if not msg:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    prediction = model.predict([msg])[0]
    department = ROUTE_MAP.get(prediction, "General Support Team")
    ticket_id = "REQ-" + str(uuid.uuid4())[:6].upper()

    # Display result
    result_text.set(f"🎫 Ticket Raised!\n\n"
                    f"Ticket ID   : {ticket_id}\n"
                    f"Issue Type  : {prediction}\n"
                    f"Assigned To : {department}\n\n"
                    f"Message     : \"{msg}\"")

# GUI setup
root = tk.Tk()
root.title("Customer Issue Classifier")
root.geometry("550x400")
root.configure(bg="#f0f4ff")

title = tk.Label(root, text="🧠 Customer Issue Classifier", font=("Helvetica", 16, "bold"), bg="#f0f4ff", fg="#4b0082")
title.pack(pady=10)

entry = tk.Text(root, height=4, font=("Helvetica", 12), wrap="word")
entry.pack(padx=20, pady=10, fill="x")

submit_btn = ttk.Button(root, text="Raise Ticket", command=classify_message)
submit_btn.pack(pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Courier", 11), bg="#f0f4ff", fg="#333")
result_label.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()
