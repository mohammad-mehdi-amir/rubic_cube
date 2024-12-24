from solver import RubikSolver,RubikSolverBFS
from init_cube import Cube
import time
start_time = time.time()
cube = Cube()

# cube.rando_moves(3)
# solver = RubikSolver(cube)

# solution = solver.solve(max_depth=10)
# def print_solution(solution):
#     formatted_solution = []
#     for move, direction in solution:
#         formatted_solution.append(move.split("_")[1] + ("'" if not direction else ""))
    
#     print(" ".join(formatted_solution))
# if solution:
#     print_solution(solution)
# else:
#     print("No solution found.")
    
    
cube1 = Cube()
cube1.rando_moves(4)
solver = RubikSolverBFS(cube1)

solution = solver.solve()
def print_solution(solution):
    formatted_solution = []
    for move, direction in solution:
        formatted_solution.append(move.split("_")[1] + ("'" if not direction else ""))
    
    print(" ".join(formatted_solution))
if solution:
    print_solution(solution)
    print(solver.number_of_cheked_node)
else:
    print("No solution found.")
print("--- %s seconds ---" % round((time.time() - start_time), 4))