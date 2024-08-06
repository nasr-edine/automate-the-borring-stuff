## Difference Between `break` and `continue`

**Question 11**: What is the difference between `break` and `continue`?

- **`break`**:
  - **Purpose**: Exits the current loop immediately.
  - **Usage**: Use `break` to terminate the loop when a certain condition is met.
  - **Example**:
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    # Output: 0 1 2 3 4
    ```

- **`continue`**:
  - **Purpose**: Skips the rest of the current iteration and proceeds to the next iteration of the loop.
  - **Usage**: Use `continue` to skip over specific iterations of the loop based on a condition but keep the loop running.
  - **Example**:
    ```python
    for i in range(10):
        if i == 5:
            continue
        print(i)
    # Output: 0 1 2 3 4 6 7 8 9
    ```

In summary, `break` terminates the entire loop, while `continue` skips the rest of the current loop iteration and proceeds with the next iteration.
