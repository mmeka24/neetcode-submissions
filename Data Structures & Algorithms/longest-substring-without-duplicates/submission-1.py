class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        my_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in my_set: 
                my_set.remove(s[l])
                print("the set", my_set)
                l += 1

            my_set.add(s[r])
            res = max(res, r-l+1)

        return res 
        