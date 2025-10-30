class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        already_done = set()
        for n in nums:
            if n in already_done:
                continue
            temp_lst = nums.copy()
            temp_lst.remove(n)
            perm = self.permuteUnique(temp_lst)
            for p in perm:
                res.append([n] + p)
            already_done.add(n)
        
        return res
