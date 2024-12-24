class Cube:
    def __init__(self, state: dict):
        self.cube = state

    def generate_state_id(self):
        state_id = ""
        for face in ["U", "D", "F", "B", "L", "R"]:
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

    def Rotate_F(self, direction: bool):
        if direction:
            self.rotate_face_clockwise("F")
            temp = self.cube["U"][2]
            self.cube["U"][2] = [self.cube["L"][2 - i][2] for i in range(3)]
            for i in range(3):
                self.cube["L"][i][2] = self.cube["D"][0][i]
                self.cube["D"][0][i] = self.cube["R"][2 - i][0]
                self.cube["R"][i][0] = temp[i]
        else:
            self.rotate_face_counterclockwise("F")
            temp = self.cube["U"][2]
            self.cube["U"][2] = [self.cube["R"][i][0] for i in range(3)]
            for i in range(3):
                self.cube["R"][i][0] = self.cube["D"][0][2 - i]
                self.cube["D"][0][2 - i] = self.cube["L"][i][2]
                self.cube["L"][2 - i][2] = temp[i]

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
        if direction:
            self.rotate_face_clockwise("B")
            temp = self.cube["U"][0]
            self.cube["U"][0] = [self.cube["R"][2 - i][2] for i in range(3)]
            for i in range(3):
                self.cube["R"][i][2] = self.cube["D"][2][2 - i]
                self.cube["D"][2][2 - i] = self.cube["L"][2 - i][0]
                self.cube["L"][i][0] = temp[i]
        else:
            self.rotate_face_counterclockwise("B")
            temp = self.cube["U"][0]
            self.cube["U"][0] = [self.cube["L"][i][0] for i in range(3)]
            for i in range(3):
                self.cube["L"][i][0] = self.cube["D"][2][i]
                self.cube["D"][2][i] = self.cube["R"][2 - i][2]
                self.cube["R"][2 - i][2] = temp[i]

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