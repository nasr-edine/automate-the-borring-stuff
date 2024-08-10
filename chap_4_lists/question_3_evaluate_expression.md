## Practice Question 3: Evaluating the Expression with spam

### Question:
Given the list `spam = ['a', 'b', 'c', 'd']`, what does the expression `spam[int(int('3' * 2) // 11)]` evaluate to?

### Answer:
Let’s break down the expression step by step:

1. `'3' * 2` results in the string `'33'`.
2. `int('33')` converts the string `'33'` to the integer `33`.
3. `33 // 11` performs integer division, resulting in `3`.
4. `spam[3]` accesses the element at index `3` in the list `spam`, which is `'d'`.

### Example:
```python
spam = ['a', 'b', 'c', 'd']  # The list
result = spam[int(int('3' * 2) // 11)]  # Evaluating the expression
print(result)  # Output: 'd'
```

### Summary:
The expression `spam[int(int('3' * 2) // 11)]` evaluates to `'d'` when `spam` contains the list `['a', 'b', 'c', 'd']`.