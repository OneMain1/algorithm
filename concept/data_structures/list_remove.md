### List - Removing Elements
Methods to remove elements from a list
- `del lst[i]` - delete at index i, no return value
- `lst.pop(i)` - delete at index i and return the value
- `lst.pop()` - delete and return last element, O(1)
- Example: `del lst[2]` → delete index 2
- Example: `x = lst.pop(2)` → delete index 2 and store value
- Middle deletion is O(n), end deletion is O(1)
