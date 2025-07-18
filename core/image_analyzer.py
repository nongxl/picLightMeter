import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def calculate_average_luminance(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    avg_lum = np.mean(gray)
    return avg_lum

def calculate_center_luminance(image_path, crop_ratio=0.5):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    x0 = int(w * (1 - crop_ratio) / 2)
    y0 = int(h * (1 - crop_ratio) / 2)
    x1 = x0 + int(w * crop_ratio)
    y1 = y0 + int(h * crop_ratio)
    center_crop = gray[y0:y1, x0:x1]
    return np.mean(center_crop)

def is_exposure_valid(image_path, threshold=0.9):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    total = gray.size
    dark_pixels = np.sum(hist[:10])
    bright_pixels = np.sum(hist[245:])

    if dark_pixels / total > threshold:
        return False, "图像严重欠曝"
    elif bright_pixels / total > threshold:
        return False, "图像严重过曝"
    return True, "图像曝光正常"

def plot_histogram(image_path):
    rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置中文字体
    rcParams['axes.unicode_minus'] = False

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.figure(figsize=(8, 4))
    plt.title("灰度直方图")
    plt.xlabel("亮度值 (0-255)")
    plt.ylabel("像素数量")
    plt.hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()