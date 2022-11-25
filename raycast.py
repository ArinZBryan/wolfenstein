import map as map
import actors as actors
import math

def cast_blockmap(start : tuple, end : tuple, map : map.Map):
    dx = abs(end[0] - start[0])
    dy = abs(end[1] - start[1])

    x = math.floor(start[0])
    y = math.floor(start[1])

    n = 1
    x_inc, y_inc = 0, 0
    error = 0

    if dx == 0:
        x_inc = 0
        error = float('inf')
    elif end[0] > start[0]:
        x_inc = 1
        n += math.floor(end[0]) - x
        error = (math.floor(start[0]) + 1 - start[0]) * dy
    else:
        x_inc = -1
        n += x - math.floor(end[0])
        error = (start[0] - math.floor(start[0])) * dy
    
    if dy == 0:
        y_inc = 0
        error -= float('inf')
    elif end[1] > start[1]:
        y_inc = 1
        n += math.floor(end[1]) - y
        error -= (math.floor(start[1]) + 1 - start[1]) * dx
    else:
        y_inc = -1
        n += y - math.floor(end[1])
        error -= (start[1] - math.floor(start[1])) * dx
    
    blocks = []

    for i in range(n):
        
        blocks.append(map.world_to_map_value(x, y))

        if error > 0:
            y += y_inc
            error -= dx
        else:
            x += x_inc
            error += dy

    return blocks

#TODO - Look for maths optimisations (like combining sqrt and inverse.)

def cast_blockmap_first(start_x : float, start_y : float, end_x : float, end_y, map : map.Map): ##All integer divisions by 1 are optimizations over math.floor()
    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    x = start_x//1
    y = start_y//1

    n = 1
    x_inc, y_inc = 0, 0
    error = 0

    if dx == 0:
        x_inc = 0
        error = float('inf')
    elif end_x > start_x:
        x_inc = 1
        n += (end_x//1) - x
        error = ((start_x//1) + 1 - start_x) * dy
    else:
        x_inc = -1
        n += x - (end_x//1)
        error = (start_x - (start_x//1)) * dy
    
    if dy == 0:
        y_inc = 0
        error -= float("inf")
    elif end_y > start_y:
        y_inc = 1
        n += (end_y//1) - y
        error -= ((start_y//1) + 1 - start_y) * dx
    else:
        y_inc = -1
        n += y - (end_y // 1)
        error -= (start_y - (start_y//1)) * dx

    for i in range(int(n)):
        coords = ((x // map.scale), (y // map.scale))
        if (coords[0] > map.height-1 or coords[1] > map.width-1 or coords[0] < 0 or coords[1] < 0):     #check if out of bounds
            #warnings.warn(f"Attempted to read map out of bounds at {coords}")
            return None
        map_value = map.map[coords[1]][coords[0]]

        if map_value != "0":
            return map_value

        if error > 0:
            y += y_inc
            error -= dx
        else:
            x += x_inc
            error += dy

    return 0

def cast_actors(start : tuple, end : tuple, actors : list):
    dx = abs(end[0] - start[0])
    dy = abs(end[1] - start[1])

    x = math.floor(start[0])
    y = math.floor(start[1])

    n = 1
    x_inc, y_inc = 0, 0
    error = 0

    if dx == 0:
        x_inc = 0
        error = float('inf')
    elif end[0] > start[0]:
        x_inc = 1
        n += math.floor(end[0]) - x
        error = (math.floor(start[0]) + 1 - start[0]) * dy
    else:
        x_inc = -1
        n += x - math.floor(end[0])
        error = (start[0] - math.floor(start[0])) * dy
    
    if dy == 0:
        y_inc = 0
        error -= float('inf')
    elif end[1] > start[1]:
        y_inc = 1
        n += math.floor(end[1]) - y
        error -= (math.floor(start[1]) + 1 - start[1]) * dx
    else:
        y_inc = -1
        n += y - math.floor(end[1])
        error -= (start[1] - math.floor(start[1])) * dx
    
    actors = []

    for i in range(n):
        
        for (actor) in actors:
            if (x, y) == actor.position:
                actors.append(actor)

        
        if error > 0:
            y += y_inc
            error -= dx
        else:
            x += x_inc
            error += dy

    return actors

cast_blockmap.__doc__ = """Cast a ray from start to end in woart), (x_end, y_end), worldMap)rld coordinates and return a list of all the map blocks it passes through"""
cast_actors.__doc__ = """Cast a ray from start to end in world coordinates and return a list of all the actors it passes through"""

def main():
    worldMap = map.Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    for i in range(8000):
        x_start = random.randint(0, 320)
        y_start = random.randint(0, 320)
        x_end = random.randint(0, 320)
        y_end = random.randint(0, 320)
        cast_blockmap_first(x_start, y_start, x_end, y_end, worldMap)

def main2():
    import time
    start_x = random.randint(0, 320)
    start_y = random.randint(0, 320)
    end_x = random.randint(0, 320)
    end_y = random.randint(0, 320)
    
    worldMap = map.Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    time1 = time.perf_counter()
    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)

    x = start_x//1
    y = start_y//1

    n = 1
    x_inc, y_inc = 0, 0
    error = 0

    if dx == 0:
        x_inc = 0
        error = float('inf')
    elif end_x > start_x:
        x_inc = 1
        n += (end_x//1) - x
        error = ((start_x//1) + 1 - start_x) * dy
    else:
        x_inc = -1
        n += x - (end_x//1)
        error = (start_x - (start_x//1)) * dy
    
    if dy == 0:
        y_inc = 0
        error -= float("inf")
    elif end_y > start_y:
        y_inc = 1
        n += (end_y//1) - y
        error -= ((start_y//1) + 1 - start_y) * dx
    else:
        y_inc = -1
        n += y - (end_y // 1)
        error -= (start_y - (start_y//1)) * dx
    time2 = time.perf_counter()
    for i in range(int(n)):
        coords = ((x // worldMap.scale), (y // worldMap.scale))
        if (coords[0] > worldMap.height-1 or coords[1] > worldMap.width-1 or coords[0] < 0 or coords[1] < 0):     #check if out of bounds
            #warnings.warn(f"Attempted to read map out of bounds at {coords}")
            time3 = time.perf_counter()
            print(time2 - time1)
            print(time3 - time2)
            return None
        map_value = worldMap.map[coords[1]][coords[0]]

        if map_value != "0":
            time3 = time.perf_counter()
            print(time2 - time1)
            print(time3 - time2)
            return map_value

        if error > 0:
            y += y_inc
            error -= dx
        else:
            x += x_inc
            error += dy

    return 0

if __name__ == "__main__":
    import cProfile as profile
    import random as random
    import time as time
    #profile.run("main()")
    main2()


