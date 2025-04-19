import os
import shutil
import random
from ultralytics import YOLO


train_path = "Dataset/train"
val_path = "Dataset/valid"
test_path = "Dataset/test"

model=YOLO("yolov8n.pt")
results=model.train(data= "Dataset/data.yaml", epochs=50, batch=32, imgsz=320)