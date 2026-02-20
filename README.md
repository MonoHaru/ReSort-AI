🌐 Languages: [[English](README.md)] | [[한국어](README-KR.md)]

# ReSort-AI: Recycling Sorting Automation with AI Vision System
*(A recycling sorting automation system using an AI vision system)*

ReSort-AI is a system designed to automatically detect and sort reusable waste items in recycling and waste-processing facilities. It takes camera footage (or images) as input and identifies reusable items using an object detection-based AI model. This helps reduce cost losses caused by reusable items being discarded and can lower operational and maintenance costs. This project also includes experiments on transfer learning using the TACO dataset to improve detection performance in waste-specific environments.


## ⚙️ Tech Stacks
- YOLOv5
- PyTorch
- Python


## ✨ Features
1. Camera footage-based **object detection of reusable waste items**
2. **Transfer learning on the TACO dataset** using waste image data
3. **Reduced cost losses and improved operational efficiency** through automated sorting


## 🧭 Overview
<img width="1835" height="791" alt="Image" src="https://github.com/user-attachments/assets/d0c6132a-e4a2-450d-9457-8fc83dc851ae" />

## 🎬 **Demo** 
https://github.com/user-attachments/assets/ed728e64-40eb-47c5-a4e4-7277d481bf76

## 🔮 **Future Work** 
1. Apply regularization and generalization techniques to mitigate overfitting during training, such as augmentation, regularization, and early stopping
2. Build a fully automated pipeline that integrates detection results with physical equipment such as a robotic arm, including picking and conveying
3. Explore Semantic Segmentation and Instance Segmentation-based approaches for more fine-grained separation, and compare performance

## 📜 License
The code in this repository is released under the GPL-3.0 License.