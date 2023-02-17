import json
import os
from map import Map
import time
from pynput import keyboard
from helicopter import Helicopter
from clouds import Clouds

MAP_W = 20
MAP_H = 20
tick = 0
TICK_SLEEP = 0.5
TREE_UPDATE = 30
FIRE_UPDATE = 50
CLOUDS_UPDATE = 20

c = Map(MAP_W, MAP_H)
helico = Helicopter(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
c.generate_forest(1, 10)
c.generate_river(10)
c.generate_river(15)
c.generate_river(20)
c.generate_river(10)
c.generate_upgrade_shop()
c.generate_hospital()
c.print_map(helico, clouds)

MOVES = {'w':(-1, 0), 'd':(0, 1),'s':(1, 0),'a':(0, -1)}
def on_release(key):
    global helico, tick
    ch = key.char.lower()
    if ch in MOVES.keys():
        dx = MOVES[ch][0]
        dy = MOVES[ch][1]
        helico.move(dx, dy)

    elif ch == 'f':
        data = {
            'helicopter': helico.export_data(),
            'clouds': clouds.export_data(),
            'map': c.export_data(),
            'tick': tick
        }

        with open('lvl.json', 'w') as lvl:
            json.dump(data, lvl)

    elif ch == 'g':
        with open('lvl.json', 'r') as lvl:
            data = json.load(lvl)
        tick = data['tick']
        helico.import_data(data['helicopter'])
        clouds.import_data(data['clouds'])
        c.import_data(data['map'])
listener  = keyboard.Listener (
    on_release=on_release)
listener.start()

while 1:
    os.system('cls')
    c.process_helicopter(helico, clouds)
    helico.print_stats()
    c.print_map(helico, clouds)
    print(f'TICK {tick}')
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        c.generate_tree()
    if tick % FIRE_UPDATE == 0:
        c.update_fires(helico)
    if tick % CLOUDS_UPDATE == 0:
        clouds.update_clouds(2, 10, 1, 10)
        