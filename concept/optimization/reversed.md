### reversed()
Reverse iteration over a sequence without modifying original
- Returns reverse iterator (not a list)
- Memory efficient - doesn't create a copy
- Example: `reversed(range(1, n + 1))` → iterate n, n-1, ..., 2, 1
- Works with sequences: lists, tuples, strings, range objects
- Compare: `range(n, 0, -1)` vs `reversed(range(1, n + 1))` (same result)
- Use `list(reversed(...))` to create reversed list
