class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m_dex = len(nums)//2
        middle = nums[m_dex]

        if target > middle:
            for i in range(m_dex, len(nums)):
                if target == nums[i]:
                    return i
            return -1
        elif target < middle:
            for i in range(m_dex):
                if target == nums[i]:
                    return i
            return -1
        else:
            return m_dex


        