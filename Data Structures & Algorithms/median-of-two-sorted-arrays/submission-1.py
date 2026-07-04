class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge lists
        # algo to find median
            # if len is even, take ((mid)+(mid+1)/2)
            # else, take mid
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        mid = (len(nums1)-1)//2
        if len(nums1)%2 == 0:
            return (nums1[mid]+nums1[mid+1])/2
        else:
            return nums1[mid]
