import turtle #for simple graphics 
import winsound


window = turtle.Screen()

window.title("Pong Game")

window.bgcolor("black") #back ground color

window.setup(width=800, height=600) #window size

window.tracer(0) #stops the window from updating to help speed up the game

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets animation to the max speed
paddle_a.shape("square") #defalt shape 20/20 pixels
paddle_a.color("white")
paddle_a.shapesize(5,1) #the #'s are * 20
paddle_a.penup() #makes it so theres no line tracing the movement
paddle_a.goto(-350, 0) #0,0 is in the middle of the screen -225 is the left edge 


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") 
paddle_b.color("white")
paddle_b.shapesize(5,1) 
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") 
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08 #d = delta/change x = x axis
ball.dy = 0.08  #2 = 2 pixels


#score
score_a = 0
score_b = 0



#Pen 
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24 , "normal"))



#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#keyboard binding
window.listen() #listen for keyboard input
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")  #how to acces the arrows
window.onkeypress(paddle_b_down,"Down")

#main game loop (Meat and Potatos of game code)
while True:
    window.update() #everytime the loop runds the window updates

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
       
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24 , "normal"))
        winsound.PlaySound("mixkit-losing-bleeps-2026.wav", winsound.SND_ASYNC)


    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #makes it so that it clears the previous score and replaces it with the new one instead of overlapping
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24 , "normal"))
        winsound.PlaySound("mixkit-losing-bleeps-2026.wav", winsound.SND_ASYNC)
    

    #Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
