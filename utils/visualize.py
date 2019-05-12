from matplotlib import pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np



def plot_images(dataset, n_images=3):
    '''
    plots random samples of the dataset with corresponding bounding boxes
    '''
    for rnd in np.random.randint(0,len(dataset.image_info)-1,n_images):

        img = dataset.load_image(rnd)

        bboxes,_ = dataset.load_bbox(rnd)
        labels = list([box['class'] for box in dataset.image_info[rnd]["bboxes"]])

        fig,ax = plt.subplots()
        plt.grid()
        plt.imshow(img)

        for box,label in zip(bboxes,labels):
            y1, x1, y2, x2 = box
            p = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2,
                                  alpha=0.7, linestyle="dashed",
                                  edgecolor="red", facecolor='none')
            ax.add_patch(p)
            plt.text(x1,y1,label, fontsize=15, color="red")

        plt.show()