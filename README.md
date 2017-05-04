# Hello! Project Recognizer

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

* Google Image Search
* Bing Image Search
* Youtube & Face Detection

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

* TODO

# How to collect training images
## Google Search API

* Place text file with key written to  secret/google_search_api_key
    * https://developers.google.com/custom-search/json-api/v1/overview
* API Manager
    * https://console.developers.google.com
    * You can see the number of queries remaining today
    * Limit a day is 100 queries (little...)
* Get cx
    * https://cse.google.com/cse/all
* Request URL example
    * https://developers.google.com/custom-search/json-api/v1/using_rest
* Package for connection
    * requests http://docs.python-requests.org/en/master/
    
## Others

* TODO