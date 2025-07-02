from ultralytics import YOLO


# 加载一个模型
model = YOLO('D:/software/Pycharm/Pycharm_Project/ultralytics-main/ultralytics/cfg/models/v8/yolov8.yaml')  # 从YAML建立一个新模型
model = YOLO('D:/software/Pycharm/Pycharm_Project/ultralytics-main/ultralytics/weights/yolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('D:/software/Pycharm/Pycharm_Project/ultralytics-main/ultralytics/cfg/models/v8/yolov8.yaml').load('D:/software/Pycharm/Pycharm_Project/ultralytics-main/ultralytics/weights/yolov8n.pt')  # 从YAML建立并转移权重

# 训练模型
results = model.train(data='D:/software/Pycharm/Pycharm_Project/ultralytics-main/ultralytics/cfg/datasets/my_coco.yaml', epochs=100, imgsz=160, device=0)
