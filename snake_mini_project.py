# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import time
import random #We'll need this later in the lab
turtle.bgcolor("black")
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(1000, 1000) #Curious? It's the turtle window  
                        #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
rock_pos = []
rock_stamps = []

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")
scores = turtle.clone()
line = turtle.clone()
line.hideturtle()
line.pencolor("purple")
line.penup()
line.goto(-410, 280)
line.pendown()
line.goto(410, 280)
line.goto(410, -280)
line.goto(-410, -280)
line.goto(-410, 280)
line.penup()
line.goto(0, 400)
line.pendown()
scores.penup()
scores.pencolor("purple")
scores.goto(0, -400)
line.write("Eat, Eat, Eat!", align="center",font=("david", 40, "normal"))
line.penup()
line.goto(0, 0)

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snake_r in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIG#HT!
    x_pos+= SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos, y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_s = snake.stamp()
    stamp_list.append(stamp_s)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    print("you pressed the up key!")

def down():
    global direction
    direction = DOWN
    print("you pressed the down key!")

def left():
    global direction
    direction = LEFT
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("you pressed the right key!")
    
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
x=0

for this_food_pos in food_pos:
    food.goto(food_pos[x])
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    x=x+1
     
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def make_food():
    global food
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    food_stmp = food.stamp()
    food_stamps.append(food_stmp)

score = 0


turtle.register_shape("rock1.gif")
rock = turtle.clone()
rock.shape("rock1.gif")
rock_pos = []
rock_stamps = []
x=0

     
def make_rock():
    global rock
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    rock_x = random.randint(min_x,max_x)*SQUARE_SIZE
    rock_y = random.randint(min_y,max_y)*SQUARE_SIZE
    rock.goto(rock_x, rock_y)
    rock_pos.append(rock.pos())
    rock_stmp = rock.stamp()
    rock_stamps.append(rock_stmp)


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved left!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    new_pos = snake.pos()
    new_x_pos= new_pos[0]
    new_y_pos= new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        line.write("Game over! you are a Loser!", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the right edge! Game over!")
        line.write("Game over! you are a Loser!", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the right edge! Game over!")
        line.write("Game over! you are a Loser!", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the right edge! Game over!")
        line.write("Game over! you are a Loser!", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()

    if snake.pos() in pos_list:
        line.write("Didn't your parents tell you not to eat yourself?!", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()
        print("stupid you, didn't your parents tell you not to eat yourself?!!!")


    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos, score
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        score = score+10
        print(score)
        scores.pendown()
        scores.clear()
        scores.write((score), align = "center", font = ("david", 20, "normal"))
        global TIME_STEP
        TIME_STEP = TIME_STEP-1
        
        
    elif snake.pos() in rock_pos:
        line.write("this is a rock, can't you see?", align = "center", font = ("david" ,30, "normal"))
        time.sleep(3)
        quit()
        
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if len (food_stamps) <=3:
        make_food()

    rock_generator = random.randint(0, 100)
    if rock_generator == 5:
        make_rock()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
snake.color("red")

