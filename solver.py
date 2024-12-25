from copy import deepcopy
from init_cube import Cube
from collections import deque
import time
class RubikSolver:
    def __init__(self, initial_cube):
        
        self.initial_cube = initial_cube
        self.goal_state = initial_cube.goal_state_id
    

    def solve(self, max_depth=20):
        for depth in range(max_depth):
            print(f"Searching with depth limit: {depth}")
            visited = set()
            solution = self._dfs(self.initial_cube, depth, [], visited)
            if solution:
                return solution
        return None  # No solution found within max_depth

    def _dfs(self, cube, depth, path, visited):
        if depth == 0:
            return None

        state_id = cube.code()

        if state_id in visited:
            return None
        visited.add(state_id)

        if cube.is_solved():
            print(len(visited))
            return path
        
        for move, direction in self.initial_cube.moves:
            new_cube = Cube(deepcopy(cube.cube))

            getattr(new_cube, move)(direction)

            new_path = path + [(move, direction)]

            result = self._dfs(new_cube, depth - 1, new_path, visited)
            if result:  
                return result

        return None
    

class RubikSolverBFS:
    def __init__(self, initial_cube):
        self.initial_cube = initial_cube
        self.goal_state = initial_cube.goal_state_id
        self.number_of_cheked_node=0
        self.start_time = time.time()
        

    def solverBfs(self):
        queue = deque([(self.initial_cube, [])])
        visited = set()

        while queue:
            cube, path = queue.popleft()
            state_id = cube.code()
            self.number_of_cheked_node+=1

            if state_id in visited:
                continue
            visited.add(state_id)

            if cube.is_solved():
               
                formatted_solution = []
                for move, direction in path:
                    formatted_solution.append(move.split("_")[1] + ("'" if not direction else ""))
                print("--- %s seconds ---" % round((time.time() - self.start_time), 4))
                return " ".join(formatted_solution)
                

            for move, direction in self.initial_cube.moves:
                new_cube = Cube(deepcopy(cube.cube))
                getattr(new_cube, move)(direction)
                queue.append((new_cube, path + [(move, direction)]))
                # print(queue)

        return None  # No solution found
    