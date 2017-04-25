# -*- coding: utf-8 -*-

"""Use CNN for Feature Extractor for t-SNE, etc"""

import mxnet as mx
import numpy as np
import cv2

import mxlib


def get_image(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    img = img[np.newaxis, :]
    return img

from collections import namedtuple
Batch = namedtuple('Batch', ['data'])

if __name__ == '__main__':
    # get model
    mxlib.get_model('http://data.mxnet.io/models/imagenet/resnext/101-layers/resnext-101', 0)
    sym, arg_params, aux_params = mx.model.load_checkpoint('resnext-101', 0)

    all_layers = sym.get_internals()
    #print(all_layers.list_outputs()[-10:-1])

    sym3 = all_layers['flatten0_output']
    mod3 = mx.mod.Module(symbol=sym3, context=mx.gpu())
    mod3.bind(for_training=False, data_shapes=[('data', (1, 3, 224, 224))])
    mod3.set_params(arg_params, aux_params)

    image_path = "C:/Users/kt/Documents/DataSet/cookpad/clf_test_224x224_0/00000000.png"
    img = get_image(image_path)
    mod3.forward(Batch([mx.nd.array(img)]))
    out = mod3.get_outputs()[0].asnumpy()
    print(out.shape)
    print(out)