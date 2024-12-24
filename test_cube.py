from init_cube import Cube
initial_state = {
    "U": [['U', 'U', 'U'], ['U', 'U', 'U'],['U', 'U', 'U']],
    "D": [['D', 'D', 'D'], ['D', 'D', 'D'], ['D', 'D', 'D']],
    "F": [['F', 'F', 'F'], ['F', 'F', 'F'], ['F', 'F', 'F']],
    "B": [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
    "L": [['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L']],
    "R": [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
}

cube = Cube(initial_state)

def print_cube(cube):
    for face, grid in cube.cube.items():
        print(f"{face}:")
        for row in grid:
            print(row)
    print("\n")

print("Initial State:")
print_cube(cube)

print("Rotate U clockwise:")
cube.Rotate_U(direction=True)
print_cube(cube)

print("Rotate L counterclockwise:")
cube.Rotate_L(direction=False)
print_cube(cube)

print("Rotate F clockwise:")
cube.Rotate_F(direction=True)
print_cube(cube)

print("Rotate D counterclockwise:")
cube.Rotate_D(direction=False)
print_cube(cube)