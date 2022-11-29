import math
import warnings
import map as map
import raycast as raycast
import actors as actors
import pygame

def init(width, height):
    pygame.init()
    pygame.display.set_caption("Wolfenstein")
    screen = pygame.display.set_mode((width, height))
    return screen

def render_frame(screen : pygame.Surface, map : map.Map, player : actors.Player):
    log = ""
    screen_size = screen.get_width()
    screen_height = screen.get_height()

    #bg
    screen.fill(0xaaaaaa, (0, 0, screen_size, screen_height/2))
    screen.fill(0x555555, (0, screen_height/2, screen_size, screen_height))
    
    
    player.update_camera_plane()

    #constants per frame
    camera_plane_x = player.right_camera_plane_point[0] - player.left_camera_plane_point[0]
    camera_plane_y = player.right_camera_plane_point[1] - player.left_camera_plane_point[1]

    camera_plane_portion_x = camera_plane_x / screen_size
    camera_plane_portion_y = camera_plane_y / screen_size
    
    
    
    for pixel_x in range(screen_size):
        #calculate ray
        ray_start_x = player.position[0]
        ray_start_y = player.position[1]

        camera_ray_add_x = (camera_plane_portion_x * pixel_x)
        camera_ray_add_y = (camera_plane_portion_y * pixel_x)

        #ray = position -> position + left_point + add 
        
        ##Get point relative to position
        ray_direction_x = player.left_camera_plane_point[0] + camera_ray_add_x
        ray_direction_y = player.left_camera_plane_point[1] + camera_ray_add_y
        ##Make ray of length 1, ray is still relative
        ray_direction_length = ((ray_direction_x * ray_direction_x) + (ray_direction_y * ray_direction_y)) ** -0.5
        ray_direction_x = ray_direction_x * ray_direction_length
        ray_direction_y = ray_direction_y * ray_direction_length
        ##Add player position to ray
        ray_end_x = ray_start_x + ray_direction_x * player.view_distance
        ray_end_y = ray_start_x + ray_direction_y * player.view_distance
        #cast ray
        #Slow -> calculates for all intersections
        #hits = raycast.cast_blockmap(ray_start, ray_end, map)
        #for hit in hits:
        #    if hit == '1':
        #        screen.fill(0x0000ff, (pixel_x, 0, pixel_x+1, 600))
        #        log+=" 1\n"
        #        break
        #    if hit == '2':
        #        screen.fill(0x00ff00, (pixel_x, 0, pixel_x+1, 600))
        #        log+=" 2\n"
        #        break

        #Fast -> calculates for first intersection
        
        hit = raycast.cast_blockmap_bresenham_first(ray_start_x, ray_start_y, ray_end_x, ray_end_y, map)
        log += hit + "\n"
        if hit == '1':
            screen.fill(0x0000ff, (pixel_x, 0, pixel_x+1, 600))
        elif hit == '2':
            screen.fill(0x00ff00, (pixel_x, 0, pixel_x+1, 600))
    fHandle = open("renderlog.log", "a")
    fHandle.write(log)
    fHandle.close()
    pygame.display.flip()
    return
    #logfile = open("renderlog.log", "a")
    #logfile.write(log)
    #logfile.close()
        


