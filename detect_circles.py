# USAGE
# python detect_circles.py --image images/simple.png

# import the necessary packages

import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 75)

# ensure at least some circles were found


	# loop over the (x, y) coordinates and radius of the circles
for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
	cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		

	# show the output image
	cv2.imwrite('output.jpg',output)
	cv2.waitKey(0)