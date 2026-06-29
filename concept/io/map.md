### map()
Apply function to each element, returns iterator
- Memory efficient (lazy evaluation)
- Example: `map(int, input().split())`
- **IMPORTANT**: map object cannot be indexed directly
- Use unpacking: `a, b, c = map(int, input().split())` ✓
- DON'T append directly: `list.append(map(...))` ✗ (stores map object)
- Use `list(map(...))` for indexing or appending
