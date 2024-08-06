## Extra Credit: Understanding `round()` and `abs()` Functions

### `round()` Function

- **Purpose**: Rounds a floating-point number to the nearest integer or to a specified number of decimal places.
- **Syntax**: `round(number[, ndigits])`
  - `number`: The number to be rounded.
  - `ndigits` (optional): The number of decimal places to round to. If omitted, the number is rounded to the nearest integer.

**Examples**:
```python
>>> round(3.14159)
3

>>> round(3.14159, 2)
3.14
```
## `abs()` Function

The `abs()` function returns the absolute value of a number. The absolute value is the non-negative value of the number without regard to its sign.

**Syntax**: `abs(number)`
- `number`: The numeric value for which you want to find the absolute value. This can be an integer, floating-point number, or even a complex number.

**Examples**:
```python
# Absolute value of a negative integer
print(abs(-5))    # Output: 5

# Absolute value of a positive integer
print(abs(3))     # Output: 3

# Absolute value of a floating-point number
print(abs(-3.14)) # Output: 3.14
print(abs(3.14))  # Output: 3.14

# Absolute value of a complex number
print(abs(3 - 4j)) # Output: 5.0
# Explanation: The absolute value of a complex number a + bj is sqrt(a^2 + b^2)
