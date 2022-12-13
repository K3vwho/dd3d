# Copyright 2021 Toyota Research Institute.  All rights reserved.
import logging
import os
from functools import partial

from detectron2.data import DatasetCatalog

from tridet.data.datasets.kitti_3d_tracking.build import build_monocular_kitti3d_tracking_dataset, register_kitti_3d_tracking_metadata

LOG = logging.getLogger(__name__)

#KITTI_ROOT = 'KITTI3D_tracking_3/0000'




DATASET_DICTS_BUILDER = {
    # Monocular datasets
    "kitti_3d_tracking_train": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='train')),
    "kitti_3d_tracking_train_project_box3d": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='train', box2d_from_box3d=True)),
    "kitti_3d_tracking_train_right_cam": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='train', sensors=('camera_3', ))),
    "kitti_3d_tracking_train_both_cams":
    (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='train', sensors=('camera_2', 'camera_3'))),
    "kitti_3d_tracking_val": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='val')),
    "kitti_3d_tracking_trainval": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='trainval')),
    "kitti_3d_tracking_test": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='test')),
    "kitti_3d_tracking_overfit": (build_monocular_kitti3d_tracking_dataset, dict(mv3d_split='train', max_num_items=32)),
}


METADATA_BUILDER = {name: (register_kitti_3d_tracking_metadata, {}) for name in DATASET_DICTS_BUILDER.keys()}


def register_kitti_3d_tracking_datasets(required_datasets, cfg):
    kitti_3d_tracking_datasets = sorted(list(set(required_datasets).intersection(DATASET_DICTS_BUILDER.keys())))
    if kitti_3d_tracking_datasets:
        LOG.info(f"KITTI-3D-tracking dataset(s): {', '.join(kitti_3d_tracking_datasets)} ")
        for name in kitti_3d_tracking_datasets:
            fn, kwargs = DATASET_DICTS_BUILDER[name]
            kwargs.update({'root_dir': os.path.join(cfg.DATASET_ROOT, cfg.KITTI_ROOT)})
            DatasetCatalog.register(name, partial(fn, **kwargs))

            fn, kwargs = METADATA_BUILDER[name]
            kwargs.update({'coco_cache_dir': cfg.TMP_DIR})
            fn(name, **kwargs)
    return kitti_3d_tracking_datasets
