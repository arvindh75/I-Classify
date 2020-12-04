## Instructions to run
- `bash script.sh <tiny/large/both>`
> Tiny uses yolov3-tiny weights (~30mb) while large uses yolov3 weights (~300mb).
Ex : `bash script.sh tiny` 
Default option is tiny.
- Run ```python` main.py``
- The resultant image will be stored `data/darknet/predictions.jpg` and the resultant text for classification using `darknet19.weights` will be stored in `results.txt`.
