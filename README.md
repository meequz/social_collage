# social_collage

Small and straightforward library based on PIL to create image collages similar to those in social networks.

## Installation
```
pip install social_collage
```

## Usage
```
import social_collage

images = [list of pil images]
collage = social_collage.collage_5_1(images)
collage.save(path to save)
```
Here `social_collage.collage_5_1` is a function that makes the collage. It accepts collection of PIL images and returns a collage as another PIL image.

Currently available collage functions are: `collage_3_1`, `collage_4_1`, `collage_4_2`, `collage_5_1`.

Arguments, applicable to any collage function:

 - `images` - list of PIL image objects
 - `ratio=7/4` - required ratio of each image inside the collage. Default value is different for each function
 - `bgcolor=(255, 255, 255, 255)` - color of the background in RGBA format
 - `spaceshare=150` - share of the first image width to use as a space size. 0 or None means no space between images

## Full example
*replace path with your own, or use files from "package/example_images"*
```
import glob
from pathlib import Path

from PIL import Image

import social_collage


# Read image files into a list of PIL objects
imgs = []
for imgpath in sorted(glob.glob('your_image_folder/*.jpg')):
    imgs.append(Image.open(imgpath))


# Send list of PIL images to a collage function
collage = social_collage.collage_5_1(imgs)


# Show the returned PIL image containing the resulting collage
collage.show()

```
This example can also be launched with
```
import social_collage
social_collage.example()
```

## Results

### collage_3_1
![collage_3_1](https://github.com/meequz/social_collage/blob/main/readme_images/collage_3_1.jpg?raw=true)

### collage_4_1
![collage_4_1](https://github.com/meequz/social_collage/blob/main/readme_images/collage_4_1.jpg?raw=true)

### collage_4_2
![collage_4_2](https://github.com/meequz/social_collage/blob/main/readme_images/collage_4_2.jpg?raw=true)

### collage_5_1
![collage_5_1](https://github.com/meequz/social_collage/blob/main/readme_images/collage_5_1.jpg?raw=true)
