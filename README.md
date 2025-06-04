# Human Detection for Trespassing Prevention (AI-Project AIF208)

This repository hosts an **Artificial Intelligence project** specifically designed for **human detection to prevent trespassing**. It leverages the cutting-edge **YOLOv8 (You Only Look Once)** model, trained on a custom dataset to accurately identify human presence in surveillance or monitored areas.

## Overview

The primary goal of this project is to create an intelligent system capable of automatically detecting humans in video feeds or images. By identifying individuals, the system aims to serve as a crucial component in **trespassing prevention** and security monitoring applications, providing alerts or triggers when unauthorized human presence is detected in designated zones.

## Features

* **Human Object Detection:** Specifically trained to recognize and localize human figures within images or video frames.
* **Trespassing Prevention Application:** Designed to be integrated into security systems for automated monitoring and alert generation.
* **Leverages YOLOv8:** Utilizes the highly efficient and accurate YOLOv8 architecture from Ultralytics, known for real-time performance.
* **Custom Dataset Training:** The model is trained on a specialized dataset to optimize its performance for human detection in relevant environments.
* **Transfer Learning from Pre-trained Weights:** Initializes with a pre-trained `yolov8n.pt` model, accelerating training and enhancing detection capabilities.

## Research Paper

For a more detailed understanding of the methodology, dataset, and results, please refer to the accompanying research paper:
[**AI-Project AIF208 Research Paper**](https://drive.google.com/file/d/1EjzmE4KHsObltZgBGN-D-nCCanae48QJ/view?usp=sharing)

## Technologies Used

* Python
* `ultralytics` (for YOLOv8 framework)
* `os` (for file system operations, often for data management)
* `shutil` (for high-level file operations, useful in dataset handling)
* `random` (for data splitting and augmentation strategies)

## How It Works

The core workflow of this project involves training a YOLOv8 model on a prepared dataset tailored for human detection:

1.  **Dataset Preparation:**
    * The project requires a structured dataset within a `Dataset/` directory. This directory must contain `train`, `valid` (validation), and `test` subdirectories, which hold images and their corresponding annotation files (e.g., in YOLO format), specifically labeled for human subjects.
    * A `data.yaml` file within the `Dataset/` directory defines the paths to these image and label sets, along with the names of the custom object classes (e.g., 'human').

2.  **Model Initialization:**
    * A YOLOv8 model is initialized using pre-trained weights (`yolov8n.pt`). This "nano"-sized model offers a strong balance between detection accuracy and computational speed, suitable for real-time applications.

3.  **Model Training:**
    * The `model.train()` method from the `ultralytics` library is invoked to commence the training process.
    * Key training parameters, such as the path to the `data.yaml` configuration, the total number of training `epochs`, the `batch` size (number of images processed per training step), and the input image `imgsz` (size to which images are resized during training), are configured.
    * During this phase, the model learns to identify and precisely locate human objects within the provided training data. The training progress, performance metrics, and the resulting trained model weights are automatically saved by the `ultralytics` framework.
