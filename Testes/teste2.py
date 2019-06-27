import cv2

img = cv2.imread('robo.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
freakExtractor = cv2.xfeatures2d.FREAK_create()
# find and draw the keypoints
kp = fast.detect(img, None)
kp, cd = freakExtractor.compute(img, kp)
img2 = cv2.drawKeypoints(img, kp, img)


cv2.imshow('fast_true.png',img2)


cv2.waitKey(10000)