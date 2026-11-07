from pyray import *
from raylib import FLAG_MSAA_4X_HINT, FLAG_WINDOW_TOPMOST
from Vector import Vector2
from Turtle import Turtle
import random

set_config_flags(FLAG_MSAA_4X_HINT)

class Main():

    def __init__(self):

        self.width, self.height = 1920, 1080
        init_window(self.width, self.height, "window")
        set_window_state(FLAG_WINDOW_TOPMOST)

        self.turtles = []

        self.turnamount = 150

        self.a = 0


        self.r, self.g, self.b = 180, 33, 100

        #List of good starting colours
        #183, 138, 184
        #176, 231, 230
        #207, 69, 82
        #70, 47, 171
        #50, 150, 250
        #44, 34, 225
        #108, 125, 227
        #113, 30, 138

        self.R, self.G, self.B = 1, 1, 1
        self.x = self.width / 2
        self.y =  self.height / 2

        self.x_ = self.width / 2
        self.y_ =  self.height / 2

        self.speed = 2

        self.X = self.width / 2
        self.Y =  self.height / 2

    def loop(self) :

        while not window_should_close() :

            #begin_texture_mode(self.canvas)
            begin_drawing()

            if is_key_pressed(32):

                self.turnamount = random.random() * 360
                self.r = random.randint(0, 255)
                self.g = random.randint(0, 255)
                self.b = random.randint(0, 255)
                print(self.r, self.g, self.b)

            if is_key_down(87):#w
                self.Y -= self.speed

            if is_key_down(83):#s
                self.Y += self.speed

            if is_key_down(68):#d
                self.X += self.speed

            if is_key_down(65):#a
                self.X -= self.speed

            if is_key_down(265):#up
                self.y -= self.speed

            if is_key_down(264):#down
                self.y += self.speed

            if is_key_down(262):#right
                self.x += self.speed

            if is_key_down(263):#left
                self.x -= self.speed

            if is_key_down(85):#u
                self.y_ -= self.speed

            if is_key_down(74):#j
                self.y_ += self.speed

            if is_key_down(75):#k
                self.x_ += self.speed

            if is_key_down(72):#h
                self.x_ -= self.speed

            #makes the middle the mouse
            #can remove if needed
            
            # self.x = get_mouse_position().x
            # self.y = get_mouse_position().y


            self.turtles.append(Turtle(self, Vector2(self.x, self.y), self.a, (self.r, self.g, self.b)))
            self.turtles.append(Turtle(self, Vector2(self.X, self.Y), self.a, (self.r, self.g, self.b)))
            self.turtles.append(Turtle(self, Vector2(self.x_, self.y_), self.a, (self.r, self.g, self.b)))

            self.turnamount += (1 / 500)

            if self.turnamount > 360 :

                self.turnamount -= 360

            self.move()
            self.check()

            end_drawing()

    def move(self) :

        for turtle in self.turtles :

            turtle.update()
            turtle.right(self.turnamount)
            turtle.forward("amount")

    def check(self) :

        self.r += self.R
        self.g += self.G
        self.b += self.B

        if self.r == 255 :

            self.R = -1

        elif self.r == 0 :

            self.R = 1

        if self.g == 255 :

            self.G = -1

        elif self.g == 0 :

            self.G = 1

        if self.b == 255 :

            self.B = -1

        elif self.b == 0 :

            self.B = 1
            
Main().loop()

        