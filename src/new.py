import cv2
import numpy as np

# 이미지 불러오기
img1 = cv2.imread('../img/kia.jpg')      # 기아 아동 이미지
img2 = cv2.imread('../img/pshcho.jpg')   # 행복한 사람 이미지

# 이미지 높이를 기준으로 두 이미지를 비율 유지하며 리사이즈
height = 500
def resize_with_height(img, target_height):
    h, w = img.shape[:2]
    ratio = target_height / h
    return cv2.resize(img, (int(w * ratio), target_height))

img1_resized = resize_with_height(img1, height)
img2_resized = resize_with_height(img2, height)

# 두 이미지 나란히 붙이기
combined = np.hstack((img1_resized, img2_resized))

# 결과 보기
cv2.imshow('Combined Image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
