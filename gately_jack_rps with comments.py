# This file was created by: Jack Gately on 9/1/2023



# imports a random number
from random import randint 


# import turtle
import turtle
from turtle import *


# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))


# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170




# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0
# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)


# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0
# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()
# add the scissors image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = 300
scissors_pos_y = 0
# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)






def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(cpu_rock_image)
    # attach the rock_image to the rock_instance
    cpu_rock_instance.shape(cpu_rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    cpu_rock_instance.penup()
    # set the position of the rock_instance
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(cpu_paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(cpu_paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)    

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(cpu_scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(cpu_scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)




# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('black')
text.hideturtle()
turtle.penup
turtle.up()

# hide turtle
t.hideturtle()

show_rock(-300, 0)
show_paper(0,0)
show_scissors(300,0)






    





# this function uses and x y value, an obj, and width and height to determine whether or not the mouse is colliding with the object
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
    
# this function uses randint to determine the cpu selection
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]


# Imports a time system which is being used to stop the code temporarily
import time

time.sleep(0.5)



# mouse position function for determining if there is a collision between objects

def mouse_pos(x, y):
    print("window geometry " + str(cv.winfo_geometry()))
    print("the paper x position is " + str(rock_instance.pos()[0]))
    print("the paper y position is " + str(rock_instance.pos()[1]))
    print(cpu_select())
    cpu_picked = cpu_select()
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("You Chose Rock!")
        player_choice = "rock..."
        text.penup()
        text.goto(-400, 150)
        text.write("You Chose Rock!", False, "left", ("Arial", 20, "normal"))
        # Logic for the computer choosing rock and the player choosing rock - results in a tie
        if cpu_picked == "rock":
            text.goto(0, 150)
            text.write("The Computer Chose Rock!", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing paper and the player choosing rock - results in a player loss
        elif cpu_picked == "paper":
            text.goto(0, 150)
            text.write("The Computer Chose Paper!", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing scissors and the player choosing rock - results in a player win
        elif cpu_picked == "scissors":
            text.goto(0, 150)
            text.write("The Computer Chose Scissors", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("You Win!", False, "left", ("Arial", 24, "normal"))
    elif collide(x,y,paper_instance,paper_w,paper_h):
        print("You Chose Paper!")
        player_choice = "paper..."
        text.penup()
        text.goto(0, 150)
        text.write("You Chose Paper!", False, "left", ("Arial", 20, "normal"))
        # Logic for the computer choosing rock and the player choosing paper - results in a player win
        if cpu_picked == "rock":
            text.goto(-400, -175)
            text.write("The Computer Chose Rock", False, "left", ("Arial", 20, "normal"))
            text.goto(150,-175)
            time.sleep(1.5)
            text.write("You Win!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing paper and the player choosing paper - results in a tie
        elif cpu_picked == "paper":
            text.goto(-400, -175)
            text.write("The Computer Chose Paper", False, "left", ("Arial", 20, "normal"))
            text.goto(150,-175)
            time.sleep(1.5)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing scissors and the player choosing paper - results in a player loss
        elif cpu_picked == "scissors":
            text.goto(-400, -175)
            text.write("The Computer Chose Scissors", False, "left", ("Arial", 20, "normal"))
            text.goto(150,-175)
            time.sleep(1.5)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        print("You Chose Scissors!")
        player_choice = "scissors..."
        text.penup()
        text.goto(200, 150)
        text.write("You Chose Scissors!", False, "left", ("Arial", 20, "normal"))
        # Logic for the computer choosing rock and the player chossing scissors - results in a player loss
        if cpu_picked == "rock":
            text.goto(-400, 150)
            text.write("The Computer Chose Rock", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing paper and the player choosing scissors - results in a player win
        elif cpu_picked == "paper":
            text.goto(-400, 150)
            text.write("The Computer Chose Paper", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("You Win!", False, "left", ("Arial", 24, "normal"))
        # Logic for the computer choosing scissors and the player choosing scissors - results in a tie
        elif cpu_picked == "scissors":
            text.goto(-400, 150)
            text.write("The Computer Chose Scissors", False, "left", ("Arial", 20, "normal"))
            text.goto(0,-175)
            time.sleep(1.5)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
    # If the player fails to make a selection or does not click rock paper or scissors, print...
    else: 
        print("Please Choose Rock, Paper, Or Scissors...")


    time.sleep(4)
    
    text.clear()




    

    
    





# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()




















