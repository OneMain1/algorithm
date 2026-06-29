### Dictionary/List mapping
Replace long if-elif chains
- Dict: `result_map = {0: "D", 1: "C"}` → `result_map[value]`
- List: `results = ["D", "C"]` → `results[index]`
- O(1) lookup vs O(n) conditional chains
