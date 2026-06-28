# Import math module
import math

try:

    # Take sentence from user
    sentence = input("Enter a Sentence: ")

    # Split sentence into words
    words = sentence.split()

    # Store unique words in set
    unique_words = set(words)

    # Print unique words
    print("Unique Words:")
    print(sorted(unique_words))

    # Count unique words
    total = len(unique_words)

    # Print square of total words
    print("Square of Total Unique Words:")
    print(math.pow(total, 2))

except Exception:

    print("Something Went Wrong.")