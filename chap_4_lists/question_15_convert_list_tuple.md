# Converting Between Lists and Tuples

**Question 15**: How can you get the tuple form of a list value? How can you get the list form of a tuple value?

In Python, you can easily convert between lists and tuples using the `tuple()` and `list()` functions.

## Converting a List to a Tuple

To convert a list into a tuple, use the `tuple()` function. This function takes a list as its argument and returns a tuple containing the same elements.

### Example:

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
```

## Converting a Tuple to a List
To convert a tuple into a list, use the `list()` function. This function takes a tuple as its argument and returns a list containing the same elements.

### Example:

```python
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(my_list)  # Output: [4, 5, 6]
```

## Summary
- Use `tuple()` to convert a list to a tuple.
- Use `list()` to convert a tuple to a list.
Copy code