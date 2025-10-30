class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        res, path = [], []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for n in counts.keys():
                if counts[n] == 0:
                    continue
                counts[n] -= 1
                path.append(n)
                backtrack()
                path.pop()
                counts[n] += 1

        backtrack()
        return res
