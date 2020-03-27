import numpy as np
import cv2 as cv
import os
import glob

"""
去阴影并提亮
"""

def shadow_remove(color_img):
    """
    去阴影
    :param color_img:原图
    :return: 去阴影之后的图
    """
    g_img = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)
    blurred_img = cv.GaussianBlur(g_img, (121, 121), 31)
    g_img = np.divide(g_img.astype(np.float), 255)
    blurred_img = np.divide(blurred_img.astype(np.float), 255)
    rs_img = np.divide(g_img, blurred_img)  # 去阴影
    rs_img = cv.pow(rs_img, 1.5)  # 提亮
    rs_img = np.maximum(rs_img, 0.0)
    rs_img = np.minimum(rs_img, 1.0)
    rs_img = np.multiply(rs_img, 255)
    rs_img = rs_img.astype(np.uint8)
    return rs_img