from turtle import Turtle, Screen
from jim import Jim
from cars import Cars
from score import Score
import random
import time

screen = Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.title("Cross")
screen.tracer(0)
score = Score()
starting_positions = [(400, 165), (40, 125), (389, 85), (180, 45), (100, 5), (300, -35), (350, -75), (300, -115), (400, -155)]
all_cars = []

#Turtle
jim = Jim((0, -200))
for traffic in starting_positions:
  new_car = Cars((traffic))
  all_cars.append(new_car)

# car1 = Cars((400, 165))
# car2 = Cars((400, 125))
# car3 = Cars((400, 85))
# car4 = Cars((400, 45))
# car5 = Cars((400, 5))
# car6 = Cars((400, -35))
# car7 = Cars((400, -75))
# car8 = Cars((400, -115))
# car9 = Cars((400, -155))


screen.listen()
screen.onkey(jim.go_up, "Up")
screen.onkey(jim.go_down, "Down")

print(all_cars)

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  score.update_scoreboard()

  for car in all_cars:
    car.movement()
    if car.xcor() < -400:
      car.restart_car()
    if car.xcor() - 10 < jim.xcor() < car.xcor() + 10 and car.ycor() - 10 < jim.ycor() < car.ycor() + 10:
      score.end_game()
      game_is_on = False
  if jim.ycor() > 200:
    score.point()
    jim.reset_turtle()



  
  


screen.exitonclick()
