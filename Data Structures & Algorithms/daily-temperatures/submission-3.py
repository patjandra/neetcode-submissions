class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [temp, index]

        if len(temperatures) == 1:
            return result
            
        stack.append([temperatures[0], 0])
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        return result
