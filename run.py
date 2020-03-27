import numpy as np
import cv2 as cv
import os
import glob
import argparse

from process.remove_shadow import shadow_remove

def get_arg():
    paser = argparse.ArgumentParser()
    paser.add_argument("-i", "--image_address", required=True, help="image folder address")
    paser.add_argument("-o", "--output_address", required=True, help="output folder address")
    paser.add_argument("-t", "--type_of_process", type=int, default=0, help="type of process applied on the paper \n 0: remove shadow \n 1: ")
    args = paser.parse_args()
    return args

if __name__ == "__main__":
    args = get_arg()
    if not os.path.exists(args.output_address):
        os.mkdir(args.output_address)
    # 获取图片
    post_fix = ["*JPG", "*jpg", "*png"]
    img_address_list = []
    for f in post_fix:
        img_address_list.extend(glob.glob(os.path.join(args.image_address,"*jpg")))

    for add in img_address_list:
        img = cv.imread(add)
        img_name = os.path.basename(add)
        if args.type_of_process == 0:
            r_img = shadow_remove(img)
            r_img = cv.cvtColor(r_img, cv.COLOR_GRAY2BGR)
        cv.imwrite(os.path.join(args.output_address,img_name), r_img)