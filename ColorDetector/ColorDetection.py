import os
import cv2 as Application
import threading
from PIL import Image

Camera = Application.VideoCapture(0)
Color = "Color"
Capture = False
Exit = False

def Detect():
    if not Exit:
        threading.Timer(5, Detect).start()
        global Capture
        Capture = True



Detect()
while(True):
    CameraLayout = Camera.read()[1]
    Layout = Camera.read()[1]
    Application.putText(Layout, Color, (20, 40), Application.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, Application.LINE_AA)

    Application.imshow('Color Detector', Layout)
    
    if Capture:
        Application.imwrite("Image.png", CameraLayout)
        File = Image.open(os.getcwd()+r"\Image.png")
        Pixels = File.load()
        Red, Green, Blue, Unknown = (0, 0, 0, 0)
        for W in range(File.size[0]//2):
            for H in range(File.size[1]):
                Colors = File.getpixel((W, H))
                if Colors[0] >= Colors[1] + Colors[2]: Red+=1
                elif Colors[1] >= Colors[0] + Colors[2]: Green+=1
                elif Colors[2] >= Colors[0] + Colors[1]: Blue+=1
                else: Unknown+=1
        Colors = [("Red", Red), ("Green", Green), ("Blue", Blue), ("Unknown", Unknown)]        
        Colors.sort(reverse=True, key=lambda C: C[1])
        Color = Colors[0][0]
        Capture = False

    keyCode = Application.waitKey(1)
    if Application.getWindowProperty('Color Detector', Application.WND_PROP_VISIBLE) < 1:
        break

Camera.release()
Application.destroyAllWindows()
Exit = True
exit()