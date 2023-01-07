# Home-Depot-Semantic-Segmentation
Computer vision project to perform semantic segmentation on a Home Depot video
using transfer learning for custom datasets in the small-data regime.

Team 1 Members:
- [Jose Mojica Perez](https://github.com/J-Mojica)
- [Mehakpreet Kaur](https://github.com/Mehakpreet21)


# Demo
Segmentation of a 30 second clip:

![Demo GIF of semantic segmentation on a 30 second clip of a Home Depot video](./media/segmentation_demo.gif)

[demoGIF]: https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/tree/main/media/segmentation_demo.gif "demo GIF"

## Milestone 1: CVAT set up and installation

Computer Vision Annotation Tool (CVAT) is an open source
annotation tool used for labeling data for computer vision 
algorithms. This is the tool we will use to annotate
a custom data set of 10 classes of kitchen items.

### CVAT Installation Instructions Followed

- Install WSL2 (Windows subsystem for Linux) refer to [this official guide][WSL2-Guide] 
WSL2 requires Windows 10, version 2004 or higher. Note: You may not have to install a Linux distribution unless needed.

- Download and install [Docker Desktop for Windows][Docker-Download] Double-click `Docker for Windows Installer` 
to run the installer. Note: Check that you are specifically using WSL2 backend for Docker.

- Download and install [Git for Windows][Git-Download]. When installing the package please keep all options 
by default. More information about the package can be found here.

- Download and install [Google Chrome][Chrome-Download]. It is the only browser which is supported by CVAT.

- Go to windows menu, find Git Bash application and run it. You should see a terminal window.

- Clone CVAT source code from the GitHub repository.

The following command will clone the latest develop branch:

```
git clone https://github.com/opencv/cvat
cd cvat
```

Run docker containers. It will take some time to download the latest CVAT release and other 
required images like postgres, redis, etc. from DockerHub and create containers.

```
docker-compose up -d
```

You can register a user but by default it will not have rights even to view list of tasks. 
Thus you should create a superuser. A superuser can use an admin panel to assign correct 
groups to other users. Please use the command below:

```
winpty docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

Choose a username and a password for your admin account. For more information please read Django documentation.

Open the installed Google Chrome browser and go to localhost:8080.

![Screenshot of CVAT's Log-in Page][CVAT-LogIn-Screenshot]

[WSL2-Guide]: https://docs.microsoft.com/windows/wsl/install-win10
[Docker-Download]: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module
[Git-Download]: https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe
[Chrome-Download]: https://www.google.com/chrome/
[CVAT-LogIn-Screenshot]: https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/blob/milestone-1/media/CVAT-LogIn-Screenshot.png "CVAT LogIn Page Screenshot"

## Milestone 2: Data Acquisition

### Image Scapping using Google Custom Search API
#### Steps used:

- Create a new project in [Google API cloud console](https://console.cloud.google.com/apis/dashboard)

- In this new project, enable the Custom Search API.

- Go to the credentials tab on the dashboard and acquire an API key for the Custom Search API

- Go to the [Programmable Search Engine Control Panel](https://programmablesearchengine.google.com/controlpanel/all) and add a new 
custom search engine, making sure to enable image search. Then get the Search Engine's ID in it's overview page after adding it.
  
- Create the functions for a [web scraper](image_scraper.py) which uses the Google API Python Client to access a Custom Search Engine resource
 to obtain the URLs of images and downloads them.

- Created a [driver program](scrape.py) for the [web scraper](image_scraper.py) functions to get the URLs of 200 images
and download them. We acquired double of what's necessary in case some of the URLs do not work or the images are repeated 
instances of others already in the set. Manual clean up will be done at a later stage and the image set will be restricted 
to only 100 images per category. 

- Saved the URLs into a file called "urls.txt" for each category and downloaded the images from those urls. Each
category has its own separate directory and are saved with the name of its respective category followed by a sequential number
for easy identification.

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


## Milestone 4: Semantic segmentation
To perform semantic segmentation on our custom dataset, 
we used the [Detectron2](https://github.com/facebookresearch/detectron2) 
framework. We used a model pretrained on the MS COCO dataset implemented within Detectron2.
The model used for the segmentation is a model similar to This is similar to the setting used in the
[Mask R-CNN paper](https://doi.org/10.48550/arXiv.1703.06870), Appendix A, with some modifications

The training and segmentation was done using google colab with a GPU runtime.

To select our hyperparamenters (mainly the number of iterations), the model
was first trained on 1000 iterations, and then the loss curves evaluated
using tensorboard. On this evaluation we determined that the model
performed best with about 600 iterations. Then the model was reinitialized
and trained for this amount of iterations.

The process can be seen in the [segmentation notebook](https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/blob/main/segmentation/segmentation.ipynb)

The trained model can be found [here](https://drive.google.com/file/d/1AHVd4HRVh_P3p6OVek-bZHMLobTmaBpb/view?usp=share_link)

The file for our 30-second demo can be found [here](./media/segmentation_demo.gif)
