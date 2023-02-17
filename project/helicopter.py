from utils import randcell
from map import Map


class Helicopter(Map):
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx = rc[0]
        ry = rc[1]
        self.w = w
        self.h = h
        self.x = rx
        self.y = ry
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.lives = 100

    def move(self, dx, dy):
        nx = self.x + dx
        ny = self.y + dy
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x = nx
            self.y = ny

    def print_stats(self):
        print(f'💧{self.tank}/{self.mxtank}', end='\t')
        print(f'💵{self.score}', end='   ')
        print(f'💛{self.lives}')

    def export_data(self):
        return {
            'score': self.score,
            'lives': self.lives,
            'x': self.x,
            'y': self.y,
            'mxtank': self.mxtank,
            'tank': self.tank
        }

    def import_data(self, data):
        self.score = data['score']
        self.lives = data['lives']
        self.x = data['x']
        self.y = data['y']
        self.mxtank = data['mxtank']
        self.tank = data['tank']
        

