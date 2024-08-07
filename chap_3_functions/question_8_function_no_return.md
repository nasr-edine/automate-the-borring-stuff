## Return Value of Functions without a Return Statement

**Question 8**: If a function does not have a return statement, what is the return value of a call to that function?

In Python, if a function does not explicitly use a `return` statement to return a value, it returns `None` by default. `None` is a special constant in Python that represents the absence of a value.

### Example:

```python
def no_return():
    print("This function does not return anything.")

result = no_return()
print(result)  # Output: None
```

In the example above, the function `no_return()` does not have a return statement.
When `no_return()` is called, it prints a message but does not return a value.
The variable `result` is assigned the return value of `no_return()`, which is `None`.

### Summary

If a function does not have a `return` statement, the return value of the function is `None`. This is the default behavior in Python to indicate that no explicit value is being returned.
