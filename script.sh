repo="https://github.com/pjreddie/darknet.git"
mkdir "data"
cd "data"
git clone "$repo"
cd "darknet"
wget "https://pjreddie.com/media/files/darknet19.weights"
wget "https://pjreddie.com/media/files/yolov3-tiny.weights"
cd ../../
