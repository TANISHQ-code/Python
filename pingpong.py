import turtle

#Players:
Player_A=input("Player A pls enter your name")
Player_B=input("Player B pls input your name")
print("press 'Q' to exit")

#screeen setup
win=turtle.Screen() #creation of screen
win.title("Ping Pong")#title o window
win.bgcolor("black")#background color
win.setup(width=800,height=600)#window size
win.tracer(0) #stops the window from updating itself helps in speeding up the game

#objects

#Paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0) #not the spped of paddle A its just the speed for animation (sets it to max speed so that the game runs on the max speed)
paddle_a.shape("square")#20x20 px   
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #increses paddle width to 5 times(100px) and length same(20px)
paddle_a.color("white")
paddle_a.penup() #stops the turtle module from leaving the line as the object moves
paddle_a.goto(-350,0)

#paddle  B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5 #everytime the ball moves it moves by 2 pixels by x
ball.dy = 0.5 # 2 pixels by y

# score
score_a=0
score_b=0

# Pen(scoreboard)
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#quit game
def quit_game():
    win.bye()

#moving paddle a and b up/down
def paddle_a_up():
    y = paddle_a.ycor() #current y cordinate
    y +=20 # add 20 pixels to y cordinate
    paddle_a.sety(y) #changes the paddles verticle postion

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #current y cordinate
    y +=20 # add 20 pixels to y cordinate
    paddle_b.sety(y) #changes the paddles verticle postion
    

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# keyboard input
win.listen() #record keyboard input
win.onkeypress(paddle_a_up,"w") #whenever we press "w" it will call up the paddle_a_up() function which would move the paddle
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")
win.onkeypress(quit_game,"q")

#moving the ball


#mian game loop
while True:
    win.update() #everytime the loop runs it updates the screen
    #moving the ball
    ball.setx(ball.xcor()+ ball.dx) #moves 2 pix from current x cor pos
    ball.sety(ball.ycor()+ball.dy)
    #Borderchecking

    #upperscreen
    if ball.ycor()>290: #if ball touches the upperscreen
        ball.sety(290) # pause to that y cor pos
        ball.dy*= -1  #bounce back
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    #sidescreen
    if ball.xcor()>390: #gone past the paddel
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write(f"{Player_A}:{score_a} {Player_B}:{score_b}",align="center",font=("courier",24,"normal"))
        
        

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write(f"{Player_A}:{score_a} {Player_B}:{score_b}",align="center",font=("courier",24,"normal"))
              

    #check collision with paddels
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+52 and ball.ycor()>paddle_b.ycor()-52): #basically we are making sure that the coordinates of the abll matches with the current coordinates of the paddel
        ball.setx(340)
        ball.dx*=-1
    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+52 and ball.ycor()>paddle_a.ycor()-52):
        ball.setx(-340)
        ball.dx*=-1

    
    
    

