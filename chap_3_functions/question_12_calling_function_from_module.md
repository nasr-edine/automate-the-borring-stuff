### Calling a Function from an Imported Module

**Question 12**: If you had a function named `bacon()` in a module named `spam`, how would you call it after importing `spam`?

To call the `bacon()` function from the `spam` module after importing it, you would use the following syntax:

```python
import spam
spam.bacon()
```

**In this example:**

- `import spam` imports the `spam` module.
- `spam.bacon()` calls the `bacon()` function defined in the `spam` module.

### Summary

The `import spam` statement makes the `spam` module available in your code. You can then use `spam.bacon()` to access the `bacon()` function defined in that module.
