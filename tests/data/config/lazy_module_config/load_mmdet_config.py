# Copyright (c) OpenMMLab. All rights reserved.
if '_base_':
    from mmdet.configs.retinanet.retinanet_r50_caffe_fpn_1x_coco import *
    from mmdet.configs.retinanet.retinanet_r101_caffe_fpn_1x_coco import \
        model as r101

model = r101
