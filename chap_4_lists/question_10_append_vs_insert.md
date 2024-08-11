## Practice Question 10: Difference Between `append()` and `insert()` Methods

### Question:
What is the difference between the `append()` and `insert()` list methods in Python?

### Answer:
- **`append()` Method:**
  - The `append()` method adds an item to the end of the list.
  - It takes exactly one argument, which is the item to be added.
  - Syntax: `list.append(item)`

- **`insert()` Method:**
  - The `insert()` method adds an item at a specified index in the list.
  - It takes two arguments: the index where the item should be added and the item itself.
  - Syntax: `list.insert(index, item)`

### Example:

```python
# Using append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Using insert()
my_list.insert(1, 'a')
print(my_list)  # Output: [1, 'a', 2, 3, 4]
```

### Summary:
- `append()` adds an item to the end of the list.
- `insert()` adds an item at a specific index within the list.