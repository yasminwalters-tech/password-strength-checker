print("🔐 Password Strength Checker")
print("----------------------------")

password = input("Enter a password to check: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in "!@#$%^&*()-_=+" for char in password):
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print(f"\nPassword Strength: {strength}")

if score < 5:
    print("Tip: Use 8+ characters, uppercase and lowercase letters, numbers, and symbols.")
else:
    print("Great job! Your password meets all the basic checks.")

