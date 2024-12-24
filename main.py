from solver import RubikSolverBFS
from init_cube import Cube
import time
start_time = time.time()

cube1 = Cube()

solver = RubikSolverBFS(cube1)
print(solver.solve())


