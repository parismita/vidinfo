import PIL,numpy,os,time,cv2
from PIL import Image
import matplotlib.pylab as plt


'''create a folder called pics in your working directory and change the path to that folder'''

capture = cv2.VideoCapture('new.mp4')

i = 0
print time.asctime( time.localtime(time.time()) )
while(capture.isOpened()):
    #time sleep delays time by 5...not used as it still take succesive video frames not 5th video frame making the vidoe slow
    #time.sleep(5)
    img,frame = capture.read()

    cv2.imwrite('pics/pic{:>05}.jpg'.format(i),frame)
    i=i+1

    cv2.imshow('original',frame)
    if cv2.waitKey(33) == ord('a'):
        print "pressed a"
        break


