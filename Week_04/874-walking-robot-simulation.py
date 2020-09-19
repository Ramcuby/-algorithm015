class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dir, x, y = 0, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2: dir = (dir + 3)%4
            elif com == -1: dir = (dir + 1)%4
            else:
                for j in range(com):
                    next_x = x + dx[dir]
                    next_y = y + dy[dir]
                    if (next_x, next_y) in obs_dict: break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance
