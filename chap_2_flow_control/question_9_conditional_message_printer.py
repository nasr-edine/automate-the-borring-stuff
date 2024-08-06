import random

# Assign a random integer between 1 and 3 to spam
spam = random.randint(1, 3)

# Check the value of spam and print the corresponding message
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
