import os
import shutil

origin_folder = "/home/ubuntu/Masterarbeit/object_detection/dd3d/data/datasets/KITTI3D_tracking"
data_folder = "/home/ubuntu/Masterarbeit/object_detection/dd3d/data/datasets/KITTI3D_tracking_3"

scenes_numbers = os.listdir(data_folder)
scenes_numbers.sort()

# for scene_number in scenes_numbers:
#     images_dir = os.path.join(origin_folder,"training","image_2",scene_number)
#     images = os.listdir(images_dir)
#     images.sort()
#     #print(images)
#     for image in images:
#         src = os.path.join(images_dir,image)
#         dst = os.path.join(data_folder, scene_number,"training","image_2")
#         shutil.copy(src, dst)

# for scene_number in scenes_numbers:
#     images_dir = os.path.join(data_folder,scene_number, "training", "image_2")
#     images = os.listdir(images_dir)
#     images.sort()
#     images = [file_name.replace('.png', '') for file_name in images]
#     for image in images:
#         src = os.path.join(data_folder, scene_number, "training", "calib")
#         src_help = os.listdir(src)
#         src = os.path.join(src, src_help[0])
#         dst = os.path.join(data_folder, scene_number, "training", "calib", "{}.txt".format(image))
#         print(src)
#         print(dst)
#         shutil.copy(src, dst)


for scene_number in scenes_numbers:
    file = os.path.join(data_folder, scene_number, "training", "calib", "{}.txt".format(scene_number))
    os.remove(file)
