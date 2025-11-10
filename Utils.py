import matplotlib.pyplot as plt
import numpy as np




def plot_sample(image, mask, prediction=None):
plt.figure(figsize=(12, 4))


plt.subplot(1, 3, 1)
plt.title("Image")
plt.imshow(image)
plt.axis('off')


plt.subplot(1, 3, 2)
plt.title("Mask")
plt.imshow(mask, cmap='gray')
plt.axis('off')


if prediction is not None:
plt.subplot(1, 3, 3)
plt.title("Prediction")
plt.imshow(prediction, cmap='gray')
plt.axis('off')


plt.show()




def visualize_training(history):
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.title('Training History')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()