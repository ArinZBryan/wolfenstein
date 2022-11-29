import cProfile as profile
import random
import math
import map

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
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

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
def cast_bresenham(start : tuple, end : tuple, map : map.Map):
    points = list(bresenham(start[0], start[1], end[0], end[1]))
    values = []
    for point in points:
        value = map.world_to_map_value(point[0], point[1])
        values.append(value)
    return values
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

def get_first(values : list):
    for value in values:
        if value != "0":
            return value
    return "0"

def main():
    worldMap = map.Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    accuracy = 0
    for i in range(1000):
        start_x = random.randint(0, 320)
        start_y = random.randint(0, 320)
        end_x = random.randint(0, 320)
        end_y = random.randint(0, 320)
        path1 = cast_blockmap((start_x,start_y),(end_x,end_y),worldMap)
        path2 = cast_bresenham((start_x,start_y),(end_x,end_y),worldMap)
        if get_first(path1) == get_first(path2):
            accuracy += 1
    print(accuracy/10)

main()