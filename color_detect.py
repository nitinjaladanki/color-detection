import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
import cv2

#PUT THE NAME OF YOUR IMAGE HERE
img_rgb = cv2.imread("message_Nitin.jpeg")

# img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV )
img_hsv = img_rgb

#making the figure to animate
#it has three plots for each of the channels of hsv
fig, ax = plt.subplots(1,4, figsize=(12,2))

#add colorbars to each of the subplots
fig.colorbar(cm.ScalarMappable(cmap="hsv"), shrink=0.4, ax=ax[0])
fig.colorbar(cm.ScalarMappable(cmap="hsv"), shrink=0.4, ax=ax[1])
fig.colorbar(cm.ScalarMappable(cmap="hsv"), shrink=0.4, ax=ax[2])

#add the original image
ax[3].imshow(img_rgb)
ax[3].set_title("Original Image")

def update_plot(frame_i: int, axis: int, color_channel: int, image, title: str) -> None:
    
    filt = cv2.boxFilter(image[:,:,color_channel], cv2.CV_32F, (frame_i+1, frame_i+1))
    ax[axis].clear()
    ax[axis].set_title(title + str(frame_i+1))
    ax[axis].imshow(filt, cmap="hsv")

def animate(i: int):
    update_plot(i, 0, 0, img_hsv, "Hue filter size: ")
    update_plot(i, 1, 1, img_hsv, "Saturation filter size: ")
    update_plot(i, 2, 2, img_hsv, "Value filter size: ")

if __name__ == "__main__":
    ani = FuncAnimation(fig, animate, frames=100, interval=300)
    plt.show()