import random
class Cube:
    def __init__(self, state: dict={
    "U": [['U', 'U', 'U'],['U', 'U', 'U'],['U', 'U', 'U']],
    "D": [['D', 'D', 'D'],['D', 'D', 'D'],['D', 'D', 'D']],
    "F": [['F', 'F', 'F'],['F', 'F', 'F'],['F', 'F', 'F']],
    "B": [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']],
    "L": [['L', 'L', 'L'],['L', 'L', 'L'],['L', 'L', 'L']],
    "R": [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']]},number_of_random_move=3):
        self.cube = state
        self.code_id=self.code()
        self.goal_state_id="UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD"
        self.rando_moves=number_of_random_move
        self.moves = [
            ("Rotate_U", True), ("Rotate_U", False),
            ("Rotate_L", True), ("Rotate_L", False),
            ("Rotate_F", True), ("Rotate_F", False),
            ("Rotate_R", True), ("Rotate_R", False),
            ("Rotate_B", True), ("Rotate_B", False),
            ("Rotate_D", True), ("Rotate_D", False),
        ]
    def code(self):
        state_id = ""
        for face in ["U", "L", "F", "R", "B", "D"]:
            for row in self.cube[face]:
                state_id += "".join(map(str, row))
        return state_id
  
    
    def rotate_face_clockwise(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def rotate_face_counterclockwise(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

    def Rotate_U(self, direction: bool):
        if direction:
            self.rotate_face_clockwise("U")
            temp = self.cube["F"][0]
            self.cube["F"][0] = self.cube["R"][0]
            self.cube["R"][0] = self.cube["B"][0]
            self.cube["B"][0] = self.cube["L"][0]
            self.cube["L"][0] = temp
        else:
            self.rotate_face_counterclockwise("U")
            temp = self.cube["F"][0]
            self.cube["F"][0] = self.cube["L"][0]
            self.cube["L"][0] = self.cube["B"][0]
            self.cube["B"][0] = self.cube["R"][0]
            self.cube["R"][0] = temp

    def Rotate_L(self, direction: bool):
        if direction:
            self.rotate_face_clockwise("L")
            temp = [row[0] for row in self.cube["F"]]
            for i in range(3):
                self.cube["F"][i][0] = self.cube["U"][i][0]
                self.cube["U"][i][0] = self.cube["B"][2 - i][2]
                self.cube["B"][2 - i][2] = self.cube["D"][i][0]
                self.cube["D"][i][0] = temp[i]
        else:
            self.rotate_face_counterclockwise("L")
            temp = [row[0] for row in self.cube["F"]]
            for i in range(3):
                self.cube["F"][i][0] = self.cube["D"][i][0]
                self.cube["D"][i][0] = self.cube["B"][2 - i][2]
                self.cube["B"][2 - i][2] = self.cube["U"][i][0]
                self.cube["U"][i][0] = temp[i]

    def Rotate_F(self, direction=True):
        if direction:  # Clockwise rotation
            self.rotate_face_clockwise("F")
            
            # Temporary variables for swapping edges
            u_row = self.cube["U"][2]
            l_col = [self.cube["L"][i][2] for i in range(3)]
            d_row = self.cube["D"][0]
            r_col = [self.cube["R"][i][0] for i in range(3)]

            # Perform the swap in clockwise direction
            self.cube["U"][2] = l_col[::-1]
            for i in range(3):
                self.cube["L"][i][2] = d_row[i]
            self.cube["D"][0] = r_col[::-1]
            for i in range(3):
                self.cube["R"][i][0] = u_row[i]
        else:  # Counterclockwise rotation
            self.rotate_face_counterclockwise("F")
            
            # Temporary variables for swapping edges
            u_row = self.cube["U"][2]
            l_col = [self.cube["L"][i][2] for i in range(3)]
            d_row = self.cube["D"][0]
            r_col = [self.cube["R"][i][0] for i in range(3)]

            # Perform the swap in counterclockwise direction
            self.cube["U"][2] = r_col
            for i in range(3):
                self.cube["R"][i][0] = d_row[::-1][i]
            self.cube["D"][0] = l_col
            for i in range(3):
                self.cube["L"][i][2] = u_row[::-1][i]

    def Rotate_R(self, direction: bool):
        if direction:
            self.rotate_face_clockwise("R")
            temp = [row[2] for row in self.cube["F"]]
            for i in range(3):
                self.cube["F"][i][2] = self.cube["U"][i][2]
                self.cube["U"][i][2] = self.cube["B"][2 - i][0]
                self.cube["B"][2 - i][0] = self.cube["D"][i][2]
                self.cube["D"][i][2] = temp[i]
        else:
            self.rotate_face_counterclockwise("R")
            temp = [row[2] for row in self.cube["F"]]
            for i in range(3):
                self.cube["F"][i][2] = self.cube["D"][i][2]
                self.cube["D"][i][2] = self.cube["B"][2 - i][0]
                self.cube["B"][2 - i][0] = self.cube["U"][i][2]
                self.cube["U"][i][2] = temp[i]

    def Rotate_B(self, direction: bool):
        if direction:  # Clockwise rotation
            self.rotate_face_clockwise("B")
            
            temp = self.cube["U"][0]
            self.cube["U"][0] = [self.cube["R"][i][2] for i in range(3)][::-1]
            for i in range(3):
                self.cube["R"][i][2] = self.cube["D"][2][i]
            self.cube["D"][2] = [self.cube["L"][i][0] for i in range(3)][::-1]
            for i in range(3):
                self.cube["L"][i][0] = temp[i]
        else:  # Counterclockwise rotation
            self.rotate_face_counterclockwise("B")
            
            temp = self.cube["U"][0]
            self.cube["U"][0] = [self.cube["L"][i][0] for i in range(3)]
            for i in range(3):
                self.cube["L"][i][0] = self.cube["D"][2][2 - i]
            self.cube["D"][2] = [self.cube["R"][i][2] for i in range(3)]
            for i in range(3):
                self.cube["R"][i][2] = temp[2 - i]

    def Rotate_D(self, direction: bool):
        if direction:
            self.rotate_face_clockwise("D")
            temp = self.cube["F"][2]
            self.cube["F"][2] = self.cube["L"][2]
            self.cube["L"][2] = self.cube["B"][2]
            self.cube["B"][2] = self.cube["R"][2]
            self.cube["R"][2] = temp
        else:
            self.rotate_face_counterclockwise("D")
            temp = self.cube["F"][2]
            self.cube["F"][2] = self.cube["R"][2]
            self.cube["R"][2] = self.cube["B"][2]
            self.cube["B"][2] = self.cube["L"][2]
            self.cube["L"][2] = temp
    
    
    def is_solved(self):
        if self.code() == self.goal_state_id:
            return True
        else:
            return False
        
    def rando_moves(self):
        for _ in range(self.rando_moves):
           ch=random.choice(self.moves)
           print(ch)
           getattr(self,f'{ch[0]}')(ch[1]) 
        
        
       