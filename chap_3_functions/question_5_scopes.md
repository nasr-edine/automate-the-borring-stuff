## Number of Scopes in a Python Program

**Question 5**: How many global scopes are there in a Python program? How many local scopes?

### Global Scope

- **Global Scope**: There is exactly **one global scope** in a Python program. This scope is created when the program starts and lasts until the program ends. Variables defined in the global scope can be accessed from anywhere in the code, including inside functions (if not shadowed by local variables).

### Local Scope

- **Local Scopes**: There can be **multiple local scopes** in a Python program. Each time a function is called, a new local scope is created for that function. This local scope is specific to the function and lasts until the function finishes execution. Variables defined inside a function are only accessible within that function's local scope.

### Example

```python
# Global scope
global_var = "I am global"

def example_function():
    # Local scope
    local_var = "I am local"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable

example_function()

print(global_var)      # Accessing global variable
print(local_var)      # This will raise an error since local_var is not defined outside the function
```

- **Global Scope**: global_var is defined in the global scope and accessible throughout the code.

- **Local Scope**: local_var is defined in the local scope of example_function and is only accessible within that function.

### Summary
In a Python program, there is one global scope and multiple local scopes, created each time a function is called.