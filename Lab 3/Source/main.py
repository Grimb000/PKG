from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['RESULT_FOLDER'] = 'static/'

# Утилиты
def load_image(path):
    """Загрузка изображения с диска."""
    return cv2.imread(path)

def save_image(image, path):
    """Сохранение изображения на диск."""
    cv2.imwrite(path, image)

# Методы обработки изображений
def equalize_hist_rgb(image):
    """Эквализация гистограммы для каждого канала RGB."""
    channels = cv2.split(image)
    eq_channels = [cv2.equalizeHist(ch) for ch in channels]
    return cv2.merge(eq_channels)

def equalize_hist_hsv(image):
    """Эквализация гистограммы по компоненте яркости в HSV."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def linear_contrast(image):
    """Линейное контрастирование изображения."""
    min_val = np.min(image)
    max_val = np.max(image)
    result = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return result

# Низкочастотные фильтры
def gaussian_blur(image, kernel_size=5):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def average_blur(image, kernel_size=5):
    return cv2.blur(image, (kernel_size, kernel_size))

def median_blur(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)

# Маршруты приложения
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    """Обработка изображения."""
    file = request.files.get('image')
    method = request.form.get('method')
    kernel_size = int(request.form.get('kernel_size', 5))  # Размер ядра (по умолчанию 5)

    if not file:
        return "Файл не загружен", 400

    # Сохранение оригинального изображения в папке static
    original_filename = f"original_{file.filename}"
    original_path = os.path.join(app.config['RESULT_FOLDER'], original_filename)
    file.save(original_path)

    # Загрузка изображения
    image = load_image(original_path)

    # Выбор метода обработки
    if method == 'histogram_rgb':
        result = equalize_hist_rgb(image)
    elif method == 'histogram_hsv':
        result = equalize_hist_hsv(image)
    elif method == 'contrast':
        result = linear_contrast(image)
    elif method == 'gaussian_blur':
        result = gaussian_blur(image, kernel_size)
    elif method == 'average_blur':
        result = average_blur(image, kernel_size)
    elif method == 'median_blur':
        result = median_blur(image, kernel_size)
    else:
        return "Метод не найден", 400

    # Сохранение обработанного изображения
    result_filename = 'result.jpg'
    result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
    save_image(result, result_path)

    # Передача путей к оригинальному и обработанному изображениям в шаблон
    return render_template(
        'result.html',
        original_image=f'static/{original_filename}',
        result_image=f'static/{result_filename}'
    )

if __name__ == '__main__':
    # Создание необходимых папок, если их нет
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)
    app.run(debug=True)