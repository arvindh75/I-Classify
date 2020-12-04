weight=0
var1="tiny"
var2="large"
var3="both"

if [ $# -gt 0 ]
then
    if [ "$1" == "$var1" ]
    then
        weight=0
    elif [ "$1" == "$var2" ]
    then
        weight=1
    elif [ "$1" == "$var3" ]
    then
        weight=2
    else
        weight=0
    fi
fi

repo="https://github.com/pjreddie/darknet.git"
mkdir "data"
cd "data"
git clone "$repo"
cd "darknet"
if [ $weight -lt 1 ]
then
    wget "https://pjreddie.com/media/files/yolov3-tiny.weights"
elif [$weight -gt 1]
then
    wget "https://pjreddie.com/media/files/yolov3.weights"
    wget "https://pjreddie.com/media/files/yolov3-tiny.weights"
else
    wget "https://pjreddie.com/media/files/yolov3.weights"
fi
wget "https://pjreddie.com/media/files/darknet19.weights"
cd ../../
