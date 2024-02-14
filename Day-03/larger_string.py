# Define a function named "larger_string" that takes two parameters, "text" and "n"
def larger_string(text, n):
    # Initialize an empty string variable named "result"
    result = ""

    # Use a for loop to repeat the "text" "n" times and concatenate it to the "result"
    for i in range(n):
        result = result + text

    # Return the final "result" string
    return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

