### abs()
Return absolute value of a number
- Useful for symmetric patterns: use `abs(i)` with `range(1-n, n)`
- Example: `abs(-3)` → `3`, `abs(3)` → `3`
- Diamond pattern: `' ' * abs(i) + '*' * (2 * (n - abs(i)) - 1)`
