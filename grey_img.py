import numpy as np
from PIL import Image

ima_ge=Image.open("color2.webp")

color_img=np.array(ima_ge)   

if len(color_img.shape)==2:
    print("Image is greyscale alerady")
    grey_scale=color_img
else:
    grey_scale = 0.2989 * color_img[:, :, 0] + \
       0.5870 * color_img[:, :, 1] + \
       0.1140 * color_img[:, :, 2]
    grey=grey_scale.astype(np.uint8)
    file_name="grey.jpg"

    Image.fromarray(grey).save(file_name)
    print("Image converted & saved")