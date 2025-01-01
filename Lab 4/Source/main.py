from flask import Flask, render_template, request, jsonify
import math
import time

app = Flask(__name__)

GRID_SIZE = 20

def step_by_step_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0

    points = []
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def dda_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0

    points = []
    for i in range(int(steps) + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def bresenham_algorithm(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    x, y = x0, y0

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

    if dx > dy:
        err = dx / 2
        while x != x1:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y1:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x, y))
    return points

def bresenham_circle_algorithm(x0, y0, x1, y1):
    points = []

    # Вычисляем радиус окружности по двум точкам
    r = int(math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))

    x = 0
    y = r
    d = 3 - 2 * r

    def plot_points(x0, y0, x, y):
        points.extend([
            (x0 + x, y0 + y), (x0 - x, y0 + y),
            (x0 + x, y0 - y), (x0 - x, y0 - y),
            (x0 + y, y0 + x), (x0 - y, y0 + x),
            (x0 + y, y0 - x), (x0 - y, y0 - x)
        ])

    while y >= x:
        plot_points(x0, y0, x, y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

    return points


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw", methods=["POST"])
def draw():
    data = request.json
    x0, y0 = data['start']
    x1, y1 = data['end']
    algorithm = data['algorithm']

    start_time = time.perf_counter()

    if algorithm == 'пошаговый':
        points = step_by_step_algorithm(x0, y0, x1, y1)
    elif algorithm == 'цда':
        points = dda_algorithm(x0, y0, x1, y1)
    elif algorithm == 'брезенхем':
        points = bresenham_algorithm(x0, y0, x1, y1)
    elif algorithm == 'окружность':
        points = bresenham_circle_algorithm(x0, y0, x1, y1)
    else:
        points = []

    execution_time = (time.perf_counter() - start_time) * 1_000_000  # в микросекундах

    # Сопроводительные вычисления
    calculations = [f"x: {x}, y: {y}" for x, y in points]  # Исправлено

    return jsonify({
        "points": points,
        "execution_time": execution_time,
        "calculations": calculations
    })

if __name__ == "__main__":
    app.run(debug=True)