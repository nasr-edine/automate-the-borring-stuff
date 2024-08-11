# Similarities Between Lists and Strings

**Question 12**: Name a few ways that list values are similar to string values.

List values and string values in Python share several similarities:

1. **Indexing:** Both lists and strings allow access to individual elements using indices.
   - Example:
     ```python
     my_list = [1, 2, 3]
     my_string = "abc"
     print(my_list[0])   # Output: 1
     print(my_string[0]) # Output: 'a'
     ```

2. **Slicing:** You can slice both lists and strings to get a subset of elements.
   - Example:
     ```python
     my_list = [1, 2, 3, 4]
     my_string = "abcd"
     print(my_list[1:3])   # Output: [2, 3]
     print(my_string[1:3]) # Output: 'bc'
     ```

3. **Concatenation:** Both lists and strings can be concatenated using the `+` operator.
   - Example:
     ```python
     my_list = [1, 2] + [3, 4]
     my_string = "ab" + "cd"
     print(my_list)   # Output: [1, 2, 3, 4]
     print(my_string) # Output: 'abcd'
     ```

4. **Repetition:** Both lists and strings can be repeated using the `*` operator.
   - Example:
     ```python
     my_list = [1, 2] * 2
     my_string = "ab" * 2
     print(my_list)   # Output: [1, 2, 1, 2]
     print(my_string) # Output: 'abab'
     ```

5. **Length:** You can find the length of both lists and strings using the `len()` function.
   - Example:
     ```python
     my_list = [1, 2, 3]
     my_string = "abc"
     print(len(my_list))   # Output: 3
     print(len(my_string)) # Output: 3
     ```

### Summary:
Both lists and strings are sequences, meaning they support indexing, slicing, concatenation, repetition, and the `len()` function.
