### input() vs sys.stdin.readline()
Fast input for competitive programming
- `input()` - automatically removes newline
- `sys.stdin.readline()` - includes newline (`\n`)
- Example: input "abc" → `input()` = `"abc"`, `readline()` = `"abc\n"`
- `sys.stdin.readline()` is much faster for large input
- Use `.rstrip()` to remove newline: `sys.stdin.readline().rstrip()`
