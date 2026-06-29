### Advanced slicing
Slice with start, stop, and step for flexible list manipulation
- `list[-2::-1]` - reverse from second-to-last (exclude last)
- `list[::2]` - even indices only
- `list[1::2]` - odd indices only
- Example: `[1,2,3,4,5][-2::-1]` → `[4,3,2,1]`
- Diamond pattern: `top + top[-2::-1]` (top + reverse excluding peak)
