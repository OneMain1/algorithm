### Input patterns
Choose correct pattern based on input format
- Single number: `n = int(input())`
- Multiple numbers on one line: `nums = list(map(int, input().split()))`
- Multiple lines, one number each: `nums = [int(input()) for _ in range(n)]`
- **Common mistake**: `int(input().split())` ✗ → int() can't convert list
- **Common mistake**: `map(int, input())` for single number ✗ → returns map object
