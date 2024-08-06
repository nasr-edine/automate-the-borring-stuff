## Difference Between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)`

**Question 12**: What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a for loop?

- **`range(10)`**:
  - **Description**: Generates a sequence of numbers from 0 to 9 (inclusive).
  - **Default Values**: Start at 0 and step by 1.
  - **Usage**:
    ```python
    for i in range(10):
        print(i)
    # Output: 0 1 2 3 4 5 6 7 8 9
    ```

- **`range(0, 10)`**:
  - **Description**: Generates a sequence of numbers from 0 to 9 (inclusive).
  - **Explicit Start and End**: Start at 0 and end at 10 (exclusive).
  - **Usage**:
    ```python
    for i in range(0, 10):
        print(i)
    # Output: 0 1 2 3 4 5 6 7 8 9
    ```

- **`range(0, 10, 1)`**:
  - **Description**: Generates a sequence of numbers from 0 to 9 (inclusive).
  - **Explicit Start, End, and Step**: Start at 0, end at 10 (exclusive), and step by 1.
  - **Usage**:
    ```python
    for i in range(0, 10, 1):
        print(i)
    # Output: 0 1 2 3 4 5 6 7 8 9
    ```

### Summary
All three ranges produce the same sequence of numbers from 0 to 9 (inclusive). The difference is in how explicitly the start, stop, and step values are defined:
- `range(10)` uses default values for start (0) and step (1).
- `range(0, 10)` explicitly sets the start to 0 and the stop to 10.
- `range(0, 10, 1)` explicitly sets the start to 0, the stop to 10, and the step to 1.
