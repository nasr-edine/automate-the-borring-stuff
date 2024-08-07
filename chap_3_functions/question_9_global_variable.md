## Forcing a Variable to Refer to a Global Variable

**Question 9**: How can you force a variable in a function to refer to the global variable?

In Python, you can use the `global` keyword to force a variable in a function to refer to the global variable instead of creating a local one.

### Example:

```python
x = 10  # This is a global variable

def modify_global():
    global x  # Declare that we are referring to the global variable x
    x = 20    # Modify the global variable

modify_global()
print(x)  # Output: 20
```

In the example above:

- The variable `x` is initially defined in the global scope with a value of 10.
- Inside the `modify_global` function, the `global` keyword is used to indicate that the function should refer to the global variable `x` instead of creating a local one.
- The function then changes the value of `x` to 20.
- When `modify_global` is called and `x` is printed, the output is 20, showing that the global variable was successfully modified within the function.

### Summary
The `global` keyword in Python is used inside a function to refer to a global variable. This allows the function to modify the variable's value in the global scope rather than creating a local copy.
