import sys
import string

def analyze_text(text):
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punctuation_count = sum(1 for c in text if c in string.punctuation)
    space_count = sum(1 for c in text if c.isspace())
    digit_count = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")
    
    analyze_text(text)

if __name__ == "__main__":
    main()

