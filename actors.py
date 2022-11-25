import math
class Actor():
    def __init__(self, position : tuple, direction : tuple):
        self.position = position
        self.direction = direction
    
class Camera(Actor):
    def __init__(self, position : tuple, direction : tuple, view_distance : float):
        super().__init__(position, direction)
        self.view_distance = view_distance
        self.camera_plane = (self.direction[1], -self.direction[0])
        
        direction_length = math.sqrt((self.direction[0] * self.direction[0]) + (self.direction[1] * self.direction[1]))
        self.direction = (self.direction[0] / direction_length, self.direction[1] / direction_length)
        
        self.camera_plane = (self.direction[1], -self.direction[0]) #Turn by 90 degrees right
        
        l_point_x = self.direction[0] - self.camera_plane[0]
        l_point_y = self.direction[1] - self.camera_plane[1]

        r_point_x = self.direction[0] + self.camera_plane[0]
        r_point_y = self.direction[1] + self.camera_plane[1]

        self.left_camera_plane_point = (l_point_x, l_point_y)
        self.right_camera_plane_point = (r_point_x, r_point_y)
    
    def update_camera_plane(self):
        direction_length =((self.direction[0] * self.direction[0]) + (self.direction[1] * self.direction[1])) ** -0.5
        self.direction = (self.direction[0] * direction_length, self.direction[1] * direction_length)
        
        self.camera_plane = (self.direction[1], -self.direction[0]) #Turn by 90 degrees right
        
        l_point_x = self.direction[0] - self.camera_plane[0]
        l_point_y = self.direction[1] - self.camera_plane[1]

        r_point_x = self.direction[0] + self.camera_plane[0]
        r_point_y = self.direction[1] + self.camera_plane[1]

        self.left_camera_plane_point = (l_point_x, l_point_y)
        self.right_camera_plane_point = (r_point_x, r_point_y)
            
class Player(Camera):
    def __init__(self, position : tuple, direction: tuple, speed : float, rotation_speed : float, view_distance : float):
        super().__init__(position, direction, view_distance)
        self.speed = speed
        self.rotation_speed = rotation_speed
    def rotate(self, angle : float):
        #Rotate direction
        new_direction_x = self.direction[0] * math.cos(angle) - self.direction[1] * math.sin(angle)
        new_direction_y = self.direction[0] * math.sin(angle) + self.direction[1] * math.cos(angle)
        self.direction = (new_direction_x, new_direction_y)
        
        self.update_camera_plane()
