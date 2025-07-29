import cv2
import numpy as np
import matplotlib.pylab as plt

# 1. 이미지를 그레이스케일로 읽기
img = cv2.imread('../img/like_lenna.png', cv2.IMREAD_GRAYSCALE)

# 2. 고정 임계값 130으로 바이너리 이미지 생성
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

# 3. Otsu 알고리즘을 이용하여 자동으로 최적 임계값 계산 및 바이너리 이미지 생성
t_otsu, t_auto = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(f"Otsu threshold: {t_otsu}")

# 4. 결과를 딕셔너리에 저장해서 시각화
imgs = {
    'Original': img,
    'Fixed Threshold (130)': t_130,
    f'Otsu Threshold ({int(t_otsu)})': t_auto
}

# 5. 그래프로 출력
for i, (title, image) in enumerate(imgs.items()):
    plt.subplot(1, 3, i + 1)
    plt.title(title)
    plt.imshow(image, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.tight_layout()
plt.show()
