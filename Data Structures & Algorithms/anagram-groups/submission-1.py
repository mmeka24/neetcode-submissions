class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the frequeencies of eahc word 
        # group them by that 

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())