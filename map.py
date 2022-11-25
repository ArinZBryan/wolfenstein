import math
import warnings

class Map():
    def __init__(self, map : str, scale : float):
        self.map = map.split("\n")
        self.scale = scale
        self.height = len(self.map)
        self.width = len(self.map[0])
    
    def map_to_world(self, x, y):
        return (self.scale * x, self.scale * y)

    def world_to_map(self, x, y):
        return ((x // self.scale),(y // self.scale))

    def world_to_map_value(self, x, y):
        coords = ((x // self.scale), (y // self.scale))
        if (coords[0] > self.height-1 or coords[1] > self.width-1 or coords[0] < 0 or coords[1] < 0):     #check if out of bounds
            #warnings.warn(f"Attempted to read map out of bounds at {coords}")
            return None
        return self.map[coords[1]][coords[0]]

    def map_value(self, x, y):
        if (x > len(self.map)-1 or y > len(self.map[0])-1):
            #warnings.warn(f"Attempted to read map out of bounds at ({x}, {y})")
            return None
        return map[y][x]

def main():
    worldMap = Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    scale = 32
    for i in range(400):
        x = random.randrange(0, scale)
        y = random.randrange(0, scale)
        worldMap.world_to_map_value(x, y)

if __name__ == "__main__":
    import random
    import cProfile as profile
    profile.run("main()")