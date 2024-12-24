from init_cube import Cube
# initial_state = {
#     'U': [['R', 'U', 'U'],
#           ['F', 'U', 'U'],
#           ['L', 'L', 'L']],

#     'L': [['F', 'L', 'B'],
#           ['F', 'L', 'D'],
#           ['F', 'F', 'R']],

#     'F': [['D', 'D', 'D'],
#           ['F', 'F', 'R'],
#           ['U', 'R', 'R']],

#     'R': [['F', 'B', 'B'],
#           ['U', 'R', 'R'],
#           ['B', 'B', 'U']],

#     'B': [['L', 'L', 'U'],
#           ['B', 'B', 'U'],
#           ['F', 'L', 'D']],

#     'D': [['F', 'D', 'D'],
#           ['R', 'D', 'D'],
#           ['R', 'B', 'L']],

# }
g_state = {
    "U": [
        ['U', 'U', 'U'],['U', 'U', 'U'],['U', 'U', 'U']],
    "D": [
        ['D', 'D', 'D'],['D', 'D', 'D'],['D', 'D', 'D']],
    "F": [
        ['F', 'F', 'F'],['F', 'F', 'F'],['F', 'F', 'F']],
    "B": [
        ['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']],
    "L": [
        ['L', 'L', 'L'],['L', 'L', 'L'],['L', 'L', 'L']],
    "R": [
        ['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']]
}



def print_cube(cube):
    for face, grid in cube.cube.items():
        print(f"{face}:")
        for row in grid:
            print(row)
    print("\n")

cube = Cube(g_state)
# print(cube.code())
z=cube
# cube.Rotate_D(direction=True)
# cube.Rotate_L(direction=False)
# cube.Rotate_F(direction=True)
# cube.Rotate_B(direction=False)
# cube.Rotate_F(direction=True)
# cube.Rotate_R(direction=False)
# print(cube.cube)
# print(z.code())
cube.rando_moves(3)
# cube.Rotate_R(direction=True)
# cube.Rotate_B(direction=False)
# cube.Rotate_F(direction=True)

# cube.Rotate_F(direction=False)
# cube.Rotate_B(direction=True)
# cube.Rotate_R(direction=False)
# cube.Rotate_D(direction=False)


# # cube.Rotate_F(direction=True)
# # cube.Rotate_F(direction=True)
# print(cube.is_solved())
# # print(cube.code())










# # print("Initial State:")
# # print_cube(cube)

# print("Rotate U clockwise:")
# # cube.Rotate_U(direction=True)
# # print_cube(cube)

# print("Rotate L counterclockwise:")
# # cube.Rotate_L(direction=False)
# # print_cube(cube)

# print("Rotate F clockwise:")
# # cube.Rotate_F(direction=True)
# # print_cube(cube)

# print("Rotate D counterclockwise:")
# # cube.Rotate_D(direction=False)
# # print_cube(cube)


# print('#-------------')

# print("Rotate D counterclockwise:")
# cube.Rotate_D(direction=True)
# # print_cube(cube)

# print("Rotate F clockwise:")
# cube.Rotate_F(direction=False)
# # print_cube(cube)

# print("Rotate L counterclockwise:")
# cube.Rotate_L(direction=True)
# # print_cube(cube)

# print("Rotate U clockwise:")
# cube.Rotate_U(direction=False)
# # print_cube(cube)

# print(cube.code())
# print(cube.goal_state_id)
# print(cube.is_solved())