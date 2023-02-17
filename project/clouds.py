from map import Map
from utils import randbool


class Clouds():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]
    
    def update_clouds(self, r=7, mxr=10, g=4, mxg=10):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(r, mxr):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {
            'cells': self.cells
        }
    
    def import_data(self, data):
        self.cells = data['cells']

