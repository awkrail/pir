import os
import argparse
import numpy as np
from fabric.colors import green
from PIL import Image

def is_image_file(target_file):
    _, ext = os.path.splitext(target_file)
    if ext == ".jpg" or ext == ".png":
        return True
    else:
        return False

def check_exact_match(query_image_path, target_files):
    query_image = np.array(Image.open(query_image_path).convert("RGB"))
    for target_file in target_files:
        target_image = np.array(Image.open(target_file).convert("RGB"))
        if query_image.shape == target_image.shape:
            if (target_image == query_image).all():
                print(green("[ExactMatched]:"), target_file)

def main():
    parser = argparse.ArgumentParser(description="Image retrieval tool to investigate whether the same images to the query exist in the target directory.")
    parser.add_argument("--query_path", "-q", type=str, required=True, help="query image path")
    parser.add_argument("--target_dir", "-t", type=str, required=True, help="target directory")
    args = parser.parse_args()

    query_image_path = args.query_path
    target_files = [os.path.join(args.target_dir, target_file) for target_file in os.listdir(args.target_dir) if is_image_file(target_file)]
    check_exact_match(query_image_path, target_files)