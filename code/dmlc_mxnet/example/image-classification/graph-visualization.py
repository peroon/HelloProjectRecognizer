# -*- coding: utf-8 -*-

"""Use CNN for Feature Extractor for t-SNE, etc"""

import mxnet as mx
import numpy as np

import mxlib

if __name__ == '__main__':
    # get model
    mxlib.get_model('http://data.mxnet.io/models/imagenet/resnext/101-layers/resnext-101', 0)
    sym, arg_params, aux_params = mx.model.load_checkpoint('resnext-101', 0)

    # visualize
    a = mx.visualization.plot_network(sym)
    a.render('graphviz_graph')