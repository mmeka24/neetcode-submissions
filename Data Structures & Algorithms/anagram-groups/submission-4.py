from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            #sortedS = ''.join(s)

            #res[sortedS].append(s)

            # better optimal way below

            count = [0] * 26
            for char in s:
                index = ord(char) - ord("a")
                count[index] += 1 
            
            res[tuple(count)].append(s)

        return list(res.values())
        # time complexity o (m * n log n) 
        # space: o (m * n)
        # m is the number of stirngs and n is the len of longest string 

        

        