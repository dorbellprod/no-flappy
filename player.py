import random

PLAYER_X = 400
PIPE_GAP_START = 445 # The topmost y coordinate in the gap, relative to the pipes' y position.
PIPE_GAP_END = 726 # The bottommost y coordinate in the gap, relative to the pipes' y position.

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.yvel = 5
        self.width = width
        self.height = height

    def update(self, gravity):
        self.y += self.yvel
        self.yvel += gravity

class Pipe:
    def __init__(self, x, width, height):

        self.x = x # Starts rendering from the top-left, so set x to leftmost x coordinate
        self.randomize()
        self.width = width
        self.height = height
    def update(self):
        self.x -= 3 # Moves left!!! BASED!!!
        if self.x <= -self.width:
            self.randomize()
            self.x = 800 + self.width
            return True
        return False
    def randomize(self):
        self.y = random.randint(-390, 0)
    def check_collisions(self, player: Player): # We take in a reference to the player.
        '''
            Hard-coded collision logic.
            We render the pipe differently than we render the player; The x and y coordinates represent the top-left of
            the pipe sprite. Therefore, we should add the width to the self.x coordinate when checking whether the player has
            passed the pipe, as it would take that many pixels past the leftmost x coordinate to do so.
        '''

        # Check if self.x is within the bounds of (player.x - [half of width], player.x + [half of width])
        colliding_x = (self.x < player.x + player.width / 2) and (self.x + self.width > player.x - player.width / 2)

        # Check if player.y is NOT within the gap of the pipes, relative to self.y, which is defined by 2 constants.
        colliding_y = not ((player.y - player.height / 2 > self.y + PIPE_GAP_START) and (player.y + player.height / 2 < self.y + PIPE_GAP_END))

        return colliding_x and colliding_y # `False` if in the gap; `True` otherwise.
