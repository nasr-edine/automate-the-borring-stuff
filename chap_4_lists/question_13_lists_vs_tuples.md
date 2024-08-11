# Difference Between Lists and Tuples

**Question 13**: What is the difference between lists and tuples?

Lists and tuples are both sequence types in Python, but they have key differences:

1. **Mutability:**
   - **Lists:** Lists are mutable, which means you can change their content (add, remove, or modify items) after they are created.
     ```python
     my_list = [1, 2, 3]
     my_list[1] = 4  # Modifies the list in-place
     print(my_list)  # Output: [1, 4, 3]
     ```
   - **Tuples:** Tuples are immutable, meaning once they are created, their content cannot be changed.
     ```python
     my_tuple = (1, 2, 3)
     # Attempting to modify the tuple will raise an error
     # my_tuple[1] = 4  # TypeError: 'tuple' object does not support item assignment
     ```

2. **Syntax:**
   - **Lists:** Lists are defined using square brackets `[ ]`.
     ```python
     my_list = [1, 2, 3]
     ```
   - **Tuples:** Tuples are defined using parentheses `( )`.
     ```python
     my_tuple = (1, 2, 3)
     ```

3. **Use Cases:**
   - **Lists:** Because they are mutable, lists are generally used for collections of items that may need to be changed throughout the lifetime of the program.
   - **Tuples:** Tuples are often used for fixed collections of items that should not be changed, such as function return values or keys in dictionaries.

4. **Performance:**
   - **Lists:** Due to their mutability, lists have a higher overhead compared to tuples. Operations on lists can be slower.
   - **Tuples:** Tuples have a smaller memory footprint and are faster to access because they are immutable.

5. **Methods:**
   - **Lists:** Lists come with several methods, such as `append()`, `extend()`, `remove()`, and `pop()`.
     ```python
     my_list = [1, 2]
     my_list.append(3)  # Adds 3 to the end of the list
     ```
   - **Tuples:** Tuples have fewer methods; primarily, `count()` and `index()`.
     ```python
     my_tuple = (1, 2, 2)
     print(my_tuple.count(2))  # Output: 2
     ```

## Summary

- **Lists** are mutable and defined with square brackets `[ ]`, suitable for collections of items that can change.
- **Tuples** are immutable and defined with parentheses `( )`, used for fixed collections of items.
