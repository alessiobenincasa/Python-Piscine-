import sys

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    
    # Extract arguments
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    # Check types of arguments
    if not isinstance(S, str) or not isinstance(N, int):
        raise AssertionError("the arguments are bad")
    
    # Filter words using a list comprehension and lambda
    words = S.split()
    filtered_words = [word for word in words if (lambda w: len(w) > N)(word)]
    
    # Print the result
    print(filtered_words)

if __name__ == "__main__":
    main()
