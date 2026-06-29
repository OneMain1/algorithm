### Counter (collections)
Count occurrences of elements
- Returns dict-like object with counts
- Example: `Counter([1,2,2,3])` returns `Counter({2:2, 1:1, 3:1})`
- Methods: `most_common()`, `elements()`, `update()`
- `c.get(key, default)` - return default if key not found (prevents KeyError)
- Example: `Counter('aab').get('c', 0)` → `0`
