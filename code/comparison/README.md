# MXNet resnext vs Keras resnet

* In food image classification, resnext was excellent, 
but since there are many similar images in face classification, 
we need to compare which is superior.

# Comparison method

* The number of each idle image is assumed to be the same
* 80% of images for Training
* 20% of images for Test (validation omitted)

# Keras result

```
Epoch 100/100
Epoch 00099: val_loss did not improve
49s - loss: 0.2960 - acc: 0.9200 - val_loss: 1.3694 - val_acc: 0.6891
```

# MXNet result

```
2017-05-19 04:54:43,011 Epoch[99] Train-accuracy=0.466667
2017-05-19 04:54:43,011 Epoch[99] Time cost=106.693
2017-05-19 04:54:52,740 Epoch[99] Validation-accuracy=0.641818
```

# Result

* accuracy: resnet > resnext
* speed of training: resnet > resnext 
* resnext has room for parameter adjustment
