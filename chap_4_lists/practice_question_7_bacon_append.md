## Practice Question 7: Result of bacon.append(99)

### Question:
Given the list `bacon = [3.14, 'cat', 11, 'cat', True]`, what does the list look like after the expression `bacon.append(99)` is executed?

### Answer:
The `append()` method in Python adds an item to the end of the list. 

- After executing `bacon.append(99)`, the list `bacon` becomes `[3.14, 'cat', 11, 'cat', True, 99]`.

### Example:
```python
bacon = [3.14, 'cat', 11, 'cat', True]  # Original list
bacon.append(99)  # Appending 99 to the end of the list
print(bacon)  # Output: [3.14, 'cat', 11, 'cat', True, 99]
```

### Summary:
The expression `bacon.append(99)` modifies the list `bacon` to include `99` as the last element, resulting in `[3.14, 'cat', 11, 'cat', True, 99]`.