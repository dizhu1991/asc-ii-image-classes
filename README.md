# asc-ii-image-classes
A class to handle some interesting asc II images.



## Setup

A virtual environment is necessary. Use `pip` to install dependencies:

``pip install -r requirements.txt``

## Initiate an image

Do the following:

``from image_processor import ImageProcessor
``
``image = ImageProcessor(url="your-url")``


To print the image:

``image.print()``

To crop the image, i.e. shrink the image down to the smallest rectangular area:

``image.crop()``

And then print it again.


