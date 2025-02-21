import math

def projectilemotion_solver(initial_speed, angle_degrees):
    g = 9.81  
    
    angle_radians = math.radians(angle_degrees)
    
    range_distance = (initial_speed**2 * math.sin(2 * angle_radians)) / g
    
    max_height = (initial_speed**2 * (math.sin(angle_radians))**2) / (2 * g)
    
    return range_distance, max_height