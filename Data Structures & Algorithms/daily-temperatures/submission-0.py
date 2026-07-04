class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # double loop through temperatures
        # compare with every other temperature, and maintain a largest seen, only alter result value if curr > largest
        # result values are j - i
        result = []
        largest = 0
        for i in range(len(temperatures) - 1):
            result.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        result.append(0)
        return result
            
