class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # moves needed = (target-position)//speed [3, 3] [3, 4, 10, 3] --> [3, 3] [3, 3, 4, 10]
        # if the amount of moves needed <= other, they belong in fleet
        # calculate moves for each car, store in set
        # return size of set --> doesn't account for bottenecks
        
        # target=12
        # position=[10,8,0,5,3]
        # speed=[2,4,1,1,3]
        # moves=[1,1,12,7,3]
        # data = [[10,1], [8,1], [0, 12], [5, 7], [3, 3]]
        # moves=[1,1,12,7,3]
        # while stack and currentMoves > stack[-1][0]
            # add to fleetCount
            # stack.pop()
        # if stack and currentMoves == stack[-1][0]
            # continue
        # append to stack

        data = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            data.append([position[i], time])

        data.sort(reverse=True)  # closest to target first

        stack = []

        for pos, time in data:
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: current car catches fleet ahead, so do nothing

        return len(stack)