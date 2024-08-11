## Practice Question 8: Result of bacon.remove('cat')

### Question:
Given the list `bacon = [3.14, 'cat', 11, 'cat', True]`, what does the list look like after the expression `bacon.remove('cat')` is executed?

### Answer:
The `remove()` method in Python removes the first occurrence of the specified value from the list.

- After executing `bacon.remove('cat')`, the list `bacon` becomes `[3.14, 11, 'cat', True]`.

### Example:
```python
bacon = [3.14, 'cat', 11, 'cat', True]  # Original list
bacon.remove('cat')  # Removing the first occurrence of 'cat'
print(bacon)  # Output: [3.14, 11, 'cat', True]
```

### Summary:
The expression `bacon.remove('cat')` removes the first occurrence of `'cat'` from the list, resulting in `[3.14, 11, 'cat', True]`