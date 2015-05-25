"""
Start Project Cars, run python standing.py while doing a race.
"""

import carseour
import time

game = carseour.live()

while True:
    for player in game.standing():
        print(str(player['position']) + '. ' + player['name'] + ' (' + str(player['lap']) + "/" +
              str(game.mLapsInEvent) + ') (' + str(round(player['lap_distance'])) + ')')

    time.sleep(10)
    print("\n\n\n\n")
