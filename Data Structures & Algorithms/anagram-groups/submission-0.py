from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Dictionary to group anagrams

        for s in strs:
            count = [0] * 26  # Count frequency of each letter (a-z)

            for c in s:
                count[ord(c) - ord("a")] += 1  # Increment letter count
            
            res[tuple(count)].append(s)  # Convert to tuple as key

        return list(res.values())  # Convert dictionary values to list

# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
