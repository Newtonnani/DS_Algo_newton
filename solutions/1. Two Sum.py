class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            output = target - nums[i]
            if output in hashmap:
                return [i,hashmap[output]]
            hashmap[nums[i]] = i
            
        
