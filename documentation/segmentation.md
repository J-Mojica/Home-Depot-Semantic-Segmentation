# Home-Depot-Semantic-Segmentation

Computer vision project to perform semantic segmentation on a Home Depot video
using transfer learning for custom datasets in the small-data regime.

Team 1 Members:
- [Jose Mojica Perez](https://github.com/J-Mojica)
- [Mehakpreet Kaur](https://github.com/Mehakpreet21)

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

Better results should be possible with a more rigorous hyperparameter optimization scheme, such
as a grid search over various values for maximum number of iterations and learning rate.
Another way results could be improved is by gathering more data, and curating the images to be 
mostly similar to the type of images the model will encounter on the video. With the current
dataset, one could also perform data augmentation to try and remedy the small amount of data.

The process of preparing the data, training and evaluating the model, and performing semantic segmentation
can be seen in the [segmentation notebook](https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/blob/main/src/segmentation/segmentation.ipynb)

The trained model can be found [here](https://drive.google.com/file/d/1AHVd4HRVh_P3p6OVek-bZHMLobTmaBpb/view?usp=share_link)

The file for our 30-second demo can be found [here](./media/segmentation_demo.gif)