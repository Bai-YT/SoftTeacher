_base_="base.py"
model = dict(
    backbone=dict(
        depth=50,
        init_cfg=dict(checkpoint="open-mmlab://detectron2/resnet50_caffe"),
    )
)

data = dict(
    samples_per_gpu=13,
    workers_per_gpu=5,
    train=dict(
        sup=dict(
            ann_file="/home/ubuntu/project/data/COCO/annotations/instances_train2017.json",
            img_prefix="/home/ubuntu/project/data/COCO/train2017/",
        ),
        unsup=dict(
            # ann_file="/home/ubuntu/project/data/COCO/annotations/instances_unlabeled2017.json",
            # img_prefix="/home/ubuntu/project/data/COCO/unlabeled2017",
            ann_file="/home/ubuntu/project/data/LGS/COCO_format.json",
            img_prefix="/home/ubuntu/project/data/LGS/images/imgs_256_04_27",
        ),
    ),
    val=dict(
        ann_file="/home/ubuntu/project/data/COCO/annotations/instances_val2017.json",
        img_prefix="/home/ubuntu/project/data/COCO/val2017/",
    ),
    sampler=dict(
        train=dict(
            sample_ratio=[1, 1],
        )
    )
)

semi_wrapper = dict(
    train_cfg=dict(
        unsup_weight=2.0,
    )
)

optimizer = dict(lr=0.01, weight_decay=1e-4, momentum=0.9)
# lr_config = dict(step=[120000 * 2.5, 170000 * 2.5])
lr_config = dict(step=[300000, 425000])
# lr_config = dict(step=[150000, 212500])
# runner = dict(_delete_=True, type="IterBasedRunner", max_iters=180000 * 2.5)
# runner = dict(_delete_=True, type="IterBasedRunner", max_iters=225000)
runner = dict(_delete_=True, type="IterBasedRunner", max_iters=450000)
