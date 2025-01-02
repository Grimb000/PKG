from flask import Flask, request, jsonify, render_template
from PIL import Image, JpegImagePlugin, GifImagePlugin, TiffImagePlugin, BmpImagePlugin, PcxImagePlugin, PngImagePlugin
import os
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # предполагается, что index.html находится в папке templates


def get_color_depth(img):
    # Словарь соответствия режимов глубине цвета
    mode_to_bpp = {
        "1": 1,
        "L": 8,
        "P": 8,
        "RGB": 24,
        "RGBA": 32,
        "CMYK": 32,
        "I": 32,
        "F": 32,
        "I;16": 16,
        "RGB;16": 48,
        "RGBA;16": 64
    }
    # Возвращаем глубину цвета или -1, если режим неизвестен
    return mode_to_bpp.get(img.mode, -1)

def determine_compression_type(img):
    """Определяет тип сжатия: с потерями, без потерь или без сжатия."""
    if isinstance(img, JpegImagePlugin.JpegImageFile):
        return "Сжатие с потерями"
    elif isinstance(img, PngImagePlugin.PngImageFile):
        return "Сжатие без потерь"
    elif isinstance(img, GifImagePlugin.GifImageFile):
        return "Сжатие без потерь"
    elif isinstance(img, TiffImagePlugin.TiffImageFile):
        compression = img.tag_v2.get(259, None)  # Тип сжатия в TIFF (259 — это тег сжатия)
        if compression == 1:  # No compression
            return "Без сжатия"
        elif compression in [5, 7, 8]:  # LZW, JPEG, ZIP
            return "Сжатие без потерь" if compression != 7 else "Сжатие с потерями"
    elif isinstance(img, BmpImagePlugin.BmpImageFile):
        return "Без сжатия"
    elif isinstance(img, PcxImagePlugin.PcxImageFile):
        return "Сжатие без потерь"
    return "N/A"

def get_image_info(file):
    """Собирает информацию об изображении и возвращает её в виде словаря."""
    try:
        with Image.open(file) as img:
            # Извлечение разрешения DPI из img.info
            dpi = img.info.get('dpi', (0, 0))
            dpi_str = f"{dpi[0]}x{dpi[1]} DPI" if dpi[0] > 0 and dpi[1] > 0 else "N/A"

            # Основная информация об изображении
            info = {
                "filename": os.path.basename(file.filename),
                "dimensions": img.size,
                "resolution": dpi_str,
                "color_depth": get_color_depth(img),
                "compression": determine_compression_type(img)
            }

            return info
    except Exception as e:
        return {"filename": os.path.basename(file.filename), "error": str(e)}

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')
    image_info_list = []
    try:
        with ThreadPoolExecutor() as executor:
            image_info_list = list(executor.map(get_image_info, files))
        return jsonify(image_info_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)