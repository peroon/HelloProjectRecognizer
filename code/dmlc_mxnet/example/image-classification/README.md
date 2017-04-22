# Idol recognition using mxnet (resnext)

# Training Steps


# Prediction Steps

* convert video to frames (images)
* face detection using dlib on them
    * and save the detected face position
* all detected faces are packed to rec file as input
* detected face's label is predicted using CNN
* merge information of frame, position, label into JSON

# Viewer

* prediction is checked by viewer
* it imposes additional idol information on movie
* maybe HTML & JSON & Youtube