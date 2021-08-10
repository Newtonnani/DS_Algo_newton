class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1,-1]
        def start(nums,target):
            for i,c in enumerate(nums):
                if c == target:
                    return i
        start = start(nums,target)
        if start is not None:
            stop = 0
            for j,k in enumerate(nums[start:]):
                if k == target:
                    stop = j
            return [start,start+stop]
        return output
