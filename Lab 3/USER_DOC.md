# Пользовательская документация

## 1. Введение

Приложение "Обработка изображений" предназначено для выполнения различных операций обработки изображений, включая улучшение контрастности, эквализацию гистограммы и применение фильтров размытия. Оно предоставляет удобный веб-интерфейс для загрузки изображений, выбора методов обработки и просмотра результатов.

## 2. Системные требования

- **Операционная система**: Windows, macOS, Linux.
- **Веб-браузер**: Последние версии Chrome, Firefox, Safari или Edge.
- **Python**: Версия 3.7 или выше.
- **Дополнительные библиотеки**: Flask, OpenCV, NumPy.

## 3. Установка и запуск
# Пользовательская документация

## 3.1 Работа с готовым веб-приложением

Если приложение развернуто на сервере, просто откройте ссылку, предоставленную администратором.

## 4. Использование приложения

### 4.1 Загрузка изображения

1. Перейдите на главную страницу приложения.
2. Нажмите кнопку **“Выберите файл”** и загрузите изображение (поддерживаются форматы: `.jpg`, `.png` и другие).
3. Выберите метод обработки из выпадающего списка:
   - Эквализация гистограммы (RGB)
   - Эквализация гистограммы (HSV)
   - Линейное контрастирование
   - Гауссово размытие
   - Среднее размытие
   - Медианное размытие
4. Укажите размер ядра (только для методов размытия). Значение должно быть нечетным.

### 4.2 Применение обработки

1. Нажмите кнопку **“Обработать”**.
2. Дождитесь завершения обработки.
3. Просмотрите оригинальное и обработанное изображение на следующей странице.

### 4.3 Сохранение результатов

- Обработанное изображение сохраняется в папке `static` на сервере.
- Вы можете скачать результат, щелкнув правой кнопкой мыши на изображении и выбрав **“Сохранить изображение как…”**.

## 5. Методы обработки изображений

- **Эквализация гистограммы (RGB)**: Улучшает контраст изображения путем перераспределения яркости в каналах RGB.
- **Эквализация гистограммы (HSV)**: Применяет эквализацию только к компоненте яркости в цветовой модели HSV.
- **Линейное контрастирование**: Увеличивает контраст изображения с использованием линейного масштабирования.
- **Гауссово размытие**: Размывает изображение, устраняя шум, сохраняя плавные переходы.
- **Среднее размытие**: Применяет усреднение по ядру заданного размера.
- **Медианное размытие**: Эффективно устраняет шумы, сохраняя края объектов.