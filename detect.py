from ultralytics import YOLO
from IPython.display import Image, display

model = YOLO('yolov8n.pt')
results = model('https://ultralytics.com/images/bus.jpg')
results[0].save('results.jpg')
print("Detection completed. Saved as results.jpg")
