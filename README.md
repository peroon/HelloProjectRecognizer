# Hello! Project Recognizer

# Goals

* Recognize idol in video using Deep Learning
* YouTube viewer using the result information

# Viewer Demo

* [list view](https://peroon.github.io/HelloProjectRecognizer/view/list/list.html) 

# Official Page

[Hello! Project](http://www.helloproject.com)

# Groups

* [℃-ute](http://www.helloproject.com/c-ute/)
* [Morning Musume '17](http://www.helloproject.com/morningmusume/)
* [Angerme](http://www.helloproject.com/angerme/)
* [Juice=Juice](http://www.helloproject.com/juicejuice/)
* [Country Girls](http://www.helloproject.com/countrygirls/)
* [Kobushi Factory](http://www.helloproject.com/kobushifactory/)
* [Tsubaki factory](http://www.helloproject.com/tsubakifactory/)
    
# How to prepare training images

## Get images

* Google Image Search
* Bing Image Search
* Youtube & Face Detection

## Crop faces

* refer to face.py
* face detection using dlib
* detected faces are placed in the candidates directory

## Sort by hand

* candidates are sorted by hand and placed in recognized idol directory

## Eliminate by hand

* Remove almost same image and blurred image
* This prevents the number of training data from increasing unnecessarily
* TODO: Efficiency can be improved if there is a tool to sort by image similarity

# Classifier

* Keras Resnet
* MXNet Resnext

# What can this framework do?

* Idol face recognition
    * Training
    * Prediction
* Visualization
    * using t-SNE
    * face similarity between idols
    
# Accuracy 

* 0.627 on validation set (3000 images)

# Environment Settings

* same as [food classification settings](https://github.com/peroon/deepanalytics_food_classification)

# How to collect training images
## Google Search API

* Place text file with key written to  secret/google_search_api_key
    * https://developers.google.com/custom-search/json-api/v1/overview
* API Manager
    * https://console.developers.google.com
    * You can see the number of queries remaining today
    * Limit a day is 100 queries (few...)
* Get cx
    * https://cse.google.com/cse/all
* Request URL example
    * https://developers.google.com/custom-search/json-api/v1/using_rest
    
# How to add a video to list

* Download mp4 by running code/collect/youtube_downloader.py
* Run code/video_analyzer.py after assign youtube id
* Run docs\view\list\list_data_maker.py

# TODO

* Since it is meaningless to learn almost the same face image, 
we want to eliminate overlapped images by sorting by image similarity
* Make READMEs ogranized