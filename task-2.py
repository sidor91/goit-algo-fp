import turtle
import math

def draw_branch(t, length, angle, level):
    if level == 0:
        return

    # Намалювати поточну гілку
    t.forward(length)

    # Зберегти позицію
    pos = t.pos()
    heading = t.heading()

    # Ліва гілка
    t.left(angle)
    draw_branch(t, length * 0.7, angle, level - 1)

    # Повернутися назад
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()

    # Права гілка
    t.right(angle)
    draw_branch(t, length * 0.7, angle, level - 1)

    # Повернутися назад
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 9): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("sienna")
    t.speed(0)
    t.left(90)  # Повернути черепашку вгору
    t.penup()
    t.goto(0, -250)  # Початкова точка
    t.pendown()

    draw_branch(t, 100, 30, level)

    screen.exitonclick()

if __name__ == "__main__":
    main()