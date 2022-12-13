import os
for i in range(21):
    root = "KITTI_ROOT=KITTI3D_tracking_3/" + str(i).zfill(4)
    print(root)
    os.system("./scripts/inference.py +experiments=dd3d_kitti_tracking_dla34.yaml " + root +  " EVAL_ONLY=True MODEL.CKPT=models/model_final_dal34.pth TEST.IMS_PER_BATCH=4")