# Техническая документация: Алгоритмы отсечения

## Описание проекта
Этот проект представляет собой веб-приложение для визуализации и работы с двумя алгоритмами отсечения:
1. Алгоритм Сазерленда-Коэна.
2. Алгоритм Кируса-Бека.

Приложение позволяет рисовать отрезки, задавать границы отсечения (в виде многоугольников) и наблюдать, как работают различные алгоритмы отсечения.

## Структура проекта
### HTML
```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Алгоритмы отсечения</title>
  <style>
    /* Стили определены внутри HTML-файла */
  </style>
</head>
<body>
  <h2>Алгоритмы отсечения</h2>
  <div class="controls">
    <button onclick="switchAlgorithm('cohen')" id="cohenBtn">Сазерленд-Коэн</button>
    <button onclick="switchAlgorithm('cyrus')" id="cyrusBtn">Кирус-Бек</button>
    <button id="lineMode" class="active" onclick="setMode('line')">Рисовать отрезки</button>
    <button id="clipMode" onclick="setMode('clip')">Рисовать границу</button>
    <button onclick="clearCanvas()">Очистить</button>
  </div>
  <canvas id="canvas" width="600" height="400"></canvas>
</body>
</html>
```

### CSS
Стили расположены внутри тега `<style>`:
```css
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
  margin: 20px;
}

canvas {
  border: 1px solid #000;
  margin: 10px;
  cursor: crosshair;
}

.controls {
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 5px 10px;
  margin: 0 5px;
}

.active {
  background-color: #4CAF50;
  color: white;
}
```

### JavaScript
Основная логика приложения написана на JavaScript. Включает:
- Переключение между алгоритмами отсечения.
- Режимы рисования отрезков и границ.
- Реализация алгоритмов:
  - Сазерленда-Коэна.
  - Кируса-Бека.

Основные функции:
```javascript
function switchAlgorithm(algorithm) { ... }
function setMode(mode) { ... }
function clearCanvas() { ... }
function cohenSutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax) { ... }
function cyrusBeck(x1, y1, x2, y2, polygon) { ... }
function drawScene() { ... }
```

## Особенности реализации
1. **Многоугольные границы:** Алгоритм Кируса-Бека поддерживает произвольные выпуклые многоугольники.
2. **Графический интерфейс:**
   - Отрисовка исходных отрезков и результатов отсечения.
   - Визуализация ограничивающего прямоугольника для алгоритма Сазерленда-Коэна.

3. **Интерактивность:**
   - Рисование мышью отрезков и границ.
   - Переключение режимов и очистка холста.

## Использование
1. Выберите алгоритм отсечения, нажав соответствующую кнопку.
2. Нажмите "Рисовать отрезки" и нарисуйте линии на холсте.
3. Переключитесь на режим "Рисовать границу" и задайте многоугольник.
4. Отсечение происходит автоматически при наличии валидной границы.

## Возможности для улучшения
- Добавить поддержку произвольных (не выпуклых) многоугольников.
- Реализовать дополнительные алгоритмы отсечения.
- Улучшить визуальные эффекты и производительность.

