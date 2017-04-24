# -*- coding: utf-8 -*-

"""Use CNN for Feature Extractor for t-SNE, etc"""

import mxnet as mx
import numpy as np

import mxlib

if __name__ == '__main__':
    # get model
    mxlib.get_model('http://data.mxnet.io/models/imagenet/resnext/101-layers/resnext-101', 0)
    sym, arg_params, aux_params = mx.model.load_checkpoint('resnext-101', 0)

    internals = sym.get_internals()
    print(internals)

    # print layer name
    for internal in internals:
        print(internal)

    fea_symbol = internals["pool1"]

    feature_extractor = mx.model.FeedForward(ctx=mx.gpu(), symbol=fea_symbol, numpy_batch_size=1,
                                             arg_params=arg_params, aux_params=aux_params,
                                             allow_extra_params=True)