# Home-Depot-Semantic-Segmentation

Computer vision project to perform semantic segmentation on a Home Depot video
using transfer learning for custom datasets in the small-data regime.

Team 1 Members:
- [Jose Mojica Perez](https://github.com/J-Mojica)
- [Mehakpreet Kaur](https://github.com/Mehakpreet21)

## Milestone 3: Annotation

We annotated our data using CVAT and DEXTR, a model for semi-automatic object segmentation.
By using DEXTR we speed up the annotation process for our custom dataset.

### Annotated Data
Our annotated data can be found in the [data directory.](./data) In this very same directory one can find a [text file](./data/classes.txt) 
with the class names of our custom dataset, as well as the [data-raw](./data/data-raw) directory which contains the data as it was downloaded
from the data acquisition stage of the project.

### Annotating images using CVAT

#### Creating a CVAT project
After booting up the CVAT docker containers, go to localhost:8080 and log in with the previously created admin account. Then, go to the project tab,
and click on the blue "plus" button on the top right corner of the page. A drop down menu will show, select "the Create a new project" option.
This will take you to a page, here you define the name of the project and then add all the labels as well as their corresponding colors. 
To add the labels one can use the constructor tab and add them one by one by giving them a name and selecting a color and attributes,
or one can use the raw tab and add all the labels in JSON format.

##### Single label JSON format example:
 ```
 [{
    "name": "toaster",
    "id": 10,
    "color": "#32b7fa",
    "type": "any",
    "attributes": []
  }
  ]
 ```

### Creating tasks
Once the project is created and all the labels are added, a task must be created to begin the annotation process. For this go to the "Tasks" tab and select
the blue "plus" button on the top right corner of the page, then select the "Create a new task" option on the drop down menu. Then, give the task a name,
select the project created before (this will automatically import the project's labels), and upload the files to be annotated. There's an option to select
which subset of the data set does this task belong to. However, due to the organization of our raw data we annotate everything as a single dataset and 
it's split later before training the model. Finally select either "Submit" button. You can find the newly created task, in the "Tasks" tab. Open it then,
click on the "Job" link and will take you to the annotation page for all the files uploaded for this task.


### Annotating images using DEXTR

#### Brief Definition of DEXTR
[Deep Extreme Cut (DEXTR)](https://cvlsegmentation.github.io/dextr/) is a computer vision deep learning model for semi-automatic object segmentation. The model is able to obtain an object segmentation from at least four of its boundary (“extreme”) points: left-most, right-most, top and bottom pixels (Maninis et al., 2018).

#### How DEXTR works
This model builds on the work of Papadopoulous et al.(2017) in which they use this same approach for generating bounding boxes around an object. In a nutshell, these four points are used to generate a heatmap around the object which is concatenated with the RGB channels of the input image, creating a four-dimensional input for a Convolutional Neural Network (CNN). These points are also used to generate a bounding box around the object of interest, then this bounding box is relaxed by several pixels to include some context around the object. And finally the image is cropped to just include this region of interest, which includes the object, some context plus its extreme points, as the input for the CNN.  The output of this CNN is “a probability map representing whether a pixel belongs to the object that we want to segment or not. The CNN is trained to minimize the standard cross entropy loss, which takes into account that different classes occur with different frequency in a dataset” (Maninis et al., 2018). In this way, the model is able to obtain fairly accurate object segmentation which can be further refined by providing more extreme points.

#### Applications

DEXTR can be used to obtain dense annotations to train supervised techniques and we have used this application in this milestone for our data of kitchen objects (Dishwasher, blender, toasters etc). As explained by Maninis et al., “in this framework, instead of detailed polygon labels, the workload of the annotator is reduced to only providing the extreme points of an object” (2018), greatly reducing the amount of time needed to to label a data set. Algorithms that are trained using the annotations that are produced by DEXTR perform just as well as those that are trained using the ground truth ones. Training with DEXTR is much more efficient than training from the ground truth for a given target quality when the cost of obtaining such annotations is taken into account. (Maninis et al., 2018)

#### Experimental observations

Following are some of the experimental observations obtained by Maninis et al. available in their 2018 publication:

Different experiments done based on processing full or cropped images also showed that focusing on the objects of interest instead of processing the whole image increased the performance by 7.9% since there are less additional variations in the input in that case. 

Another such experiment on DEXTR focused on the variations in the output between extreme points supplied by humans and those that [Deep Extreme Cut: From Extreme Points to Object Segmentation](https://arxiv.org/pdf/1711.09081.pdf) modeled, to see if the conclusions we make from the simulations would still hold true in a real-world application with human annotators. 
Similarly, many such variations of possibilities have been considered in the use of DEXTR, a CNN architecture that converts extreme clicking annotations into precise object masks for semi-automatic segmentation, in order to absolve the possible parameters that make it a better model. 

#### Citations
D. P. Papadopoulos, J. R. Uijlings, F. Keller, and V. Ferrari. Extreme clicking for efficient object annotation. In ICCV, 2017

Maninis, K.-K. et al. (2018) “Deep Extreme Cut: From extreme points to object segmentation,” 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition [Preprint]. Available at: https://doi.org/10.1109/cvpr.2018.00071.
