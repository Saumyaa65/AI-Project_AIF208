# AI Project: Custom Object Detection (YOLOv8)

This repository hosts an **Artificial Intelligence project** focused on **custom object detection** using the cutting-edge **YOLOv8 (You Only Look Once)** model. The project involves training a pre-existing YOLOv8 model on a custom dataset to identify specific objects relevant to the project's goals.

## Overview

The aim of this project is to develop and train an object detection model capable of recognizing and localizing custom objects within images. By leveraging the efficient and powerful YOLOv8 architecture, the project demonstrates a practical application of deep learning in computer vision.

## Features

* **Custom Object Detection:** Trains a YOLOv8 model to detect specific objects defined in a custom dataset.
* **Leverages YOLOv8:** Utilizes the highly optimized and accurate YOLOv8 architecture from Ultralytics.
* **Transfer Learning from Pre-trained Weights:** Starts with a pre-trained `yolov8n.pt` model, allowing for faster convergence and better performance on the custom dataset.
* **Model Training Pipeline:** Includes the necessary steps to set up and initiate the training process for the YOLOv8 model.

## Technologies Used

* Python
* `ultralytics` (for YOLOv8 framework)
* `os` (for path handling, usually involved in dataset management)
* `shutil` (for file operations, often used in dataset splitting)
* `random` (for random sampling, also common in data preparation)

## How It Works

The core workflow of this project involves training a YOLOv8 model on a prepared dataset:

1.  **Dataset Preparation:**
    * The project expects a structured dataset within a `Dataset/` directory. This typically includes `train`, `valid` (validation), and `test` subdirectories containing images and their corresponding annotation files (e.g., in YOLO format).
    * A `data.yaml` file within the `Dataset/` directory is crucial. This YAML file specifies the paths to the training, validation, and test images/labels, as well as the names of the custom object classes.

2.  **Model Initialization:**
    * A YOLOv8 model is initialized using pre-trained weights (`yolov8n.pt`). This nano-sized model offers a good balance between performance and computational efficiency.

3.  **Model Training:**
    * The `model.train()` method from the `ultralytics` library is called to start the training process.
    * Training parameters such as the path to the `data.yaml` file, the number of training `epochs` (iterations over the entire dataset), `batch` size (number of samples processed at once), and input `imgsz` (image size for training
