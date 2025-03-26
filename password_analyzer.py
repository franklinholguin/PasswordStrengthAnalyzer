import tkinter as tk
from tkinter import messagebox

def check_password(password):
    feedback = []
    score = 0
    
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters.")
    else:
        score += 1
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")
        
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")
        
    with open("common_passwords.txt", "r") as f:
        common = [line.strip() for line in f]
    if password in common:
        feedback.append("Password is too common!")
        score = 0
    
    strength = "Weak" if score < 2 else "Moderate" if score < 4 else "Strong"
    return strength, feedback

def analyze():
    password = entry.get()
    strength, feedback = check_password(password)
    result_text.set(f"Password Strength: {strength}")
    feedback_text.delete(1.0, tk.END)  # Clear previous feedback
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n" + "\n".join(f"- {tip}" for tip in feedback))

# Set up GUI
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

# Input
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*")  # Hide password input
entry.pack(pady=5)

# Button
tk.Button(root, text="Check Strength", command=analyze).pack(pady=10)

# Result
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack(pady=5)

# Feedback
feedback_text = tk.Text(root, height=10, width=50)
feedback_text.pack(pady=5)

root.mainloop()