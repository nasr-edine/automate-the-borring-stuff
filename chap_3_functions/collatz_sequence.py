def collatz(number):
    # Check if the number is even
    if number % 2 == 0:
        result = number // 2
    else:
        # If the number is odd, apply the Collatz transformation
        result = number * 3 + 1
    return result

print('Enter number: ')
number = int(input())

# Continue the sequence until number reaches 1
while number > 1:
    number = collatz(number)
    print(number)
