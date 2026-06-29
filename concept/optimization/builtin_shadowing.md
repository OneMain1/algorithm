### Built-in name shadowing
Never use built-in function names as variable/parameter names
- `list`, `map`, `int`, `str`, `sum`, `max`, `min` etc. are built-in functions
- Using them as names shadows the built-in: `list = [1,2,3]` → `list()` no longer works
- Causes `TypeError: 'list' object is not callable`
- **Fix**: Use descriptive names like `nums`, `result`, `items` instead
- Example: `def func(list):` ✗ → `def func(nums):` ✓
