import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
  
img = cv2.imread('alexample.png',0)
  
hist,bins = np.histogram(img.flatten(),256,[0,256])
  
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
  
hist_norm = np.zeros(hist.shape)
hist_sum = 0.0

for bins in hist:
   hist_sum += bins

for bins in hist:
   hist_norm[i] = hist[i]/hist_sum

histnorm = Image.fromarray(hist_norm)
histnorm = histnorm.convert('RGB')
histnorm.save('alexhisteq.png')

plt.hist(img.ravel(),256,[0,256]); 
plt.savefig('histogram1.png')

plt.plot(cdf_normalized, color = 'b')
plt.plot(hist_norm, color = 'b')
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.savefig('histogrameq1.png')
