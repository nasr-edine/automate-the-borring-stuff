# Automate the Boring Stuff with Python - Answers

This repository contains my solutions to the exercises and practice questions from "Automate the Boring Stuff with Python" by Al Sweigart.

## Repository Structure

```automate-the-boring-stuff/
├── Chapter_1/
│   ├── question1.py
│   ├── question2.py
│   └── ...  # More question files for Chapter 1
├── Chapter_2/
│   ├── question1.py
│   ├── question2.py
│   └── ...  # More question files for Chapter 2
└── README.md
```

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/automate-the-boring-stuff-answers.git
    cd automate-the-boring-stuff-answers
    ```

2. Navigate to a chapter and run the code:
    ```sh
    cd Chapter_1
    python question1.py
    ```

## Example

**Question 9**: Prints different messages based on the value of `spam`.

```python
import random

spam = random.randint(1, 3)

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
# Write your code here :-)
