## Practice Question 9: List Concatenation and Replication Operators

### Question:
What are the operators for list concatenation and list replication in Python?

### Answer:
- **List Concatenation:** The `+` operator is used for concatenating (joining) two lists.
- **List Replication:** The `*` operator is used for replicating (repeating) the elements of a list.

### Example:

```python
# List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# List Replication
original_list = ['a', 'b', 'c']
replicated_list = original_list * 3
print(replicated_list)  # Output: ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```

### Summary:
- The `+` operator is used to concatenate lists.
- The `*` operator is used to replicate a list multiple times.