## Practice Question 6: Evaluating bacon.index('cat')

### Question:
Given the list `bacon = [3.14, 'cat', 11, 'cat', True]`, what does the expression `bacon.index('cat')` evaluate to?

### Answer:
In Python, the `index()` method returns the index of the first occurrence of the specified value in the list. 

- `bacon.index('cat')` evaluates to `1` because `'cat'` first appears at index `1` in the list.

### Example:
```python
bacon = [3.14, 'cat', 11, 'cat', True]  # The list
result = bacon.index('cat')  # Finding the first index of 'cat'
print(result)  # Output: 1
```
### Summary:
The expression `bacon.index('cat')` evaluates to `1` because `'cat'` first appears at index `1` in the list `bacon = [3.14, 'cat', 11, 'cat', True]`.