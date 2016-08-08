import matplotlib.pyplot as plt
import csv,gc
import matplotlib
import numpy as np
import nibabel as nb
import scipy.ndimage
BINS = 32

a = np.random.randint(0,10,(2,2,2))

## Converting matrix into array

#// b = np.asarray(a)[:,:,0]

## This is the 3d histogram
#// H = np.histogramdd(b, bins = 32)
#// plt.plot(H)
#// plt.savefig("3dhistogram.png", H)
##print "H shape is" 
##print H.shape
###########################

''' 
The above process gives me an error specifically because of the b = np.asarray(a)[:,:,0] step which does not play nicely with histogramdd.

'''

for z in range(10):
   for y in range(10):
      for x in range(10):

         data = a
      
         (hist, bins) = np.histogram(data[data > 0], BINS, range=(0,BINS))
         hist_sum = 0.0
         hist_sum = np.add(hist_sum, hist)

         print "Processed cube {} {} {}".format(x,y,z)

## This is the 2d representation of the histogram
plt.hist(hist_sum)
plt.savefig('2drepresenationof3d.png')

'''
hist_norm_histogram = np.histogram(data)
hist_norm = np.zeros(hist_norm_histogram)

This gives me an error - if I try to do 
hist_norm = np.zeros(hist_norm_histogram.shape())
it gives me a tuple from which I have to choose - however if I index the tuple it will result in the normalized histogram taking the dimensions of a 2D array

If I try to do 
hist_norm = np.zeros(hist_norm_histogram)
It gives me a scalar must be a length of 1 error indicating that numpy is not playing nicely with a math operation
'''

'''
hist_norm_histogram = np.histogram(data)
hist_norm = hist_norm_histogram

i = 0
i < 32
while True:
   ####Broadcast error: hist_norm[i] = hist_norm_histogram[i] / hist_sum
   ####Broadcast error: hist_norm[i] = np.divide(hist_norm_histogram[i], hist_sum)
   i = i+1
numpy.savetxt("normalizedexperiment.csv", hist_norm, delimiter=",")

plt.hist(hist_norm)
plt.savefig('normalizedhistogram.png')
'''

hist_norm_histogram = hist_sum
hist_norm = hist_norm_histogram

new_hist_sum = 0.0
j = 0
j < 32
while True:
   new_hist_sum += j

i = 0
i < 32
while True:
   hist_norm[i] = hist_norm_histogram[i] / new_hist_sum   ####Broadcast error: hist_norm[i] = np.divide(hist_norm_histogram[i], hist_sum)
   i = i+1
numpy.savetxt("normalizedexperiment.csv", hist_norm, delimiter=",")

plt.hist(hist_norm)
plt.savefig('normalizedhistogram.png')
