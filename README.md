# Home-Depot-Semantic-Segmentation
Team 1 Members:
- [Jose Mojica Perez](https://github.com/J-Mojica)
- [Mehakpreet Kaur](https://github.com/Mehakpreet21)

## Milestone 3
## DEXTR and How it works

### Brief Definition 
[Deep Extreme Cut (DEXTR)] (https://cvlsegmentation.github.io/dextr/) is a computer vision deep learning model for semi-automatic object segmentation. The model is able to obtain an object segmentation from at least four of its boundary (“extreme”) points: left-most, right-most, top and bottom pixels (Maninis et al., 2018).

### How it works
This model builds on the work of Papadopoulous et al.(2017) in which they use this same approach for generating bounding boxes around an object. In a nutshell, these four points are used to generate a heatmap around the object which is concatenated with the RGB channels of the input image, creating a four-dimensional input for a Convolutional Neural Network (CNN). These points are also used to generate a bounding box around the object of interest, then this bounding box is relaxed by several pixels to include some context around the object. And finally the image is cropped to just include this region of interest, which includes the object, some context plus its extreme points, as the input for the CNN.  The output of this CNN is “a probability map representing whether a pixel belongs to the object that we want to segment or not. The CNN is trained to minimize the standard cross entropy loss, which takes into account that different classes occur with different frequency in a dataset” (Maninis et al., 2018). In this way, the model is able to obtain fairly accurate object segmentation which can be further refined by providing more extreme points.

#### Applications

DEXTR can be used to obtain dense annotations to train supervised techniques and we have used this application in this milestone for our data of kitchen objects (Dishwasher, blender, toasters etc). As explained by Maninis et al., “in this framework, instead of detailed polygon labels, the workload of the annotator is reduced to only providing the extreme points of an object” (2018), greatly reducing the amount of time needed to to label a data set. Algorithms that are trained using the annotations that are produced by DEXTR perform just as well as those that are trained using the ground truth ones. Training with DEXTR is much more efficient than training from the ground truth for a given target quality when the cost of obtaining such annotations is taken into account. (Maninis et al., 2018)

#### Experimental observations

Following are some of the experimental observations obtained by Maninis et al. available in their 2018 publication:

Different experiments done based on processing full or cropped images also showed that focusing on the objects of interest instead of processing the whole image increased the performance by 7.9% since there are less additional variations in the input in that case. 

Another such experiment on DEXTR focused on the variations in the output between extreme points supplied by humans and those that [Deep Extreme Cut: From Extreme Points to Object Segmentation](https://arxiv.org/pdf/1711.09081.pdf) modeled, to see if the conclusions we make from the simulations would still hold true in a real-world application with human annotators. 
Similarly, many such variations of possibilities have been considered in the use of DEXTR, a CNN architecture that converts extreme clicking annotations into precise object masks for semi-automatic segmentation, in order to absolve the possible parameters that make it a better model. 

### Citations
D. P. Papadopoulos, J. R. Uijlings, F. Keller, and V. Ferrari. Extreme clicking for efficient object annotation. In ICCV, 2017

Maninis, K.-K. et al. (2018) “Deep Extreme Cut: From extreme points to object segmentation,” 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition [Preprint]. Available at: https://doi.org/10.1109/cvpr.2018.00071.


