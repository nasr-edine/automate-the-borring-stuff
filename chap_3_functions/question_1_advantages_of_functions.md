## Advantages of Functions in Programs

**Question 1**: Why are functions advantageous to have in your programs?

### Advantages of Functions

1. **Code Reusability**:
   - Functions allow you to write a piece of code once and reuse it multiple times throughout your program, which reduces redundancy and makes the code easier to maintain.

2. **Modularity**:
   - By breaking the code into smaller, manageable pieces, functions make the program more modular. This makes it easier to understand, test, and debug individual components of the code.

3. **Improved Readability**:
   - Functions help in organizing code logically and give meaningful names to code blocks, making the program more readable and understandable.

4. **Ease of Maintenance**:
   - Functions help in isolating different parts of the program, making it easier to update or fix bugs without affecting other parts of the code.

5. **Abstraction**:
   - Functions provide a way to abstract complex operations, allowing the programmer to use them without needing to understand their inner workings.

6. **Scalability**:
   - Functions make it easier to manage and scale large programs by dividing them into smaller, manageable sections.

### Example
Consider a program that needs to calculate the factorial of a number in multiple places. Instead of writing the factorial calculation code repeatedly, you can define a function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Using the factorial function
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
