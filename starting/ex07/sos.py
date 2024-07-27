import sys

# Morse code dictionary
NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def encode_to_morse(input_string):
    # Convert input string to uppercase since Morse code is case-insensitive
    input_string = input_string.upper()
    
    # Check if input contains only valid characters
    for char in input_string:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
    
    # Encode each character to Morse code
    encoded_string = ''.join(NESTED_MORSE[char] + " " for char in input_string).strip()
    
    return encoded_string

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    
    # Extract the input string
    input_string = sys.argv[1]
    
    # Ensure input is a string
    if not isinstance(input_string, str):
        raise AssertionError("the arguments are bad")
    
    # Encode the string to Morse code
    morse_code = encode_to_morse(input_string)
    
    # Print the result
    print(morse_code)

if __name__ == "__main__":
    main()
