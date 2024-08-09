from cv2 import VideoCapture, imshow, imwrite, waitKey

cam_port = 0
cam = VideoCapture(cam_port)

# Reading the input using the camera
inp = input('Enter person name')

# If image is detected without any error, show result
while True:
    result, image = cam.read()
    imshow(inp, image)
    if waitKey(1) & 0xFF == ord('q'):
        imwrite(inp + ".png", image)
        print("Image taken")
        break
