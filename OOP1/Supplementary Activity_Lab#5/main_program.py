from projectilemotion import projectilemotion_solver

initial_speed = 11.0  # m/s
angle_degrees = 20.0  # degrees

range_distance, max_height = projectilemotion_solver(initial_speed, angle_degrees)

print(f"(a) The horizontal distance jumped is: {range_distance:.2f} meters")
print(f"(b) The maximum height reached is: {max_height:.2f} meters")