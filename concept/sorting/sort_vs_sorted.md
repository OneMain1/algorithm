### sort() vs sorted()
Sorting functions
- `sort()`: in-place sorting, returns None (memory efficient)
- `sorted()`: returns new list
- Both use Timsort algorithm O(n log n)
- **Default: ascending order**
- For descending: add `reverse=True` parameter
- Example: `numbers.sort(reverse=True)` or `sorted(numbers, reverse=True)`
- **CRITICAL**: `[].sort()` returns None, not a list!
