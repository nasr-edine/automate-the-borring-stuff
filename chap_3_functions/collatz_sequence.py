def collatz(number):
    # Check if the number is even
    if number % 2 == 0:
        result = number // 2
    else:
        # If the number is odd, apply the Collatz transformation
        result = number * 3 + 1
    return result

# Get user input with error handling
try:
    number = int(input('Enter a number: '))
except ValueError:
    print('You must enter an integer.')
    number = 1  # Defaulting to 1 to end the program immediately

# Continue the sequence until the number reaches 1
while number > 1:
    number = collatz(number)
    print(number)
