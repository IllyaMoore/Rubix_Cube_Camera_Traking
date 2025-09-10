from ultralytics import YOLO
import cv2



model = YOLO(r'') #! -- model of your choice
def run(img):
    result = model(img)
    result[0].show()