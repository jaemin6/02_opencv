# OpenCV 개념 정리

## 필수 라이브 러리
```
import cv2                  # OpenCV - 이미지 처리 기능 제공
import numpy as np         # Numpy - 배열, 프린서 계산을 위해 필요
import matplotlib.pyplot as plt  # Matplotlib - 특정 데이터를 구현적으로 그리는 용도
```

### 1. 히스토그램(Histogram)

#### 개발 목적
1. 이미지의 값 범위 및 범위의 평화, 메인 값의 범위를 해석

2. 메뉴 보이는 값들이 바로 어떻게 반영되는지

#### 사용 코드
```
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)   # 회전이 없는 구분 이미\uc9c으로 로드
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()
```

#### HSV 모델의 Histogram
```
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0,256])
```

### 2. 스레싱홀딩 (Thresholding)

#### 개발 목적
복수로 방면을 나누는 것이 또는 가장 높은 값, 낮은 값으로 구분

#### 가정
```
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", binary)
```
127 = 기준값

255 = 차례 이상 일감 값의 출력 값

THRESH_BINARY : 낮은 값은 0, 높은 값은 255

#### 자동 사용 (Otsu)
```
_, th_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

### 3. 이미지 내 관심 영역 선택 (ROI: Region of Interest)

#### 개발 목적
이미지의 특정 영역을 개발자가 선택하여 처리

#### 그래프
```
(x,y,w,h) = cv2.selectROI("win_name", img, False)   # 마우스로 선택
roi = img[y:y+h, x:x+w]    # 이미지의 그 영역을 자동 표시
```

#### HSV 변환 + 히스토그램 생성
```
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
hist_roi = cv2.calcHist([hsv_roi], [0,1], None, [180,256], [0,180,0,256])
```

### 4. 역투영 (Back Projection)

#### 개발 목적
1. 선택한 개체의 연결 형태를 검색하기 위해

2. 전체 이미지에서 그 도메인스를 찾는 기능

#### 직접 구현 함수 Manual
```
hist_img = cv2.calcHist([hsv_img], [0,1], None, [180,256], [0,180,0,256])
hist_rate = hist_roi / (hist_img + 1)

h,s,v = cv2.split(hsv_img)
bp = hist_rate[h.ravel(), s.ravel()]
bp = np.minimum(bp, 1)
bp = bp.reshape(hsv_img.shape[:2])
cv2.normalize(bp, bp, 0, 255, cv2.NORM_MINMAX)
bp = bp.astype(np.uint8)
```

#### OpenCV 기능 이용
```
bp = cv2.calcBackProject([hsv_img], [0, 1], hist_roi, [0,180,0,256], 1)
```

#### 결과 마스킹 및 출력
```
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(bp, -1, disc, bp)
_, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("result", result)
```


### 5. 기타 개념 정리

#### 요소 생성 (Structuring Element)
```
cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
```
전환, 해제 같은 곳에 사용

#### 필터링 함수
```
cv2.filter2D(src, ddepth, kernel, dst)
```
시계적 논리와 같은 필터 결과 출력

#### 비트 연산
```
cv2.bitwise_and(img1, img2, mask=mask)
```
영역적 건포를 간주

#### Threshold 
```
_, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
```
bp의 값이 1 이상이면 255, 그 이하면 0


## 종료
```
cv2.imshow("win_name", draw)
cv2.waitKey()
cv2.destroyAllWindows()
```

### 목적
출력 함수의 반복 및 종료











