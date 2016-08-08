import matplotlib.pyplot as plt
import csv,gc
import matplotlib
import numpy as np
import nibabel as nb
from skimage import data, img_as_float
from skimage import exposure

BINS=32 # histogram bins
RANGE=(10.0,300.0)

im = nb.load('Fear197.nii')
im = im.get_data()
img = im[:,:,:,0]

img_eq = exposure.equalize_hist(im)
img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.03)

img_eqfinal = nb.Nifti1Image(img_eq, np.eye(4))
img_adapteqfinal = nb.Nifti1Image(img_adapteq, np.eye(4))

nb.save(img_eqfinal, "Fear197eq.nii")
nb.save(img_adapteqfinal, "Fear197adapteq.nii")




