class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #For each str in strs we will calucate the charCount.
        #Use that as a key in a dict
        #Append all the str that have same charCount

        res = defaultdict(list) #To map charCount to anagrams

        for s in strs:
            charCount = [0]*26

            for ch in s:
                charCount[ord(ch) - ord("a")] += 1
            
            res[tuple(charCount)].append(s) #A list can not be a key since it is mutable. Hence converting it to tuple because tuple is immutable

        return res.values()

        #TC: O(m*n) m=#number of str, n=avg length of each str
        #Other way to solve this problem would be to sort each str and then grouping the strs that are same after sorting. TC for that would be O(m*nlogn)
        
