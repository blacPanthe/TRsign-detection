# TRsign-detection
Basic Traffic sign recognition system, with OpenCv

for begginners in OpenCV
Basic Traffic signs like := Stop, Forward, leFt , right, forward and left, and forward and right are detected.

So Talking about Code
 

First of all we are using Python language here with the help of Jet brains Pycharm tool we are coding and Using OPENCV for the visualization.

There are three major steps here:
1.Use of Hough transform concept to detect the circles in the Traffic Sign
2.Comparing of the cluster after the clusters are detected, these are divided into different zones and compared
3. Use of K means clustering to detect the clusters in different zones of the live capture

We have Imported cv2, numpy and Scipy.stats libraries
So further firstly we define function for K means clustering, so here we can randomly chose the clusters ,  and then after choosing the clusters we are defining the mouse events.
Further we are using the camera to do live capturing using over default webcam.And then creating a named window for it.
Further the live frame we got from the camera capture we are converting it to grayscale and blurring it, and then finally using the Hough transform for detecting the circles. we are using Hough circles for detecting the circles

![Screenshot (562)](https://user-images.githubusercontent.com/66546484/120888480-23f87e00-c616-11eb-827f-cd143aac2077.png)

Fig 2 green circles are hough circles detection
![Screenshot (576)](https://user-images.githubusercontent.com/66546484/120888931-83578d80-c618-11eb-95da-ccddee9f3328.png)
![image](https://user-images.githubusercontent.com/66546484/120888784-e3016900-c617-11eb-87d5-5514c23149d6.png)

First the shape is given the priority

Then if they are not circles then we are creating variables which then manages the length of circles to detect in Hough transform, to get the square, then we have the x, y variables to get the square frame with the help of the new variables made.
Further when the square frames are made we are comparing the dominant colors of the squares
 If the color is greater than 100 then we can print STOP or else
 
![Screenshot (563)](https://user-images.githubusercontent.com/66546484/120888494-2fe44000-c616-11eb-9ead-98501b690d6b.png)

Fig 3 these are the 3 square zones made by k Means clustering for detecting the sign

We create 3 zones out of it, zone0, zone 1, zone2, here the square windows are made to show the different zone of colors
Further the colors in the zone are compared and particularly the traffic signs are given there names


![Screenshot (570)](https://user-images.githubusercontent.com/66546484/120888975-b3069580-c618-11eb-830f-7c25356be319.png)

Fig 4 there is then d hough circle detection as well as the dominant color comparing
![image](https://user-images.githubusercontent.com/66546484/120888829-21972380-c618-11eb-86f8-21ba44f4be8c.png)
![image](https://user-images.githubusercontent.com/66546484/120888839-2cea4f00-c618-11eb-9a3e-cd08ef3ed3bd.png)

if both the signs are circles then dominant Color is given the priority

At the end we are just giving X , Y and radius of the circles with help of I coordinate
And after comparing we get the result and the name of the traffic sign displaying on the console.

![Screenshot (570)](https://user-images.githubusercontent.com/66546484/120888634-fb24b880-c616-11eb-937b-fc7feefacff9.png)

Fig 5 Display of the traffic sign name on the console
And at last we destroy all window and end the camera capture





IV.discussion of strategy adopted

Further talking about the strategy adopted

![image](https://user-images.githubusercontent.com/66546484/120888998-c1ed4800-c618-11eb-9013-64a95ec3ca93.png)

There are three major steps here:
1.Use of Hough transform concept (https://en.wikipedia.org/wiki/Hough_transform#:~:text=The%20Hough%20transform%20is%20a,shapes%20by%20a%20voting%20procedure.)
2.Comparing of the cluster using dominant color method
3.K means clustering Concept

These strategies are important and are basic to the traffic sign detection system.
So first method used here is the Hough Transform method which is used to detect the circles in the sign(hough circles method )is usually used to do so. So to separate the different shapes 
Further we use the dominant color comparison , to do do comparison between different color present in the sign as we red color is dominant it will get priority , and its traffic sign output will be show.
After the Comparison with the help of K means clustering method we create 3 zones(cluster) to see if which trafic sign it is and it finally give us the output 
 This all help in making a basic traffic sign recognition system
