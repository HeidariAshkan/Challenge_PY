class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        s = dict()
        res = []
        arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            s[i] = s.get(i,0) + 1
        for ke,v in s.items():
            arr[v].append(ke)
        for i in range(len(arr) - 1, 0 , -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res


        



s = Solution()
print(s.topKFrequent([1,2],2))