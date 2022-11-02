# Trash-detection
Using Yolov5 model with TACO dataset

2021-11-13 ~ 2021-11-14

# 폐기물 처리 업체를 위한 AI 폐품 검출 시스템

# Outline
1. 분리수거 처리 시설에서 재사용가능한 폐품만 검출하는 시스템.

# Benefit
1. 버려지는 폐품에 대한 비용 손실을 줄일 수 있다.
2. 폐기물 처리 업체에서 사용하는 유지비를 절감 할 수 있다.

# Functions
1. 영상이나 이미지를 받아 학습시킨 데이터(TACO)를 기반으로 결과를 보여준다.

# TroubleShooting
1. Overfitting이 발생하여 성능 향상이 더이상 이뤄지지 않았다. ->> Overfitting을 줄일 수 있는 작업들을 추가로 해봐야겠다.
2. 물체들을 객체로 보지않고 아닌 순간순간마다 물체로써만 부여하는 Yolo의 특성으로 인해 정확도가 많이 떨어졌다. ->> 다른 모델(Semantic Segmentation, Instance Segmentation 관련 model)을 사용해서 학습시켜보고 싶다.

# Futher
1. 로봇 팔도 만들어서 같이 구동시켜보고 싶다.

# How to use
1. data folder나 models folder의 카테고리 수 등을 바꾸어 주어야하고, 사용하고자 하는 data에 따라 yaml에서의 경로설정을 다시 해줘야한다. 그리고 이 코드의 특징인 Yolo에 따라 coco format의 데이터를 object detection형태로 전환하는 prepareDataset를 잘 활용해아한다.