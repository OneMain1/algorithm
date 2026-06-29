### center() / rjust() / ljust()
String alignment methods for padding
- `s.center(width)` - center align, add spaces on both sides
- `s.rjust(width)` - right align, add spaces on left
- `s.ljust(width)` - left align, add spaces on right
- Example: `'*'.center(5)` → `'  *  '`
- Example: `'*'.rjust(5)` → `'    *'`
- **Warning**: `center()` adds spaces on both sides, may cause BOJ format error
