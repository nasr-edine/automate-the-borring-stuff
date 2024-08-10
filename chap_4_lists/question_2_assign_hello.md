## Question 2: Assigning 'hello' as the Third Value in a List

### Question:
How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)

### Answer:
You can assign the value `'hello'` as the third value in the list by accessing the index `2` of the list (since list indices start at `0` in Python) and then assigning the new value.

### Example:
```python
spam = [2, 4, 6, 8, 10]  # Original list
spam[2] = 'hello'  # Assign 'hello' to the third value (index 2)
print(spam)  # Output: [2, 4, 'hello', 8, 10]
```

### Summary:
To assign `'hello'` as the third value in the list `spam`, you access the element at index `2` (`spam[2]`) and assign it the new value.