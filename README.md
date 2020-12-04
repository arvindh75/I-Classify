# Image Classifier based on yolov3
## Instructions to run
- `bash script.sh <tiny/large/both>`
> Tiny uses yolov3-tiny weights (~30mb) while large uses yolov3 weights (~300mb).
Ex : `bash script.sh tiny` 
Default option is tiny.
- Run `python main.py`
- The resultant image will be stored `data/darknet/predictions.jpg` and the resultant text for classification using `darknet19.weights` will be stored in `results.txt`.
## Note
Large weight model may take upto a minute to process depending on the resolution and complexity of the image on iGPU while it will take approximately half the time on a dGPU (Nvidia GTX 1650).
