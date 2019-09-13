# Globals for the bearings
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self._x = x
        self._y = y
        self.coordinates = (self._x, self._y)

    @property
    def bearing(self):
        return self._bearing

    @bearing.setter
    def bearing(self, direction):
        if str(direction).upper() == 'N':
            self._bearing = 'NORTH'
        elif str(direction).upper() == 'E':
            self._bearing = 'EAST'
        elif str(direction).upper() == 'W':
            self._bearing = 'WEST'
        elif str(direction).upper() == 'S':
            self._bearing = 'SOUTH'

    def turn_right(self):
        if self._bearing == 'N':
            self._bearing = 'E'
        elif self._bearing == 'E':
            self._bearing = 'S'
        elif self._bearing == 'S':
            self._bearing = 'W'
        elif self._bearing == 'W':
            self._bearing = 'N'

    def turn_left(self):
        if self._bearing == 'N':
            self._bearing = 'W'
        elif self._bearing == 'W':
            self._bearing = 'S'
        elif self._bearing == 'S':
            self._bearing = 'E'
        elif self._bearing == 'E':
            self._bearing = 'N'

    def simulate(self, movement):
        # For every command in movement param, call the methods to execute robot movement
        for command in movement:
            if command == 'R':
                self.turn_right()
            elif command == 'L':
                self.turn_left()
            elif command == 'A':
                self.advance()
            else:
                raise Exception("This Robot can't do this movement!")
        return self.coordinates

    def advance(self):
        # Check bearing and update the cordinates property X and Y
        if self._bearing == 'N':
            self._y += 1
        elif self._bearing == 'E':
            self._x += 1
        elif self._bearing == 'S':
            self._y -= 1
        elif self._bearing == 'W':
            self._x -= 1
        # update cordinates tuple
        self.coordinates = (self._x, self._y)
