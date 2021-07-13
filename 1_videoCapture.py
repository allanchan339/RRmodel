import cv2
import threading
import time

flag = True

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID

    def run(self):
        print("Starting "+self.previewName)
        camPreview(self.previewName, self.camID)


def camPreview(previewName, camID):
    global flag
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval and flag:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        # video recording
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)


# Create two threads as follows
def main():
    global flag
    thread1 = camThread("Camera 1", 0)
    thread2 = camThread("Camera 2", 1)
    thread1.start()
    thread2.start()
    while flag:
        time.sleep(5)
        flag = False
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()
# thread1.join()