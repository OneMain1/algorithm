### String is iterable
Strings can be iterated directly without list()
- `for char in "abc":` ✓ (can iterate directly)
- `for char in list("abc"):` ✗ (unnecessary conversion)
- Use `for char in input():` instead of `list(input())`
