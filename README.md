# ReSort-AI: Recycling Sorting Automation with AI Vision System
*(AI 비전 시스템을 활용한 재활용품 분류 자동화 시스템)*

ReSort-AI는 분리수거 처리 시설에서 재사용 가능한 폐품을 자동으로 검출·선별하는 것을 목표로 하는 시스템입니다. 카메라 영상(또는 이미지)을 입력으로 받아 객체 탐지 기반 AI 모델을 통해 재사용 가능 품목을 식별하며, 이를 통해 버려지는 폐품으로 인한 비용 손실을 줄이고 운영·유지 비용을 절감할 수 있습니다. 본 프로젝트에서는 폐기물 환경에 특화된 탐지를 위해 TACO 데이터셋을 활용해 모델을 전이학습하는 실험을 포함합니다.

## ⚙️ Tech Stacks
- YOLOv5
- PyTorch
- Python

## ✨ Features
1. 카메라 영상 기반 **재사용 가능 폐품 객체 탐지**
2. 폐기물 이미지 데이터 기반 **TACO 데이터셋 전이학습**
3. 선별 자동화를 통한 **비용 손실 감소 및 운영 효율 향상**

## 🧭 Overview
<img src="https://github.com/MonoHaru/CephLD-CCA/blob/main/assets/overview.png" alt="overview" width="700">

## 🎬 **Demo** 
https://github.com/user-attachments/assets/ed728e64-40eb-47c5-a4e4-7277d481bf76

## 🔮 **Future Work** 
1. 학습 과정에서 발생하는 과적합(overfitting)을 완화하기 위한 정규화 및 일반화 기법 적용(ex: augmentation, regularization, early stopping 등)
2. 검출 결과를 기반으로 로봇 팔 등 물리 장비와 연동하여 수거/이송까지 포함한 완전 자동화 파이프라인 구축
3. 더 정교한 분리를 위해 Semantic/Instance Segmentation 기반 접근 방법 적용 및 성능 비교

## 📜 License
The code in this repository is released under the GPL-3.0 License.