class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lst = nums

    def add(self, val: int) -> int:
        self.lst.append(val)
        self.lst.sort()
        return self.lst[-self.k]