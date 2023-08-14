import turtle
import time
import random


delay = 0.1
score = 0
highest_score = 0
new_game= None

# Display configuration
s = turtle.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Game: Snake")
s.tracer(0)  

# Difficulty level options
difficulty_levels = ["Fácil", "Medio", "Difícil"]
selected_difficulty = None

#Functions for difficulty levels
def set_easy(x,y):
    global delay
    delay = 0.15
    global selected_difficulty
    selected_difficulty = "Easy"

def set_medium(x,y):
    global delay
    delay = 0.1
    global selected_difficulty
    selected_difficulty = "Medium"

def set_hard(x,y):
    global delay
    delay = 0.05
    global selected_difficulty
    selected_difficulty = "hard"

#Functions: snake directions
def up():
    snake.direction = 'up'

def down():
    snake.direction = 'down'

def right():
    snake.direction = 'right'

def left():
    snake.direction = 'left'

#Function for snake movements
def movement():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

#Function that restarts the game once the player loses a game.
def newgame(x,y):
    global new_game
    new_game= True
    # Ocultar elementos de Game Over y botón de nuevo juego
    gameover.clear()
    gameover.hideturtle()
    newgame_button.clear()
    newgame_button.hideturtle()

     # Restaurar el juego
    food.showturtle()
    snake.showturtle()
    snake.home()
    snake.direction = 'stop'
    for b in body:
        b.clear()
        b.hideturtle()
    body.clear()

    # Restablecer puntuación y actualizar el texto
    global score
    score = 0
    text.clear()
    text.write("Score: {}\t Highest Score: {}".format(score, highest_score), align="center", font=("verdana", 20, "normal"))

    # Iniciar el juego nuevamente
    s.update()
    
    
#End-of-game display function when a player loses a game
def game_over():
    snake.hideturtle()
    food.hideturtle()

    global gameover
    gameover = turtle.Turtle()
    gameover.speed(0)
    gameover.color('white')
    gameover.penup()
    gameover.hideturtle()
    gameover.goto(0, 50)
    gameover.write("Game Over!", align="center", font=("verdana", 50, "normal"))

    global newgame_button
    newgame_button=turtle.Turtle()
    newgame_button.speed(0)
    newgame_button.color('green')
    newgame_button.shape('arrow')
    newgame_button.shapesize(0.4)
    newgame_button.penup()
    newgame_button.goto(0,0)
    newgame_button.write("New Game", align="center", font=("verdana", 20, "normal"))
    newgame_button.onclick(newgame)

#Welcome screen configuration
welcome = turtle.Turtle()
welcome.speed(0)
welcome.color('white')
welcome.penup()
welcome.hideturtle()
welcome.goto(0, 100)
welcome.write("Welcome to my Snake Game!", align="center", font=("verdana", 30, "normal"))
welcome.goto(0, 0)
welcome.write("Select a difficulty level:", align="center", font=("verdana", 18, "normal"))

#Button configuration for difficulty levels
easy_button=turtle.Turtle()
easy_button.speed(0)
easy_button.color('green')
easy_button.shape('arrow')
easy_button.shapesize(0.4)
easy_button.penup()
easy_button.goto(-150,-50)
easy_button.write("Easy", align="center", font=("verdana", 20, "normal"))
easy_button.onclick(set_easy)

medium_button= turtle.Turtle()
medium_button.speed(0)
medium_button.color('orange')
medium_button.shape('arrow')
medium_button.shapesize(0.4)
medium_button.penup()
medium_button.goto(0,-50)
medium_button.write("Medium", align="center", font=("verdana", 20, "normal"))
medium_button.onclick(set_medium)

hard_button=turtle.Turtle()
hard_button.speed(0)
hard_button.color('red')
hard_button.shape('arrow')
hard_button.shapesize(0.4)
hard_button.penup()
hard_button.goto(150,-50)
hard_button.write("Hard", align="center", font=("verdana", 20, "normal"))
hard_button.onclick(set_hard)

while selected_difficulty is None:
    s.update()

# Clear the welcome screen and buttons
welcome.clear()
easy_button.clear()
medium_button.clear()
hard_button.clear()
easy_button.hideturtle()
medium_button.hideturtle()
hard_button.hideturtle()



#Creating the snake
snake = turtle.Turtle()
snake.speed(1)
snake.shape('square')
snake.color('green')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#Creating the food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
food.speed(0)

body = []

#Text displaying the score and the highest score
text= turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,-280)
text.write("Score: 0 \t Highest score: 0", align="center", font=("verdana",20, "normal"))

#Capturing keystrokes for snake movements
s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")

#Game Logic Code 
while True:
    s.update()
    
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -220:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        
        game_over()
        while new_game is None:
            s.update()
        new_game= None

    if snake.distance(food)<20:
        x=random.randint(-250,250)
        y=random.randint(-240,250)
        food.goto(x,y)

        new_body=turtle.Turtle()
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)

        score+=10
        if score > highest_score:
            highest_score=score
            text.clear()
            text.write("Score: {}\t Highest Score: {}".format(score,highest_score), align="center", font=("verdana", 20, "normal"))



    size=len(body)
    for i in range(size -1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
        
    if size > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x,y)
        

    movement()

    for i in body:
        if i.distance(snake) < 20:
            game_over()
            while new_game is None:
                s.update()
            new_game= None
            
            
    time.sleep(delay)

turtle.done()