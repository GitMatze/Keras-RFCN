from matplotlib import pyplot as plt
import cv2
import numpy as np


def plot_images(dataset, n_images=3):
    '''
    plots random samples of the dataset with corresponding bounding boxes
    '''
    for rnd in np.random.randint(0,len(dataset.image_info)-1,n_images):

        img = dataset.load_image(rnd)


        #path = dataset.image_info[rnd]["path"]
        bboxes = dataset.image_info[rnd]["bboxes"]

        #img = cv2.imread(path)



        for row in bboxes:
            xmin = row['x1']
            xmax = row['x2']
            ymin = row['y1']
            ymax = row['y2']
            category = row['class']

            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (50,50,250), 6)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, category, (xmin, ymin-10), font, 1, (50,50,250), 3)



        plt.figure()
        plt.grid()
        plt.imshow(img)
        plt.show()