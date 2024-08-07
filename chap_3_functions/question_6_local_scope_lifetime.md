## Variables in Local Scope After Function Returns

**Question 6**: What happens to variables in a local scope when the function call returns?

### Explanation

When a function is called, a new local scope is created for that function. Variables defined within this local scope are only accessible inside the function. 

**Upon function return:**

- **Local Variables**: Local variables are destroyed and their memory is freed when the function returns. This means that once the function finishes execution and returns, the local scope is discarded and the variables defined within it are no longer accessible.

### Example

```python
def my_function():
    local_var = "I am local"
    print(local_var)  # This works fine and prints the local variable

my_function()

print(local_var)  # This will raise an error since local_var is no longer accessible
```

- In the example above, `local_var` is defined inside `my_function`. It is accessible within the function and printed when the function is called.

- Once `my_function` completes and returns, `local_var` is no longer available. Trying to access `local_var` outside the function will result in a `NameError` because the variable has been destroyed along with its local scope.

### Summary
Local variables are temporary and exist only during the function call. They are removed when the function returns, meaning their scope ends and they can no longer be accessed.