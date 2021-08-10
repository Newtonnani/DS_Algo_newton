class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,c in enumerate(nums):
            if c == target:
                return i
        return -1
        
