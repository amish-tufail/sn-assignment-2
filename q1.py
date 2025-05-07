# Pseudo-code:
# First, we define a function to encrypt the text based on given rules.
# - For lowercase letters (a-z), check if the letter is in the first or second half of the alphabet.
# - For the first half (a-m), shift forward by n * m.
# - For the second half (n-z), shift backward by n + m.
# - For uppercase letters (A-Z), check if the letter is in the first or second half.
# - For the first half (A-M), shift backward by n.
# - For the second half (N-Z), shift forward by m^2.
# - Special characters and numbers remain unchanged.
#
# Then, we define a function to decrypt the text based on the same rules:
# - Reverse the encryption steps for both lowercase and uppercase letters.
# - Shift backward for the first half of the alphabet, and shift forward for the second half.
# - Special characters and numbers remain unchanged.
#
# After that, we define a function to check if the decrypted text matches the original text:
# - If the decrypted text matches the original text, print "Decryption is successful!".
# - If not, print "Decryption failed. The texts do not match."
#
# Finally, we define a function to get valid user input for n and m:
# - If the user enters an invalid value (non-integer), show an error and ask again.
#
# After running the program, the user can choose whether to redo the encryption and decryption process:
# - Prompt the user if they want to retry with different n and m values or exit the program.

# Here is the complete code:

# Function to encrypt the text based on given rules
def encrypt_text(text, n, m):
    encrypted_text = []
    
    for char in text:
        # Handle lowercase letters (a-z)
        if 'a' <= char <= 'z':
            if char <= 'm':  # First half of alphabet (a-m)
                # Shift forward by n * m
                new_char = chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:  # Second half of alphabet (n-z)
                # Shift backward by n + m
                new_char = chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
            encrypted_text.append(new_char)
        
        # Handle uppercase letters (A-Z)
        elif 'A' <= char <= 'Z':
            if char <= 'M':  # First half of alphabet (A-M)
                # Shift backward by n
                new_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:  # Second half of alphabet (N-Z)
                # Shift forward by m^2
                new_char = chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
            encrypted_text.append(new_char)
        
        # Special characters and numbers remain unchanged
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

# Function to decrypt the text based on given rules
def decrypt_text(text, n, m):
    decrypted_text = []
    
    for char in text:
        # Handle lowercase letters (a-z)
        if 'a' <= char <= 'z':
            if char <= 'm':  # First half of alphabet (a-m)
                # Shift backward by n * m
                new_char = chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:  # Second half of alphabet (n-z)
                # Shift forward by n + m
                new_char = chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
            decrypted_text.append(new_char)
        
        # Handle uppercase letters (A-Z)
        elif 'A' <= char <= 'Z':
            if char <= 'M':  # First half of alphabet (A-M)
                # Shift forward by n
                new_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:  # Second half of alphabet (N-Z)
                # Shift backward by m^2
                new_char = chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
            decrypted_text.append(new_char)
        
        # Special characters and numbers remain unchanged
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Function to check the correctness of the decrypted text
def check_decrypted_text(original, decrypted):
    if original == decrypted:
        print("Decryption is successful!")
    else:
        print("Decryption failed. The texts do not match.")

# Function to get valid integer input from the user
def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer value.")

# Function to process the text file and handle user input with error checking
def process_file():
    # Read the raw text from the file or prompt user to create it
    try:
        with open('raw_text.txt', 'r') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("raw_text.txt not found. Creating a sample text file...")
        raw_text = "This is a sample text for encryption!"
        with open('raw_text.txt', 'w') as file:
            file.write(raw_text)
    
    # Prompt for n and m
    n = get_valid_integer_input("Enter the value for n: ")
    m = get_valid_integer_input("Enter the value for m: ")

    # Encrypt the text
    encrypted_text = encrypt_text(raw_text, n, m)
    
    # Write the encrypted text to a new file
    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)
    
    print("Encryption successful! Encrypted text written to 'encrypted_text.txt'.")
    
    # Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, n, m)
    
    # Write the decrypted text to a new file
    with open('decrypted_text.txt', 'w') as file:
        file.write(decrypted_text)
    
    # Check if decryption is correct
    check_decrypted_text(raw_text, decrypted_text)

# Function to ask the user if they want to redo the encryption/decryption
def redo_prompt():
    while True:
        redo = input("Do you want to redo the encryption and decryption process? (y/n): ").lower()
        if redo == 'y':
            process_file()
            break
        elif redo == 'n':
            print("Exiting the program.")
            break
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the program
process_file()
redo_prompt()
