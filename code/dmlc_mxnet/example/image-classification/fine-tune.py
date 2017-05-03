# -*- coding: utf-8 -*-

import os
import urllib.request
import time
import glob

import mxnet as mx
import numpy as np

from constant import PROJECT_ROOT
import constant
import mxlib


def download(url):
    filename = url.split("/")[-1]
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)


def get_model(prefix, epoch):
    download(prefix + '-symbol.json')
    download(prefix + '-%04d.params' % (epoch,))


def get_iterators(batch_size, data_shape=(3, 224, 224)):
    IMAGES_ROOT = PROJECT_ROOT + '/resources/rec_files/'
    train_rec = IMAGES_ROOT + "training.rec"
    valid_rec = IMAGES_ROOT + "validation.rec"

    train = mx.io.ImageRecordIter(
        path_imgrec=train_rec,
        data_name='data',
        label_name='softmax_label',
        batch_size=batch_size,
        data_shape=data_shape,
        shuffle=True,
        rand_crop=True,
        rand_mirror=True)

    val = mx.io.ImageRecordIter(
        path_imgrec=valid_rec,
        data_name='data',
        label_name='softmax_label',
        batch_size=batch_size,
        data_shape=data_shape,
        rand_crop=False,
        rand_mirror=False)
    return (train, val)


def fine_tune(mode):
    BATCH_PER_GPU = 20
    CLASS_NUM = constant.LABEL_NUM
    EPOCH_NUM = 30
    MODEL_NAME = 'resnext-101'
    ENABLE_VALIDATION = True
    GPU_NUM = 1

    print('学習済みモデルをDL', MODEL_NAME)
    if MODEL_NAME is 'resnext-101':
        get_model('http://data.mxnet.io/models/imagenet/resnext/101-layers/resnext-101', 0)
        sym, arg_params, aux_params = mx.model.load_checkpoint('resnext-101', 0)

    def get_fine_tune_model(symbol, arg_params, num_classes, layer_name='flatten0'):
        """
        symbol: the pre-trained network symbol
        arg_params: the argument parameters of the pre-trained model
        num_classes: the number of classes for the fine-tune datasets
        layer_name: the layer name before the last fully-connected layer
        """
        all_layers = sym.get_internals()
        net = all_layers[layer_name + '_output']
        net = mx.symbol.FullyConnected(data=net, num_hidden=num_classes, name='fc1')
        net = mx.symbol.Dropout(data=net, p=0.50000)
        net = mx.symbol.SoftmaxOutput(data=net, name='softmax')
        new_args = dict({k: arg_params[k] for k in arg_params if 'fc1' not in k})
        return (net, new_args)

    # 学習中のログ
    import logging
    head = '%(asctime)-15s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=head)

    (new_sym, new_args) = get_fine_tune_model(sym, arg_params, CLASS_NUM)

    def fit(symbol, arg_params, aux_params, train, val, batch_size, GPU_NUM):
        devs = [mx.gpu(i) for i in range(GPU_NUM)]
        mod = mx.mod.Module(symbol=new_sym, context=devs)
        mod.bind(data_shapes=train.provide_data, label_shapes=train.provide_label, force_rebind=True)
        mod.init_params(initializer=mx.init.Xavier(rnd_type='gaussian', factor_type="in", magnitude=2))
        mod.set_params(new_args, aux_params, allow_missing=True)

        start_time = time.time()
        mod.fit(train,
                eval_data=val,
                num_epoch=EPOCH_NUM,
                batch_end_callback=[
                    mx.callback.Speedometer(batch_size, 10),
                ],
                kvstore='device',
                optimizer='sgd',
                optimizer_params={
                    'learning_rate': 0.001,
                },
                eval_metric='acc')
        end_time = time.time()
        passed_minutes = int((end_time - start_time) / 60)
        print('学習完了', 'min', passed_minutes)
        mod.save_params(PROJECT_ROOT + '/temp/model_weight/resnext')

        if ENABLE_VALIDATION:
            metric = mx.metric.Accuracy()
            return mod.score(val, metric)
        else:
            return None

    if mode == 'train':
        batch_size = BATCH_PER_GPU * GPU_NUM
        (train, val) = get_iterators(batch_size)
        mod_score = fit(new_sym, new_args, aux_params, train, val, batch_size, GPU_NUM)
        if mod_score:
            result = list(mod_score)
            print('result', result)
            acc = result[0][1]
            print('学習モデルの評価結果', acc)

    if mode == 'predict':
        print('predictします')
        batch_size = BATCH_PER_GPU * GPU_NUM
        (train, val) = get_iterators(batch_size)
        train = None

        devs = [mx.gpu(i) for i in range(GPU_NUM)]
        mod = mx.mod.Module(symbol=new_sym, context=devs)
        mod.bind(data_shapes=val.provide_data, label_shapes=val.provide_label)
        mod.init_params(initializer=mx.init.Xavier(rnd_type='gaussian', factor_type="in", magnitude=2))
        mod.set_params(new_args, aux_params, allow_missing=True)

        # 学習済みパラメータをロード
        mod.load_params(PROJECT_ROOT + '/temp/model_weight/resnext')
        output_list = mod.predict(eval_data=val, num_batch=None)

        # 予測して確率を保存
        labels = []
        probabilities = output_list.asnumpy()
        for prob in probabilities:
            label = np.argmax(prob)
            labels.append(label)
        print('labels', labels)

        save_path = PROJECT_ROOT + '/temp/predicts/validation.npy'
        np.save(save_path, labels)

        # generate viewer HTML
        # TODO


def evaluate_validation():
    """evaluate validation results"""

    lst_path = PROJECT_ROOT + '/resources/rec_files/validation.lst'
    answer_labels = get_labels_from_lst(lst_path)
    predicted_labels = np.load(PROJECT_ROOT + '/temp/predicts/validation.npy')

    correct_num = 0
    incorrect_num = 0

    for i in range(len(answer_labels)):
        if answer_labels[i] == predicted_labels[i]:
            correct_num += 1
        else:
            incorrect_num += 1

    print('correct num', correct_num)
    print('incorrect num', incorrect_num)
    print('accuracy', correct_num / (correct_num + incorrect_num))

    f = open(PROJECT_ROOT + '/temp/HTML/validation_result.html', 'w')
    g = open(lst_path, 'r')
    import idol
    idol_list = idol.get_idol_list()
    for i, s in enumerate(g):
        spl = s.split()
        img_path = spl[2]

        if predicted_labels[i] != answer_labels[i]:
            answer_name = idol_list[answer_labels[i]].name
            predict_name = idol_list[predicted_labels[i]].name
            tag = '<img src="{}"> 正解: {} 予測結果: {}\n'.format(img_path, answer_name, predict_name)
            f.write(tag)



def get_labels_from_lst(lst_path):
    f = open(lst_path, 'r')
    labels = []
    for s in f:
        s = s.strip()
        if s != '':
            sep = s.split()
            label = int(sep[1])
            labels.append(label)
    f.close()
    return labels


if __name__ == '__main__':
    #make_directory()
    #fine_tune(mode='train')
    #fine_tune(mode='predict')
    evaluate_validation()