import random
import string

def get_user_choice(message):
    """Function to get yes/no input from user"""
    while True:
        choice = input(message).strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter Y or N only.")

def generate_password():
    print("====== Random Password Generator ======")

    # Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Ask user preferences
    use_letters = get_user_choice("Include letters? (Y/N): ")
    use_numbers = get_user_choice("Include numbers? (Y/N): ")
    use_symbols = get_user_choice("Include symbols? (Y/N): ")

    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("You must select at least one character type!")
        return

    # Generate password
    password = ""
    for _ in range(length):
        password += random.choice(character_pool)

    print("\nGenerated Password:", password)
    print("=======================================")

if __name__ == "__main__":
    generate_password()
