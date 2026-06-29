### Direct iteration over list
Prefer `for item in list` over `for i in range(len(list))`
- Simpler, less error-prone, more Pythonic
- Example: `for p in patterns:` instead of `for i in range(len(patterns)): patterns[i]`
- When index is needed, use `enumerate()`: `for i, item in enumerate(lst):`
