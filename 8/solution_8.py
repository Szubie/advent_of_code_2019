
img = list(map(int, list(open('input.txt').read())[:-1]))

img_dims = (6, 25)
layer_stride = img_dims[0] * img_dims[1]

# Part 1
fewest_zeros = layer_stride
layer_calculation = None

for stop_index in range(layer_stride, len(img) + 1, layer_stride):
    start_index = stop_index - layer_stride
    print(start_index, stop_index)
    layer = img[start_index:stop_index]
    n_zeros = sum(map(lambda x: x == 0, layer))
    if n_zeros < fewest_zeros:
        fewest_zeros = n_zeros
        layer_calculation = sum(map(lambda x: x == 1, layer)) * sum(map(lambda x: x == 2, layer))

print(fewest_zeros)
print(layer_calculation)

# Part 2

BLACK = 0
WHITE = 1
TRANSPARENT = 2

def update_pixel(lower_layer_pixel, higher_layer_pixel):
    if higher_layer_pixel == TRANSPARENT:
        return lower_layer_pixel
    return higher_layer_pixel

visible_layer = img[len(img) - layer_stride:]

for stop_index in reversed(range(layer_stride, len(img) + 1, layer_stride)):
    start_index = stop_index - layer_stride
    print(stop_index - layer_stride,  stop_index)
    higher_layer = img[start_index:stop_index]
    print('Current visible layer', visible_layer)
    print('Higher layer', higher_layer)
    visible_layer = [update_pixel(lower_layer_pixel, higher_layer_pixel) 
                                         for lower_layer_pixel, higher_layer_pixel in zip(visible_layer, higher_layer)]
    print('New visible layer', visible_layer)

for end_index in range(img_dims[1], len(visible_layer) + 1, img_dims[1]):
    start_index = end_index - img_dims[1]
    print(''.join(['*' if pixel == WHITE else ' ' for pixel in visible_layer[start_index:end_index]]))

from matplotlib import pyplot as plt
import numpy as np

plt.figure()
plt.imshow(np.reshape(visible_layer, img_dims))
plt.show()

