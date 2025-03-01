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

def main():
    password = input("Enter a password to check: ")
    strength, feedback = check_password(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"- {tip}")

if __name__ == "__main__":
    main()