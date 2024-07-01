import random as rd  # Importing the random module with alias 'rd' for generating random values

chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

def getCapital():
    return chr(rd.randint(65, 90))  # Generates a random uppercase letter 'A' to 'Z'

def getSmall():
    return chr(rd.randint(97, 122))  # Generates a random lowercase letter 'a' to 'z'

def getChar():
    return rd.choice(chars)  # Chooses a random character from the chars string

def getNum():
    return str(rd.randint(0, 9))  # Generates a random digit 0 to 9

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Check if at least one character type is selected
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected")
    
    globalPass = ""  # Initialize the password string
    character_pool = []  # Initialize the pool of character functions
    
    # Add character functions to the pool based on user preferences
    if use_uppercase:
        character_pool.append(getCapital)
    if use_lowercase:
        character_pool.append(getSmall)
    if use_digits:
        character_pool.append(getNum)
    if use_special:
        character_pool.append(getChar)

    # Generate the password by randomly selecting characters from the pool
    for _ in range(length):
        globalPass += rd.choice(character_pool)()
    
    return globalPass  # Return the generated password

if __name__ == "__main__":
    # Welcome message for the user
    print("Welcome to the Random Password Generator!")
    
    # Get user input for password length and character inclusion preferences
    length = int(input("Enter the desired password length: "))
    include_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    try:
        # Generate the password based on user preferences
        password = generate_password(length, include_upper, include_lower, include_digits, include_special)
        # Print the generated password
        print("Generated Password: ", password)
    except ValueError as e:
        # Handle the error if no character type is selected
        print(e)
