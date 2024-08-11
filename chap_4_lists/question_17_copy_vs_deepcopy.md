### Question 17: What is the difference between `copy.copy()` and `copy.deepcopy()`?

When working with Python's `copy` module, there are two main functions for copying objects: `copy.copy()` and `copy.deepcopy()`. These functions are used to create copies of objects, but they behave differently when dealing with nested objects (objects that contain other objects like lists within lists).

#### `copy.copy()`
- **Shallow Copy:** `copy.copy()` creates a shallow copy of an object.
- **Behavior:** It copies the object, but does not create copies of objects contained within the original object. Instead, it just copies references to those objects. This means changes made to nested objects in the copied object will affect the original object as well.
- **Use Case:** Shallow copies are typically used when you want to create a copy of an object that does not have nested objects, or when you don't need to duplicate the nested objects.

#### Example:

```python
import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[2].append(5)

print(original_list)  # Output: [1, 2, [3, 4, 5]]
print(shallow_copy)   # Output: [1, 2, [3, 4, 5]]
python
import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[2].append(5)

print(original_list)  # Output: [1, 2, [3, 4, 5]]
print(shallow_copy)   # Output: [1, 2, [3, 4, 5]]
```
**Explanation:**

- In this example, the nested list `[3, 4]` is not copied; both `original_list` and `shallow_copy` reference the same nested list. Therefore, when you modify the nested list in `shallow_copy`, it also modifies the nested list in `original_list`.

**`copy.deepcopy()`**

- **Deep Copy:** `copy.deepcopy()` creates a deep copy of an object.
- **Behavior:** It copies the object and also recursively copies all objects contained within the original object. This means changes made to nested objects in the copied object will not affect the original object.
- **Use Case:** Deep copies are useful when you need to fully duplicate an object, including all objects it contains, so that changes to the copied object do not affect the original object.

#### Example:
```python
import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

deep_copy[2].append(5)

print(original_list)  # Output: [1, 2, [3, 4]]
print(deep_copy)      # Output: [1, 2, [3, 4, 5]]
```


**Explanation:**

In this example, the nested list `[3, 4]` is fully copied. Therefore, when you modify the nested list in `deep_copy`, it does not affect the nested list in `original_list`.

**Summary**

- `copy.copy()` creates a shallow copy, copying the object but not the objects it contains. Changes to nested objects will affect the original object.
- `copy.deepcopy()` creates a deep copy, copying the object and all the objects it contains. Changes to nested objects will not affect the original object.
