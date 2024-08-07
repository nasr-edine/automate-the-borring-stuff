## Difference Between a Function and a Function Call

**Question 4**: What is the difference between a function and a function call?

### Function

- **Definition**: A function is a block of code that performs a specific task and can be reused throughout your code. It is defined once and can be called multiple times.
- **Definition Syntax**: Functions are defined using the `def` keyword followed by the function name and its parameters.

  ```python
  def greet(name):
      print(f"Hello, {name}!")
  ```
### Function Call

- **Definition**: A function call is an instruction to execute the function's code. It triggers the function and can pass arguments to it.

- **Call Syntax**: Functions are called by using their name followed by parentheses, which may include arguments.

  ```python
  greet("Alice")  # This calls the greet function with "Alice" as an argument
  ```

### Example

Here is a complete example illustrating the difference:

  ```python
  # Function definition
  def add(a, b):
      return a + b

  # Function call
  result = add(3, 5)
  print(result)  # Output: 8
  ```

- **Function Definition**: The add function is defined to take two parameters and return their sum.

- **Function Call**: Calling add(3, 5) executes the function with 3 and 5 as arguments and returns the result, which is printed.

### Summary
A function is a reusable block of code, while a function call is an execution of that code. Functions define actions, and function calls perform those actions.