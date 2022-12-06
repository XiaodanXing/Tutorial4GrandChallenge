#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import SimpleITK as sitk
import os
import pandas as pd

input_segmentation_dir = '/input_segmentation/'
input_image_dir = '/input_image/'
path_img = os.path.join(input_image_dir,'{}.nii.gz')
path_seg = os.path.join(input_segmentation_dir,'{}.nii.gz')
path_pred = '/output/'
result = [[],[]]

list_case = [k for k in os.listdir(input_image_dir)]

for case in list_case:
    img = sitk.ReadImage(path_img.format(case))
    seg = sitk.ReadImage(path_seg.format(case))

    ##
    # your logic here. Below we do airway volume counting as an example
    ##

    # using SimpleITK to do binary thresholding between 100 - 10000
    vs_pred = stik(
    cochlea_pred = sitk.BinaryThreshold(t2_img, lowerThreshold=900, upperThreshold=1100)

    result = vs_pred + 2*cochlea_pred

    # save the segmentation mask
    sitk.WriteImage(result, path_pred.format(case))
