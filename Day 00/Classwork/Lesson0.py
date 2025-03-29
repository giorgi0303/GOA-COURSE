from turtle import * #ფანჯრის გამოძახება რაშიც იხატება ნახაძზი კოდის საშუალებით
 #ეს არის ბრძანება რომელიც იწერება კოდის ბოლოში და უზრნველყოფს კოდის გაშვების შემდეგ ნახზს ხანგრძ₾ივად გაჩრებას


width (8)
color("purple")

#SQUARE
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#COURSOR
forward(200)
left(90)

forward(70) 
left(90)

color("yellow")

#DOOR
color("red")
begin_fill()

forward(120)
right(90)

forward(50)
right(90)

forward(120)
left(90)

color("purple")
penup()
goto(200, 200)
pendown()


#ROOF

color("green") 
begin_fill()
left(140)

forward(140)
left (84)

forward(132)
end_fill()

#window 1
color("brown")
penup()
goto(140, 160)
pendown()

left(46)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

penup()
goto(55, 115)
pendown()

right(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

right(185)

penup()
goto(32,116)
pendown()

right(85)
forward(45)

penup()
goto(10, 135)
pendown()

right(90)
forward(45)

penup()
goto(145, 135)
pendown()

forward(40)
left(90)

penup()
goto(162, 160)
pendown()

left(180)
forward(45)

penup()
goto(145, 250)
pendown()

right(230)
forward(45)

right(90)
forward(25)

right(90)
forward(42)


exitonclick()