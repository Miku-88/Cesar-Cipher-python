import os
def welcome():
    """
    shows welcome message to the program
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with Caesar Cipher.")

def enter_message():
    """
    takes input for encrypt or decrypt, message to process, and shift value
    then returns a tuple containing mode e or d, message and shift value
    """
    while True:
        m = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if m in ['e', 'd']:
            break
    while True:
        msg = input(f"What message would you like to {'encrypt' if m=='e' else 'decrypt'}?").upper()
        if msg.isalpha():
            break
    while True:
        try:
            shift = int(input("What is the shift number: "))
            if 0 <= shift <= 25:
                break
        except ValueError:
            print("Invalid Shift. Please enter a number.")
    return m, msg, shift

def encrypt(msg, shift):
    """
    encrypts the message using ceaser cypher
        msg is the message to be encrypted
        shift if for the shift value
        then returns the encrypted message.
    """
    result = ""
    for i in msg:
        if i.isalpha():
            if i.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted_char = chr((ord(i)-base+shift)%26+base)
            result = result + shifted_char
        else:
            result = result + i
    return result

def decrypt(msg, shift):
    """
    decrypts the message using ceaser cypher
    msg is the message to be decrypted
    shift is the shift value 
    then returns the decrypted message
    """
    return encrypt(msg, -shift)

def process_file(filename, mode, shift):
    """
    this function process messages from file and encrypt or decrypt based on mode and shift value
        filename is the name of the file containing messages
        mode is the mode ('e' or 'd') for encryption or decryption
        shift is the shift value for encryption or decryption
        then returns a list of encrypted or decrypted messages
    """
    msgs = []
    try:
        with open(filename,'r') as f:
            for a in f:
                msgs.append(a.strip())
    except FileNotFoundError:
        print("File not found")
        return []

    return [encrypt(msg, shift) if mode == 'e' else decrypt(msg, shift) for msg in msgs]

def is_file(filename):
    """
    used to check if the file exists
        filename is the name of the file
    """
    return os.path.isfile(filename)

def write_messages(msgs):
    """
    used to write message to a file
    msgs is a list of messages to be written to a file
    """
    with open('results.txt', 'w') as f:
        for msg in msgs:
            f.write(msg + '\n')

def message_or_file():
    """
    Takes input from the user to determine if to read from a file or the console.
    Returns a tuple containing the mode, the input message, and the filename.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        check = input("Would you like to read from a file (f) or the console (c): ").lower()
        if check in ['f', 'c']:
            break
        else:
            print("Invalid Choice")

    if check == 'c':
        while True:
            msg = input(f"What message would you like to {'encrypt' if mode=='e' else 'decrypt'}? ")
            msg = msg.upper()
            if any(c.isalpha() for c in msg):
                break
            else:
                print("Invalid Message")
        return mode, msg, None
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        return mode, None, filename


def main():
    """
    Main function to execute the Caesar Cipher program.
    """
    welcome()

    while True:
        mode, message, filename = message_or_file()

        shift = 0
        while True:
            try:
                shift = int(input("What is the shift number: "))
                if 1 <= shift <= 26:
                    break
                else:
                    print("Invalid Shift")
            except ValueError:
                print("Invalid Shift. Please enter a number.")

        if filename:
            messages = process_file(filename, mode, shift)
            if messages:
                write_messages(messages)
                print("Output written to results.txt")
            else:
                print("No messages to process.")
        else:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)

        ant_msg = input("Would you like to encrypt or decrypt another message? (y/n): ")
        ant_msg=ant_msg.lower()
        if ant_msg != 'y':
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()