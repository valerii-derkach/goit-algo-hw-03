import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  # повертаємося на 120 градусів для наступної сторони

def main():
    order = int(input("Введіть рівень рекурсії (наприклад, 0, 1, 2, 3): "))
    size = 300  # розмір сніжинки

    window = turtle.Screen()
    window.bgcolor("white")

    # створюємо черепашку для малювання
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # малюємо сніжинку Коха
    koch_snowflake(t, order, size)

    window.mainloop()

if __name__ == "__main__":
    main()
