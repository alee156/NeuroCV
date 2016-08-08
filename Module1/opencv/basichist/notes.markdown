## Notes for basic histogram 

### What is a histogram?

- Graph or plot describing image's intensity distribution 
   - X axis: pixel value (dark to light)
   - Y axis: number of pixels
-   Can extract information about contrast, brightness, intensity, etc.

### Key definitions

- *BINS*
   - Each bin is a range of pixel values
   - When representing the total number of pixel values (0 - 255) means there are 256 bins
   - 16 or 32 are the most frequent bin numbers
   - Represented by term histSize in OpenCV

- *DIMS* 
   - Number of parameters used for data collection

- *RANGE* 
   - Range of intensity values
   - Usually [0,256] to represent all values


