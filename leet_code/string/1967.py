class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                num += 1

        return num
    
# Solution 1
class Solution:                                                                       
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
    

# Solution 2
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num = 0
        for p in patterns:
            if p in word:
                num += 1
        return num