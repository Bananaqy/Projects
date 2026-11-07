from Vector import Vector2
import math
from pyray import *

class Turtle :

    def __init__(self, game, pos, direction_facing, colour) : 

        self.game = game
        self.pos = pos
        self.direction_facing = direction_facing
        self.r, self.g, self.b = colour
        self.move_amount = 0
        self.moving = 0
        self.move_amount_amount = 1

    def forward(self, move_amount) :

        if move_amount == "amount" :

            move_amount = self.move_amount

        newpos = Vector2(0, 0)

        newpos.x = self.pos.x +(move_amount * math.cos(math.radians(self.direction_facing)))
        newpos.y = self.pos.y + (move_amount * math.sin(math.radians(self.direction_facing)))

        self.render(newpos)

    def right(self,turn) :

        self.direction_facing += turn

        while self.direction_facing >= 360 :

            self.direction_facing -= 360

    def left(self,turn) :

        self.direction_facing -= turn

        while self.direction_facing < 0 :

            self.direction_facing += 360

    def move(self, pos) :

        self.pos = pos

    def update(self) :

        self.move_amount += self.move_amount_amount
        self.move_amount_amount *= 1.01
        self.moving += 1

        if self.moving > 400 :

            self.game.turtles.remove(self)

    def render(self, newpos):
        draw_line(int(self.pos.x), int(self.pos.y), int(newpos.x), int(newpos.y), (self.r, self.g, self.b))
        self.pos = newpos

    def set_colour(self, r, g, b):

        self.r = r
        self.g = g
        self.b = b