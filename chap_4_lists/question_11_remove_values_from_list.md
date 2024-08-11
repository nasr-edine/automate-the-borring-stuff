## Practice Question 11: Ways to Remove Values from a List

### Question:
What are two ways to remove values from a list in Python?

### Answer:
Two common ways to remove values from a list in Python are:

1. **`remove()` Method:**
   - The `remove()` method removes the first occurrence of a specified value from the list.
   - If the value is not found, it raises a `ValueError`.
   - Syntax: `list.remove(value)`

   ### Example:
   ```python
   my_list = [1, 2, 3, 2, 4]
   my_list.remove(2)
   print(my_list)  # Output: [1, 3, 2, 4]
   ```

2. **`del` Statement:**

- The `del` statement removes an item at a specified index from the list or deletes a slice of items.
- Unlike `pop()`, `del` does not return the removed item.
- Syntax: `del list[index]` or `del list[start:end]`

  ### Example:
   ```python
    my_list = [1, 2, 3, 4]
    del my_list[1]
    print(my_list)  # Output: [1, 3, 4]
   ```

### Summary:
- Use `remove()` to delete the first occurrence of a specific value.
- Use `del` to remove an item by its index without returning it, or to remove a slice of items.