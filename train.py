from ultralytics import YOLO


def train():
    # Load the pretrained YOLOv8 nano model
    model = YOLO("yolov8n.pt")

    # Train on your electrical symbol dataset
    model.train(
        data="dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        workers=2,
        project="ElectricalEstimatorAI",
        name="ElectricalSymbols"
    )

    # Validate the trained model
    model.val()

    print("Training completed successfully!")
    print("Your trained model will be saved as:")
    print("ElectricalEstimatorAI/ElectricalSymbols/weights/best.pt")


if __name__ == "__main__":
    train()