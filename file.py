import os
print(os.listdir(r'train\images'))
images = os.listdir(r'train\images')
images_dir = []
for image_name in images:
    images_dir.append(image_name.split('.')[0])

print(images_dir)