class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        if pivot == 0:
            left, right = 0, len(nums) - 1
        elif nums[0] <= target <= nums[pivot - 1]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1