class TimeMap:

    def __init__(self):
        # key=(key, timestamp), value=value
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        values = list(self.timeMap.keys()) # list of tuples (key, timestamp)
        largestTime = 0
        largest = ""
        for i in range(len(values)):
            if key == values[i][0] and values[i][1] > largestTime and values[i][1] <= timestamp:
                largestTime = values[i][1]
                largest = self.timeMap[values[i]]
        return largest

