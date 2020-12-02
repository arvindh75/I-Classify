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

os.system(
    "cd data/darknet && ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights ../../"
    + img
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
