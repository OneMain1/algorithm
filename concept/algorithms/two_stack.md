### Two Stack Technique
Use two stacks for efficient cursor-based editing (BOJ 1406)
- `left` stack: characters to the left of cursor
- `right` stack: characters to the right (stored in reverse)
- All operations O(1):
  - P x: `left.append(x)` - add left of cursor
  - L: `right.append(left.pop())` - move cursor left
  - D: `left.append(right.pop())` - move cursor right
  - B: `left.pop()` - delete left of cursor
- Output: `''.join(left + right[::-1])`
- **Key insight**: `insert()`/`del` in middle is O(n), stack end operations are O(1)
