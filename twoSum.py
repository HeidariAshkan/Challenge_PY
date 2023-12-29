class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}

        for x,i in enumerate(nums):
            com = target - i
            if com in obj:
                return[obj[com] , x]
            obj[i] = x
