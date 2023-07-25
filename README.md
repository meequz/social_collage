# social_collage

Small and straightforward library based on PIL to create image collages similar to those in social networks.

## Usage
```
import social_collage

images = [...]
collage = social_collage.collage_5_1(images)
collage.save(...)
```
Currently available functions are: `collage_3_1`, `collage_4_1`, `collage_4_2`, `collage_5_1`.

Arguments, applicable to any collage function:

 - `images` - list of PIL objects
 - `ratio=7/4` - required ratio of each image inside the collage. Default value is different for each function
 - `bgcolor=(255, 255, 255, 255)` - color of the background in RGBA format
 - `spaceshare=150` - share of the first image width to use as a space size. 0 or None means no space

## Example
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


### collage_4_1


### collage_4_2


### collage_5_1

