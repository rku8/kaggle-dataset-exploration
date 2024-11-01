"""You were at here"""
import os
import shutil
import random
from typing import List
# from pathlib import Path
from remove import delete_file
import pandas as pd


def main():
    delete_file(r'data\train')
    delete_file(r'data\test')
    os.makedirs(r'data\train\images', exist_ok=True)
    os.makedirs(r'data\test\images', exist_ok=True)

    path = r'dataset\train\images'
    image_paths = os.listdir(path)
    print(len(image_paths))
    random.shuffle(image_paths)

    TEST_SIZE = int(len(image_paths)*0.1)
    train_image_path = image_paths[TEST_SIZE:]
    test_image_path = image_paths[:TEST_SIZE]
    move_file(test_image_path)
    move_label(test_image_path, r'data\test\test.csv')

    # move_file(train_image_path)
    # move_label(train_image_path, r'data\train\train.csv')

def move_file(path_list: List[str])-> None:
    path = r'dataset\train\images'
    for file in path_list:
        src_path = os.path.join(path, file)
        dest_path = os.path.join(r'data\test\images', file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)

def move_label(path_list: List[str], dest_path: str)-> None:
    df1 = pd.read_csv(r'dataset\train\train.csv')
    df2 = pd.read_csv(r'dataset\sample_submission_ns2btKE.csv')
    df = pd.concat([df1, df2], ignore_index=True)
    img_df = pd.DataFrame(path_list, columns=['image'])
    merge_df = pd.merge(df, img_df)
    merge_df.to_csv(dest_path, index=False)

if __name__=="__main__":
    main()
    

