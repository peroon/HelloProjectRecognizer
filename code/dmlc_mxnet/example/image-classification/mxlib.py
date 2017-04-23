# -*- coding: utf-8 -*-

import os
import urllib.request

import mxnet as mx
import numpy as np


def download(url):
    filename = url.split("/")[-1]
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)


def get_model(prefix, epoch):
    download(prefix + '-symbol.json')
    download(prefix + '-%04d.params' % (epoch,))


if __name__ == '__main__':
    pass