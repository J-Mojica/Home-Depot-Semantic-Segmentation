## Milestone 4
To perform the segmentation, we used the [Detectron2](https://github.com/facebookresearch/detectron2)
We used a model pretrained on the MS COCO dataset implemented within the Detectron2 framework.
The model used for the segmentation is a model similar to This is similar to the setting used in the
[Mask R-CNN paper](https://doi.org/10.48550/arXiv.1703.06870), Appendix A, with some modifications

The training and segmentation was done using google colab with a GPU runtime.

To select our hyperparamenters (mainly the number of iterations), the model
was first trained on 1000 iterations, and then the loss curves evaluated
using tensorboard. On this evaluation we determined that the model
performed best with about 600 iterations. Then the model was reinitialized
and trained for this amount of iterations.

The process can be seen in the [segmentation notebook](https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/tree/segmentation/segmentation.ipynb)

In the [segmentation directory](https://github.com/J-Mojica/Home-Depot-Semantic-Segmentation/tree/segmentation/) one can find the trained model and our attempt at segmenting a 30 second clip of a Home Depot video.