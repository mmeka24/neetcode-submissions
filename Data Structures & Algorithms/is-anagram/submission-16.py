class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same letteers 
        # samen number of letteres

        # use hashmap

        counter = Counter(s)

        if len(s) != len(t):
            return False

        for i in t:
            if i not in counter or counter[i] == 0:
                return False

            counter[i] -= 1

        return True 

        
        