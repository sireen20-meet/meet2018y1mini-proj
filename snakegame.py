import turtle
import random #We'll need this later in the lab
import time
turtle.bgcolor("black")
game_over=turtle.clone()
game_over.hideturtle()
game_over.color("red")




lines = turtle.clone()


lines.penup()


lines.hideturtle()

lines.goto(0,300)
lines.pendown()
lines.pencolor("white")
lines.write("~~Snake game~~", align='center', font=("Arial",30,"normal"))
lines.penup()
lines.goto(0,250)
lines.pendown()
lines.goto(400,250)
lines.goto(400,-250)
lines.goto(-400,-250)
lines.goto(-400,250)
lines.goto(0,250)
lines.penup()


turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=740
SIZE_Y=450
turtle.setup(1000, 1000)  #Curious? It's the turtle window  


turtle.penup()


SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.pencolor("yellow")
snake.shape("square")


#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)




for snakepos in range(START_LENGTH) :
    x_pos=snake.pos()[0]#Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_id= snake.stamp()
    stamp_list.append(stamp_id)

UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


#SSSSS

direction = UP


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
   #Update the snake drawing <- remember me later
    print("You pressed the up key!")


def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the down key!")

def  right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    #Update the snake drawing <- remember me later
    print("You pressed the  right key!")


def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
   #Update the snake drawing <- remember me later
    print("You pressed the left key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

    

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)# Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()


#######################makefood

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    food_stamps.append(food.stamp())
    

    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    ##                        position 
    ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
def make_rock():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    rock_x = random.randint(min_x,max_x)*SQUARE_SIZE
    rock_y = random.randint(min_y,max_y)*SQUARE_SIZE
    rock.goto(rock_x,rock_y)
    rock_pos.append((rock_x,rock_y))
    rock.stamp()
i=0
score=turtle.clone()
score.pencolor("white")
def move_snake():

    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        make_food()
        
        global i
        i = i + 1
        print(i)
        score.penup()
        score.color("blue")
        score.goto(-395,-250)
        score.pendown()
        score.clear()
        score.write(i, font=("Arial", 18, "normal"))

        if i % 5 == 0:
            make_rock()
    
    else:
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
        #333333333333
    
    
        ############################################################################

    
    
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
        snake.goto(x_pos ,y_pos  +SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos , y_pos- SQUARE_SIZE)
        print("You moved down!")
    
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    if snake.pos() in pos_list[:-1] :
        snake_ind = pos_list.index(snake.pos()) #What does this do?
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()

    if snake.pos() in rock_pos:
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()
    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
        '''
    if snake.pos() in food_pos:
        my_pos=snake.pos() 
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        
        lines.write(i)
        '''
    

    
    
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
   
       
    
    
        

    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()
        
        #Add new lines to the end of the function
    #Grab position of snake


    # The next three lines check if the snake is hitting the 
    # right edge.
    
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()
        
#Add new lines to the end of the function
    #Grab position of snake


    # The next three lines check if the snake is hitting the 
    # right edge.
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the Down edge! Game over!")
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()

        #Add new lines to the end of the function
    #Grab position of snake


    # The next three lines check if the snake is hitting the 
    # right edge.
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        turtle.bgcolor("red")
        game_over.color("white")
        game_over.write("GAME OVER",align='center', font=("Impact", 100, "normal"))
        time.sleep(10)
        quit()
    
    
        
    turtle.ontimer(move_snake,TIME_STEP)



    





turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script
turtle.register_shape("18c.gif")
rock = turtle.clone()
food = turtle.clone()
food.shape("trash.gif") 
rock.shape("18c.gif")
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
rock_pos = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!

for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())


move_snake()
    
