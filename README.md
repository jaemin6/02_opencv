# OpenCV 이미지 처리 개념 총정리 (예제 + 개념 + 수도코드)

## 목차
1. 히스토그램 (Histogram)

2. 스레숄딩 (Thresholding)

3. 관심영역 (ROI: Region of Interest)

4. 역투영 (Back Projection)

5. 기본 라이브러리 설명

## 1. 히스토그램 (Histogram)

### ✅ 개념
히스토그램은 이미지의 밝기 또는 색상 값이 얼마나 분포되어 있는지 시각적으로 나타낸 그래프입니다.
이미지 처리에서 히스토그램은 색 분포, 명암도 분포를 파악하거나 대비 향상 등에 사용됩니다.

### ✅ 대표 함수
```
cv2.calcHist(images, channels, mask, histSize, ranges)
```

<img width="576" height="310" alt="cv2" src="https://github.com/user-attachments/assets/59303cfa-f8b1-41af-a41e-ed6a2aa06e56" />


### ✅ 예제 코드
```
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.title('Histogram')
plt.show()
```

### ✅ 수도코드
```
1. 이미지를 불러온다
2. 흑백으로 변환한다 (필요시)
3. 히스토그램 계산 함수 호출
4. matplotlib로 시각화
```

## 2. 스레숄딩 (Thresholding)

### ✅ 개념
임계값을 기준으로 이미지를 이진화합니다. 픽셀 값이 임계값보다 크면 흰색(255), 작으면 검정색(0)으로 설정합니다.

### ✅ 대표 함수
```
retval, dst = cv2.threshold(src, thresh, maxval, type)
```

<img width="464" height="226" alt="cv3" src="https://github.com/user-attachments/assets/d6cc8639-ae43-4966-85cf-eecfde9de8cd" />

### ✅ 예제 코드
```
img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### ✅ 수도코드
```
1. 이미지를 불러온다
2. 그레이스케일로 변환한다
3. cv2.threshold()로 이진화 처리
4. 결과를 출력한다
```
## 3. 관심영역 (ROI: Region of Interest)

### ✅ 개념
이미지에서 사용자가 관심 있는 부분만 잘라서 따로 처리하는 기술입니다. 객체 추적, 필터 적용 등에 사용됩니다.

### ✅ ROI 설정 함수
```
x, y, w, h = cv2.selectROI(window_name, img, fromCenter=False)
roi = img[y:y+h, x:x+w]
```
### ✅ 예제 코드
```
img = cv2.imread('lenna.jpg')
roi = img[100:200, 100:200]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### ✅ 수도코드
```
1. 이미지 불러오기
2. ROI 영역 좌표 설정
3. 자른 부분만 따로 변수로 저장
4. 해당 영역만 출력하거나 처리
```
## 4. 역투영 (Back Projection)

### ✅ 개념
어떤 특정 물체의 색상 히스토그램을 기반으로 전체 이미지에서 해당 색상이 있는 부분을 찾아내는 기술입니다.
대표적으로 객체 추적 등에 활용됩니다.

### ✅ 주요 사용 함수
```
cv2.calcBackProject(images, channels, hist, ranges, scale)
```

### ✅ 예제 코드
```
# ROI 선택 -> HSV -> 히스토그램 계산 -> 전체 이미지에 역투영 적용
img = cv2.imread('target.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
bp = cv2.calcBackProject([hsv], [0,1], hist, [0,180,0,256], 1)
```

### ✅ 수도코드
```
1. 원본 이미지 불러오기
2. 추적할 대상 ROI 선택 -> HSV 변환
3. ROI 히스토그램 계산
4. 전체 이미지 HSV에서 calcBackProject() 실행
5. 결과로 나온 역투영 이미지 활용 (마스킹 등)
```

## 5. 기본 라이브러리 설명

### 1. 📦 OpenCV (cv2)
1. 컴퓨터 비전 라이브러리

2. 이미지 처리, 영상 인식, 객체 추적 등 기능 제공

### 2. 📦 NumPy (np)
1. 수치 계산용 라이브러리

2. 배열 처리, 이미지 수치 연산 등에 사용

### 3. 📦 Matplotlib (matplotlib.pyplot)
1. 데이터 시각화 라이브러리

2. 히스토그램, 이미지 출력 등을 위한 플롯 기능 제공

### 4. 📁 추천 예제 이미지 목록
1. lenna.jpg → 고전적인 테스트 이미지
<img width="300" height="300" alt="like_lenna" src="https://github.com/user-attachments/assets/1393019e-9653-49cf-a0ba-b29dd571750b" />

2. sunset.jpg → 다양한 컬러가 섞인 장면 (히스토그램 연습에 좋음)
![sunset](https://github.com/user-attachments/assets/79bb3ee6-58ac-45ea-aeb3-ef65a597432e)

3. pump_horse.jpg → 역투영 예제에 적합
<img width="1280" height="351" alt="pump_horse" src="https://github.com/user-attachments/assets/3b856d08-0f2a-4c76-99b6-e62016c66d4f" />








