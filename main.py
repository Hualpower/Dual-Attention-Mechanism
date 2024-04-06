

from ultralytics import YOLO
if __name__ == '__main__':
    # 加载模型
    model = YOLO("ultralytics-main/ultralytics/cfg/models/v8/yolov8n_ATT2.yaml")  # 从头开始构建新模型
    # model = YOLO("yolov8s.pt")  # 加载预训练模型（推荐用于训练）

    # Use the model
    results = model.train(data="ultralytics-main/yolo-bvn.yaml", epochs=1500, batch=16, workers=0, close_mosaic=0, name='cfg')  # 训练模型
    # results = model.val()  # 在验证集上评估模型性能
    # results = model("https://ultralytics.com/images/bus.jpg")  # 预测图像
    # success = model.export(format="onnx")  # 将模型导出为 ONNX 格式
