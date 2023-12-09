import numpy as np
import matplotlib.pyplot as plt

color_map = np.array([
    [1, 1, 1],  # Background (white)
    [0, 1, 0],  # No Damage (green)
    [0, 0, 1],  # Minor Damage (blue)
    [1, 0, 1],  # Major Damage (red-blue)
    [1, 0, 0],  # Destroyed (red)
    [0, 0, 0],  # Unclassified (black)
])


def display_image(image):
    image = image / 255.

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')

    plt.show()


def display_mask_overlay(image, mask):
    image = image / 255.

    color_mask = np.dot(mask, color_map)
    color_mask = np.clip(color_mask, 0, 1)

    alpha = 0.4
    overlay_image = (1 - alpha) * image + alpha * color_mask

    plt.figure(figsize=(10, 10))
    plt.imshow(overlay_image)
    plt.axis('off')

    plt.show()


def display_polygons_overlay(image, polygons, color='red'):
    image = image / 255.

    plt.figure(figsize=(10, 10))
    plt.imshow(image)

    for polygon in polygons:
        y, x = zip(*polygon)
        plt.plot(x, y, color=color)

    plt.axis('off')
    plt.show()
