import os
import turtle
import time 
import random

delay = 0.04
count = 0
Score = 0
High_score = 0

pen = turtle.Turtle()

pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Score :{}   High_score :{} ".format(Score,High_score) ,align ="center" ,font=("courier",24,"bold"))





wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Snake head 
head = turtle.Turtle()
head.speed(15)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(15)
food.shape("circle")
food.color("cyan")
food.penup()
food.goto(0,100)
food.direction = "stop"

segments = []


#defining movement functions
def go_up():
    if head.direction!="down":
        head.direction = "up"

    
def go_down():
    if head.direction!="up":
        head.direction = "down"

def go_left():
    if head.direction!="right":
        head.direction = "left"

def go_right():
    if head.direction!="left":
        head.direction = "right"

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#snake movement
def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+12)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-12)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-12)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x+12)



#main game loop
while True:
    wn.update()

    # Check for collison with border
    if head.xcor()>390 or head.xcor()<-390 or head.ycor()>290 or head.ycor()<-290:
        
        time.sleep(0.5)
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        pen.goto(0,260)
        pen.clear()
        if Score>High_score:
            High_score = Score
        pen.write("Score :{}   High_score :{} ".format(0,High_score) ,align ="center" ,font=("courier",24,"bold"))
        Score = 0
        delay = 0.04



    

    # Check for a collision
    if head.distance(food) <20:
        # Move food to a random spot
        Score+=1
        if delay>0.001:
            delay = delay - 0.001


        x = random.randint(-290, 290)
        y = random.randint(-290, 270)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        pen.clear()
        pen.write("Score :{}   High_score :{} ".format(Score,High_score) ,align ="center" ,font=("courier",24,"bold"))



        

    # Move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        

        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    

    move()
    for segment in segments:
        if segment.distance(head)<5:
            head.color("purple")
            time.sleep(1)
            head.goto(0,0)
            head.color("red")
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            pen.goto(0,260)
            pen.clear()
            if Score>High_score:
                High_score = Score
                pen.write("Score :{}   High_score :{} ".format(0,High_score) ,align ="center" ,font=("courier",24,"bold"))
                Score = 0
            delay = 0.04





    time.sleep(delay)


wn.mainloop()
