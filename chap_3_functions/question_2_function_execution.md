## Function Execution

**Question 2**: When does the code in a function execute: when the function is defined or when the function is called?

The code inside a function executes only when the function is called, not when the function is defined.

### Explanation

- **Function Definition**: This is when you write the code for the function, specifying its name, parameters, and the block of code it contains. During this phase, Python merely registers the function and its code for later use; it does not execute the function.

  ```python
  def greet(name):
      print(f"Hello, {name}!")

In the above example, the `greet` function is defined, but the code inside it (`print(f"Hello, {name}!")`) does not run at this point.

- **Function Call**: This is when you invoke the function to perform its task. Only when the function is called does Python execute the code inside the function.

  ```python
  greet("Alice")
  ```

In this example, calling `greet("Alice")` executes the code inside the `greet` function, printing `Hello, Alice!`.

### Example
- Here is a complete example to illustrate the difference between `function definition` and `function call`:
  ```python
    # Function definition
    def add(a, b):
        return a + b

    # Function call
    result = add(3, 5)
    print(result)  # Output: 8  
  ```
In the example above:

- The function add is defined with two parameters, a and b, and a return statement that adds them.
- The function add is called with arguments 3 and 5, and the result (8) is printed.

### Summary
**In summary**, the code inside a function executes only when the function is called, not when it is defined. Function definition is about declaring the function and its behavior, whereas function call is about executing that behavior.
