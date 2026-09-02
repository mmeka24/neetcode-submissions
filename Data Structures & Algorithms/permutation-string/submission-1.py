class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # hashtale approach 

        count1 = Counter(s1)

        window = Counter(s2[:len(s1)])

        if count1 == window:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1

            # delete the left portion 
            left = s2[i - len(s1)]
            window[left] -= 1 

            # if the left window part is non existing just delete
            if window[left] == 0:
                del window[left]

            if count1 == window:
                return True

        return False





        
        
        