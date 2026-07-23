import getpass

# 1 Accept the password securely
password = getpass.getpass("Enter password to test: ")

# Initialize our category flags (True/False)
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

# 2 Check length first
length_ok = len(password) >= 8

# 3 Inspect every character to see what categories are present
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum() and not char.isspace():
        has_symbol = True

# 4 Calculate the score (True counts as 1, False counts as 0)
score = sum([has_upper, has_lower, has_digit, has_symbol])

# 5 Determine and display the strength
print("\n--- Password Strength Result ---")

if not length_ok:
    print("Strength: WEAK (Must be at least 8 characters long)")
elif score <= 2:
    print("Strength: WEAK (Needs a better mix of character types)")
elif score == 3:
    print("Strength: MEDIUM (Good, but add a symbol or uppercase to make it excellent!)")
elif score == 4:
    print("Strength: EXCELLENT (Super secure!)")

print("---")