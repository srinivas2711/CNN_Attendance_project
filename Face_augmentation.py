import tensorflow
import numpy as np
import os
img=tensorflow.keras.preprocessing.image.load_img(
    f'C:/Users/Srini/Desktop/srini/{stud_cls}/{recent_file}', grayscale=False, color_mode="rgb", target_size=None, interpolation="nearest")
imag_num=np.array(img)
x=imag_num.reshape((1,) + imag_num.shape)
i=0
fname=input("Enter folder name you want to create in your training directory..")
folder_path = f'C:/Users/Srini/Desktop/Proj_images/Training_images/{fname}'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
for batch in train_img.flow(x, batch_size=1, save_to_dir=f'C:/Users/Srini/Desktop/Proj_images/Training_images/{fname}',
                            save_prefix="srini_face", save_format="jpeg"):
    i=i+1
    if(i>35):
        break
print("Hurray!...Data augmentation done successfully")
print("Now you can access our RECOGNITION SYSTEM!!!!!!!!")


#Map training and testing folder
import shutil
import os
src_folder = "C:/Users/Srini/Desktop/Proj_images/Training_images/"
dst_folder = "C:/Users/Srini/Desktop/Proj_images/Testing_images"
if os.path.exists(dst_folder):
    shutil.rmtree(dst_folder)
shutil.copytree(src_folder, dst_folder)
print("Images copied from Train to Test Folder!!")
