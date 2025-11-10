import cv2
import numpy as np
import os
from tensorflow.keras.utils import Sequence




class SegmentationDataset(Sequence):
def __init__(self, image_paths, mask_paths, batch_size=8, img_size=(256, 256)):
self.image_paths = image_paths
self.mask_paths = mask_paths
self.batch_size = batch_size
self.img_size = img_size


def __len__(self):
return len(self.image_paths) // self.batch_size


def __getitem__(self, idx):
batch_x = self.image_paths[idx*self.batch_size:(idx+1)*self.batch_size]
batch_y = self.mask_paths[idx*self.batch_size:(idx+1)*self.batch_size]


images = []
masks = []


for img_path, mask_path in zip(batch_x, batch_y):
img = cv2.imread(img_path)
img = cv2.resize(img, self.img_size)
img = img / 255.0


mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, self.img_size)
mask = mask / 255.0
mask = np.expand_dims(mask, axis=-1)


images.append(img)
masks.append(mask)


return np.array(images), np.array(masks)