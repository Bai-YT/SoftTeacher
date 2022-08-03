_base_ = "base.py"
model = dict(
    backbone=dict(
        depth=50,
        init_cfg=dict(checkpoint="open-mmlab://detectron2/resnet50_caffe"),
    )
)

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=7,
    train=dict(
        ann_file="/home/ubuntu/project/data/COCO/annotations/instances_train2017.json",
        img_prefix="/home/ubuntu/project/data/COCO/train2017/",
    ),
    val=dict(
        ann_file="/home/ubuntu/project/data/COCO/annotations/instances_val2017.json",
        img_prefix="/home/ubuntu/project/data/COCO/val2017/",
    ),
)

optimizer = dict(lr=0.0, weight_decay=1e-4)
lr_config = dict(step=[120000 * 4, 170000 * 4])
runner = dict(_delete_=True, type="IterBasedRunner", max_iters=180000 * 4)
