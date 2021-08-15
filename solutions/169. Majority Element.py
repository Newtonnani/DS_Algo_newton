class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        set_nums = list(set(nums))
        
        
        for i in set_nums:
            count = 0
            for j in nums:
                if i == j:
                    count += 1
                    hashmap[i] = count
​
        for i in hashmap.values():
            if i >= (len(nums)/2):
                return (list(hashmap.keys())[list(hashmap.values()).index(i)])
        
