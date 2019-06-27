import numpy as np
import cv2
import math

cap = cv2.VideoCapture("robos.avi")

img = cv2.imread("robot.jpg")
sift = cv2.xfeatures2d.SIFT_create()


# Features Matching
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)
fast = cv2.FastFeatureDetector_create()
star = cv2.xfeatures2d.StarDetector_create()
br = cv2.BRISK_create();
# find and draw the keypoints
kp_image = fast.detect(img, None)
kp_image, desc_image = sift.compute(img, kp_image)
img = cv2.drawKeypoints(img, kp_image, img)
cv2.imshow("IMG", img)
desc_image = np.float32(desc_image)

while(True):
    status, frame = cap.read()
    if status:
        grayframe = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)

        kp_grayframe = fast.detect(grayframe, None)
        kp_grayframe, desc_grayframe = sift.compute(grayframe, kp_grayframe)
        desc_grayframe = np.float32(desc_grayframe)
        #kp, desc_grayframe = sift.detectAndCompute(grayframe, None)
        grayframe = cv2.drawKeypoints(grayframe, kp_grayframe, grayframe)
        cv2.imshow("GRAYFRAME", grayframe)
        matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
        good_points = []
        for m, n in matches:
            if m.distance < 0.8*n.distance:
                good_points.append(m)

        img3 = cv2.drawMatches(img, kp_image, grayframe, kp_grayframe, good_points, grayframe)
        cv2.imshow("img3", img3)

        #if len(good_points) > 10:
        #    query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        #    train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        #    matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        #    matches_mask = mask.ravel().tolist()
        #    # Perspective transform
        #    h, w = img.shape
        #    pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        #    ldst = cv2.perspectiveTransform(pts, matrix)
        #    dst = np.int32(ldst)
        #    midLeft = (int((dst[0][0][0] + dst[1][0][0]) / 2), int((dst[0][0][1] + dst[1][0][1]) / 2))
        #    midRight = (int((dst[2][0][0] + dst[3][0][0]) / 2), int((dst[2][0][1] + dst[3][0][1]) / 2))
        #    center = (int((midLeft[0] + midRight[0])/2), int((midLeft[1] + midRight[1])/2))
        #    homography = cv2.polylines(frame, [np.int32(ldst)], True, (255, 0, 0), 3)
        #    x1 = 100
        #    x2 = midRight[0] - center[0]
        #    y1 = 0
        #    y2 = midRight[1] - center[1]
        #    cos = (x1*x2 + y1*y2)
        #    bot = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2)) * math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
        #    cos = cos / bot
        #    angle = np.degrees(math.acos(cos))
        #    if midRight[1] < center[1]:
        #        angle *= -1
        #    print(angle)
        #    cv2.circle(homography, midLeft, 10, (0, 255, 255), -1)
        #    cv2.circle(homography, midRight, 10, (0, 255, 255), 2)
        #    cv2.circle(homography, center, 10, (0, 0, 255), 2)
        #    cv2.imshow("Homography", homography)
        #else:
        #    cv2.imshow("Homography", grayframe)

    else:
        cap = cv2.VideoCapture("ROTATION,avi")
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
