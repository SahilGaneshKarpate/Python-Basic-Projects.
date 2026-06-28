# Function to analyze a string
def analyze_string(s):

    # Check if string is empty
    if s == "":
        print("String is empty.")
        return

    # Print length of string
    print("Length:", len(s))

    # Print reverse string
    print("Reverse:", s[::-1])

    # Count vowels
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Total Vowels:", count)

    # Print character with positive and negative index
    print("\nCharacters with Index:")

    for i in range(len(s)):
        print("Positive Index:", i,
              "Negative Index:", i-len(s),
              "Character:", s[i])


# Take input from user
text = input("Enter a string: ")

# Call function
analyze_string(text)