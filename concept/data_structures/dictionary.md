### Dictionary
Key-Value pairs for fast lookups (Hash Table)
- Syntax: `{key: value}` - key comes first, value comes second
- Example: `grades = {"Alice": 95, "Bob": 87}`
- Access: `grades["Alice"]` returns `95`
- Keys must be unique, values can be duplicated
- **Lookup is O(1)** (list search with `in` is O(n))
- Pattern: store seen values for fast future lookup
- Example: `seen = {}` → `seen[num] = i` → `if target in seen: O(1)`
- Two Sum pattern: check if `target - num` exists in dict while iterating
