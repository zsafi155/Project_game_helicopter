import os
from utils import randbool, randcell, randcell2

#💼🏆
CELL_TYPES = '💠🌲🌊🔥🏪🏥'
TREE_BONUS = 300
UPGRADE_COST = 500
LIFE_COST = 100

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

    def print_map(self, helico, clouds):
        print('▭ ' * (self.w + 2))
        for i in range(self.h):
            print('▭ ', end='')
            for j in range(self.w):
                if clouds.cells[i][j] == 1:
                    print('🔳', end='')
                elif clouds.cells[i][j] == 2:
                    print('🔲', end='')
                elif helico.x == i and helico.y == j:
                    print('🚁', end='')
                else:
                    cell = self.cells[i][j]
                    print(CELL_TYPES[cell], end='')
            print('▭')
        print('▭ ' * (self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def generate_forest(self, r=5, mxr=10):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2 = rc2[0]
            ry2 = rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] =2
                rx = rx2
                ry = ry2
                l -= 1

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx = c[0]
        cy = c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx = c[0]
        cy = c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 3

    def update_fires(self, helico):
        for i in range(self.h):
            for j in range(self.w):
                cell = self.cells[i][j]
                if cell == 3:
                    self.cells[i][j] = 0
                    if helico.score >= 100:
                        helico.score -= 100
        for i in range(30):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        elif c == 3 and helico.tank > 0:
            helico.tank -= 1
            self.cells[helico.x][helico.y] = 1
            helico.score += TREE_BONUS
        elif c == 4 and helico.score >= UPGRADE_COST:
            helico.score -= UPGRADE_COST
            helico.mxtank += 1
        elif c == 5 and helico.score >= LIFE_COST and helico.lives <= 100:
            helico.score -= LIFE_COST
            helico.lives += 10
        if d == 2:
            helico.lives -= 1
            if helico.lives <= 0:
                os.system('cls')
                print(f'GAME OVER :( YOUR SCORE IS {helico.score}')
                exit(0)            
    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx = c[0]
        cy = c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx = c[0]
        cy = c[1]
        if self.cells[cx][cy] == 4:
            self.generate_hospital()
        else:
            self.cells[cx][cy] = 5

    def export_data(self):
        return {
            'cells': self.cells
        }

    def import_data(self, data):
        self.cells = data['cells']