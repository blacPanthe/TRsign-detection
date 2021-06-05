import cv2 # importing cv2 lib
import numpy as np # importing numpy lib
from scipy.stats import itemfreq #This module contains a large number of probability
# distributions as well as a growing library of statistical functions
# from scipy.stat importing itemfreq
# itemfreq function help us to calculate the item frequencies
# Parameters :  arr : [array_like] input array.


def get_dominant_color(image, n_colors):# we are defining a function here
    pixels = np.float32(image).reshape((-1, 3)) #we are resizing the with help of reshape and float32
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    #cv.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached.
    #cv.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter.
    #cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
    flags = cv2.KMEANS_RANDOM_CENTERS
    #This flag is used to specify how initial centers are taken. Normally two flags are used for this
    # : cv.KMEANS_PP_CENTERS and cv.KMEANS_RANDOM_CENTERS.
    flags, labels, centroids = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)
    #now here we are using cv2. kmeans for data clustering which have parameters
    #samples( pixels), nclusters(n_color), criteria, attempts(10), flags
    palette = np.uint8(centroids)# is used unsigned 8 bit integer and that is range of pixel for centroid
    return palette[np.argmax(itemfreq(labels)[:, -1])]
    #it returns the indices of the highest item frequency


clicked = False
def onMouse(event, x, y, flags, param): # we are defining on Mouse event
    global clicked
    if event == cv2.EVENT_LBUTTONUP: # to check if left mose button was clicked
        clicked = True


cameraCapture = cv2.VideoCapture(0) #video capture from camera webacam
cv2.namedWindow('camera') #used to create window
cv2.setMouseCallback('camera', onMouse) # Sets mouse handler for the specified window.

# Read and process frames in loop
success, frame = cameraCapture.read()


while success and not clicked:
    cv2.waitKey(1) # i get a continuos live feed from my laptops webcam,
    # (0) i get still images everytime i close the window another one pops up with another picture
    success, frame = cameraCapture.read() #returns a bool (True/False). If the frame is read correctly, it will be True

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # here we converting(frame) img to Grayscale
    img = cv2.medianBlur(gray, 37)# it process the edges while removing the noises creating blur images
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,                     #hough transform used here for circle detection

                              1, 50, param1=120, param2=40)
    #hough circles is used to detect circles in an image
    #cv2.hough_gradient uses gradient information of edges for detecting circles

    if not circles is None:# uint16 type object representing the type of array scalars
        circles = np.uint16(np.around(circles))# np.around helps the user to evenly round array element to give number of circles here
        max_r, max_i = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]

            dominant_color = get_dominant_color(square, 2)
            if dominant_color[2] > 100:
                print("STOP")
            elif dominant_color[0] > 80:
                zone_0 = square[square.shape[0]*3//8:square.shape[0]
                                * 5//8, square.shape[1]*1//8:square.shape[1]*3//8]
                cv2.imshow('Zone0', zone_0)
                zone_0_color = get_dominant_color(zone_0, 1)

                zone_1 = square[square.shape[0]*1//8:square.shape[0]
                                * 3//8, square.shape[1]*3//8:square.shape[1]*5//8]
                cv2.imshow('Zone1', zone_1)
                zone_1_color = get_dominant_color(zone_1, 1)

                zone_2 = square[square.shape[0]*3//8:square.shape[0]
                                * 5//8, square.shape[1]*5//8:square.shape[1]*7//8]
                cv2.imshow('Zone2', zone_2)
                zone_2_color = get_dominant_color(zone_2, 1)


                if zone_1_color[2] < 60:
                    if sum(zone_0_color) > sum(zone_2_color):
                        print("LEFT")

                    else:
                        print("RIGHT")
                else:
                    if sum(zone_1_color) > sum(zone_0_color) and sum(zone_1_color) > sum(zone_2_color):
                        print("FORWARD")
                    elif sum(zone_0_color) > sum(zone_2_color):
                        print("FORWARD AND LEFT")
                    else:
                        print("FORWARD AND RIGHT")
            else:
                print("N/A")

        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imshow('camera', frame)


cv2.destroyAllWindows() #Destroys all of the HighGUI windows.
cameraCapture.release()