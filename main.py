import os
import subprocess
import cv2


def classify_image(img_name):
    os.system(
        "cd data/darknet && ./darknet classifier predict cfg/imagenet1k.data cfg/darknet19.cfg darknet19.weights ../../"
        + img_name
        + " > ../../results.txt"
    )
    results_file = open("results.txt", "r")
    results = results_file.readlines()
    results_file.close()
    return results


img = input("Enter image path: ")
var = int(input("Enter 0 for tiny and 1 for large: "))
if var != 0 and var != 1:
    print("Wrong option, choosing tiny by default")
    var = 0

if var == 0:
    os.system(
        "cd data/darknet && ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights ../../"
        + img
    )
if var == 1:
    os.system(
        "cd data/darknet && ./darknet detect cfg/yolov3.cfg yolov3.weights ../../" + img
    )
pred = cv2.imread("data/darknet/predictions.jpg")
cv2.imshow("Prediction", pred)
cv2.waitKey(0)
cv2.destroyAllWindows()

result_list = classify_image(img)
output = "The Classification: \n"
for r in result_list:
    output += r
print(output)
