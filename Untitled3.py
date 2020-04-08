#!/usr/bin/env python
# coding: utf-8

# In[10]:


from turtle import *

class MyTurtle(Turtle):
    def drawSquare(self):
        for i in range(4):
          self.right(90)
          self.forward(100)
        
my_turtle = MyTurtle()
my_turtle.forward(100)
my_turtle.drawSquare()

