### Combinations (itertools)
Generate all possible combinations without repetition
- `combinations(iterable, r)` returns all r-length combinations
- Example: `combinations([1,2,3], 2)` → `(1,2), (1,3), (2,3)`
- Time complexity: O(C(n,r)) where C(n,r) = n!/(r!(n-r)!)
- Use for brute force when search space is small
