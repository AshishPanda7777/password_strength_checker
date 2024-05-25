import re

def check_password_strength(password):
    # Criteria for password strength
    length_ok = len(password) >= 8
    uppercase_ok = any(char.isupper() for char in password)
    lowercase_ok = any(char.islower() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    special_char_ok = bool(re.search(r'[!@#$%^&*()_+=\-{}\[\]:;"/?.><,|\\`~]', password))
    
    # Determine password strength based on criteria
    if length_ok and uppercase_ok and lowercase_ok and digit_ok and special_char_ok:
        return "Strong"
    elif length_ok and (uppercase_ok or lowercase_ok) and digit_ok:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Enter your password: ")
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
        continue_checking = input("Do you want to check another password? (yes/no): ").lower()
        if continue_checking != "yes":
            break
    print("Thank you for using the Password Strength Checker!")

if __name__ == "__main__":
    main()
