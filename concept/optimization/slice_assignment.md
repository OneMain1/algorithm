### Slice assignment
Replace a section of a list in-place using slice assignment
- `list[a:b] = new_values` replaces elements from index a to b-1
- Reverse a sublist: `list[a:b] = list[a:b][::-1]`
- `[::-1]` creates a reversed copy of the slice
- Example: `numbers[2:5] = numbers[2:5][::-1]` reverses indices 2,3,4
- Useful for partial list manipulation without rebuilding the entire list
