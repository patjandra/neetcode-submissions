class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst=set()
        for i in nums:
            lst.add(i)
        if len(nums)!= len(lst):
            return True
        return False
