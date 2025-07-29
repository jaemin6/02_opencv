import cv2
import numpy as np
import matplotlib.pylab as plt

#--① 그레이 스케일로 영상 읽기
img = cv2.imread('../img/sunset.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 정상적으로 읽혔는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
    exit()

#--② 직접 연산한 정규화
img_f = img.astype(np.float32)
img_norm = ((img_f - img_f.min()) * (255) / (img_f.max() - img_f.min()))
img_norm = img_norm.astype(np.uint8)

#--③ OpenCV API를 이용한 정규화
img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

#--④ 히스토그램 계산
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 256])

# 이미지 출력
cv2.imshow('Before', img)
cv2.imshow('Manual', img_norm)
cv2.imshow('cv2.normalize()', img_norm2)

# 키 입력 대기 및 윈도우 종료
cv2.waitKey(0)
cv2.destroyAllWindows()

# 히스토그램 그래프 출력
hists = {'Before' : hist, 'Manual':hist_norm, 'cv2.normalize()':hist_norm2}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1,3,i+1)
    plt.title(k)
    plt.plot(v)
plt.show()
