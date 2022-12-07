#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import SimpleITK as sitk
import os
import pandas as pd

input_segmentation_dir = '/input_segmentation/'
input_image_dir = '/input_image/'
path_img = os.path.join(input_image_dir,'{}.nii.gz')
path_seg = os.path.join(input_segmentation_dir,'{}.nii.gz')
path_pred = '/output/mortality.csv'

result = []

list_case = [k.split('.')[0] for k in os.listdir(input_image_dir)]

for case in list_case:
    img = sitk.ReadImage(path_img.format(case))
    seg = sitk.ReadImage(path_seg.format(case))

    # ==========your logic here. Below we do airway volume counting and thresholding as an example==============
    seg_numpy = sitk.GetArrayFromImage(seg)
    pred = seg_numpy.sum()/(seg_numpy.shape[0]*seg_numpy.shape[1]*seg_numpy.shape[2])
    # ==========================================================================================================
    result.append(pred)
    # record the result

# save the result
result = pd.DataFrame(result,columns=['pred'])
result['filename'] = list_case
result.to_csv(path_pred)
