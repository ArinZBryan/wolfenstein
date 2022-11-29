import map as map
import actors as actors
import math

def cast_blockmap_bresenham_first(x0, y0, x1, y1, map : map.Map):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(int(dx) + 1):
        #coords are (x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        coord_x = (x0 + x*xx + y*yx) // map.scale
        coord_y = (y0 + x*xy + y*yy) // map.scale
        if (coord_x > map.height-1 or coord_y > map.width-1 or coord_x < 0 or coord_y < 0):     #check if out of bounds
            return "0"
        value = map.map[coord_y][coord_x]
        if value != "0":
            return value
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return "0"

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
def cast_blockmap_first(start_x : float, start_y : float, end_x : float, end_y : float, map : map.Map): ##All integer divisions by 1 are optimizations over math.floor()
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
            return "0"
        map_value = map.map[coords[1]][coords[0]]

        if map_value != "0":
            return map_value

        if error > 0:
            y += y_inc
            error -= dx
        else:
            x += x_inc
            error += dy
    return "0"
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

if __name__ == "__main__":
    import cProfile as profile
    import random as random
    x1 = random.randint(0, 320)
    x2 = random.randint(0, 320)
    y1 = random.randint(0, 320)
    y2 = random.randint(0, 320)
    WorldMap = map.Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    profile.run("cast_blockmap_bresenham_first(x1, y1, x2, y2, WorldMap)")