import os
import random
import shutil

# Source folder path
source_folder = 'C:/Users/prbop/Desktop/Universidade/S6/BSP/Repo/pytorch-CycleGAN-and-pix2pix/datasets/pixelart/trainB'

# Destination folder path
destination_folder = 'C:/Users/prbop/Desktop/Universidade/S6/BSP/Repo/pytorch-CycleGAN-and-pix2pix/datasets/pixelart/testB'

# Number of images to select
num_images = 902

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Select random images
random_images = random.sample(files, num_images)

# Move selected images to the destination folder
for image in random_images:
    source_path = os.path.join(source_folder, image)
    destination_path = os.path.join(destination_folder, image)
    shutil.move(source_path, destination_path)

print(f"{num_images} random images moved to {destination_folder}.")
