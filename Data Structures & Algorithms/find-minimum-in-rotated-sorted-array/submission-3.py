class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left, right, and middle pointers
        # if mid > r, smaller subarray to the right of mid
        # else mid < r, smaller subarray is mid or to the left of mid
        l, r = 0, len(nums)-1

        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]