# Typing a Tuple with a Single Integer Value

**Question 14**: How do you type the tuple value that has just the integer value 42 in it?

In Python, to create a tuple with a single value, you must include a comma after the value. Without the comma, Python will interpret it as just an expression within parentheses, not as a tuple.

## Example:

To create a tuple with the integer value `42`, you would type:

```python
single_value_tuple = (42,)
```
## Explanation:
- **With Comma**: The comma is essential to distinguish a single-value tuple from a parenthesized expression.

```python
single_value_tuple = (42,)  # This is a tuple with one integer element
```

- **Without Comma**: If you omit the comma, it will be interpreted as just an integer in parentheses, not as a tuple.

```python
not_a_tuple = (42)  # This is just an integer with parentheses
```

### Summary
To type a tuple containing a single integer value, such as `42`, you need to include a comma after the integer: `(42,)`. This distinguishes it from a regular expression enclosed in parentheses.