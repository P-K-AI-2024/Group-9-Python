import re

# Define the user_data dictionary at the top of the script
user_data = {
    "user1@example.com": {
        "first_name": "Alice",
        "last_name": "Johnson",
        "age": 25,
        "password": "password123"
    },
    "user2@example.com": {
        "first_name": "Bob",
        "last_name": "Smith",
        "age": 30,
        "password": "securepass"
    }
}

# Validation functions like for email, password, age validation
def is_valid_email(email):
    """Validate email format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_password(password):
    """Validate password format (at least 6 characters, letters, and numbers)."""
    return len(password) >= 6 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)

def is_valid_age(age):
    """Validate if the age is a positive integer."""
    try:
        age = int(age)
        return age > 0
    except ValueError:
        return False

def signup():
    """Handles the user signup process with validations."""
    print("\n--- Signup ---")
    
    # Email validation
    while True:
        email = input("Enter Email ID: ").strip()
        if email in user_data:
            print("Email already registered. Please try signing in.")
            return
        if not is_valid_email(email):
            print("Invalid email format. Please enter a valid email address (e.g., example@domain.com).")
        else:
            break

    # Password validation
    while True:
        password = input("Enter Password: ").strip()
        if not is_valid_password(password):
            print("Password must be at least 6 characters long, and contain both letters and numbers.")
        else:
            break

    # Collect other details
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()

    # Age validation
    while True:
        age = input("Enter Age: ").strip()
        if not is_valid_age(age):
            print("Please enter a valid positive integer for age.")
        else:
            age = int(age)
            break

    # Store user information in plain text
    user_data[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "password": password
    }

    print("Signup successful! You can now log in.")

def signin():
    """Handles the user login process with exception handling."""
    print("\n--- Sign-in ---")
    
    # Email validation
    while True:
        email = input("Enter Email ID: ").strip()
        if email not in user_data:
            print("No account found with this email. Please sign up.")
            return
        if not is_valid_email(email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            break

    # Password validation
    while True:
        password = input("Enter Password: ").strip()
        if user_data[email]["password"] == password:
            print(f"Welcome, {user_data[email]['first_name']}! You have successfully logged in.")
            break
        else:
            print("Incorrect password. Please try again.")

def main_menu():
    """Displays the menu and handles user input."""
    while True:
        print("\n=== User Authentication System ===")
        print("1. Signup")
        print("2. Sign-in")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            signup()
        elif choice == '2':
            signin()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
