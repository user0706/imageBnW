# About

This is a simple image processing code that filters it so it's black and white.
Pillow (PIL) module was used to open the image, while the Numpy module was used to manipulate image data.

### How it works

Expressing the image through Numpy array, the image is ready for software manipulation. The whole picture can be presented as a lists in the list in the list.

![](https://github.com/user0706/imageBnW/blob/master/ignore/listsOfImage.png)

The idea of converting an image to black and white is extremely simple. 

The balance, or the mean value of each pixel, is searched and placed in a temporary list. In this way it is possible to find the mean value (balance) of the whole picture. Then, if the individual pixel balance is above the entire image balance, that current pixel is set to black [255 255 255 255]. Otherwise, the current pixel is set to white [0 0 0 255].

### Mathematics behind

The most used and most needed mathematical form is the search for mean values.

The *arithmetic mean* (or simply *mean*) of a sample ![](https://github.com/user0706/imageBnW/blob/master/ignore/fromXtoN.svg), usually denoted by ![](https://github.com/user0706/imageBnW/blob/master/ignore/x.svg), is the sum of the sampled values divided by the number of items in the example.

![](https://github.com/user0706/imageBnW/blob/master/ignore/meanValueForm.svg)

