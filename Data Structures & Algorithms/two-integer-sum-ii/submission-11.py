class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[front]+numbers[back] > target:
                back -= 1
            elif numbers[front]+numbers[back] < target:
                front += 1
            else:
                return [front+1,back+1]