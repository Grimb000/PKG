# Пользовательская документация

## 1. Введение

Приложение **"Конвертер цветовых моделей (Kislov, lab 1, вариант 7)"** предназначено для работы с цветовыми моделями **CMYK**, **RGB** и **HSV**. Оно позволяет пользователям конвертировать значения между этими моделями и визуализировать результат. Программа подойдет дизайнерам, разработчикам и всем, кто работает с цветами.

## 2. Системные требования

- **Операционная система**: Windows, macOS, Linux
- **Веб-браузер**: последняя версия Chrome, Firefox, Safari или Edge
- **Подключение к интернету**: требуется для доступа к веб-приложению

## 3. Установка и запуск

### 3.1 Доступ к приложению

1. Откройте веб-браузер.
2. Перейдите по предоставленному адресу
3. Приложение автоматически загрузится и будет готово к использованию.

## 4. Использование приложения

### 4.1 Интерфейс приложения

Приложение состоит из трех разделов, каждый из которых представляет одну из цветовых моделей:

1. **CMYK** – работа с цветами в формате *Cyan, Magenta, Yellow, Key (Black)*.
2. **RGB** – работа с цветами в формате *Red, Green, Blue*.
3. **HSV** – работа с цветами в формате *Hue, Saturation, Value*.

Каждый раздел включает:
- Поля для ввода численных значений.
- Ползунки для интерактивного выбора значений.
- Синхронизацию данных между моделями в реальном времени.

### 4.2 Выбор цвета

#### 4.2.1 Ввод значений вручную
Введите значения для нужной модели:
- **CMYK**: от 0 до 100 для каждого параметра.
- **RGB**: от 0 до 255 для каждого параметра.
- **HSV**: 
  - **H (Hue)**: от 0 до 360.  
  - **S (Saturation)** и **V (Value)**: от 0 до 100.

#### 4.2.2 Использование ползунков
Ползунки позволяют менять значения плавно. При их перемещении:
- Значения обновляются мгновенно.
- Цвет в фоновом режиме страницы изменяется в соответствии с текущими параметрами.

#### 4.2.3 Визуализация
- Фон страницы изменяется в соответствии с текущими параметрами цвета.
- Цвет текста автоматически подстраивается для лучшей читаемости.

### 4.3 Конвертация между моделями

- Значения всех моделей пересчитываются автоматически при изменении одного из параметров.
- Приложение поддерживает конвертацию:
  - **CMYK → RGB → HSV**
  - **RGB → CMYK → HSV**
  - **HSV → RGB → CMYK**

### 4.4 Валидация и предупреждения

- Приложение автоматически корректирует некорректные значения.
- Если возможно, пользователю выводится предупреждение о потере точности при конвертации.

## 5. Часто задаваемые вопросы

### 5.1 Почему значения других моделей не обновляются?
Убедитесь, что вы завершили ввод значения в поле (нажмите `Enter` или переключитесь на другое поле).

### 5.2 Что делать, если цвет отображается некорректно?
Проверьте, что введенные значения находятся в допустимом диапазоне. Используйте ползунки для точного выбора.

### 5.3 Как изменить цветовую модель?
Просто начните вводить данные или использовать ползунки в нужной модели — конвертация произойдет автоматически.
