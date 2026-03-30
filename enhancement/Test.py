from skimage import io
import matplotlib.pyplot as plt
from enhance import enhance_image
from skimage import img_as_ubyte

image = io.imread(r'../Images/input/Noisy_image_2.png')

denoised, sharpened, final = enhance_image(image)

fig, axes = plt.subplots(1, 4, figsize=(15,5))

axes[0].imshow(image)
axes[0].set_title("Original")

axes[1].imshow(denoised)
axes[1].set_title("Denoised")

axes[2].imshow(sharpened)
axes[2].set_title("Sharpened")

axes[3].imshow(final)
axes[3].set_title("Final")

for ax in axes:
    ax.axis('off')
    
io.imsave(r'..\Images\output\denoised.png', img_as_ubyte(denoised))
io.imsave(r'..\Images\output\sharpened.png', img_as_ubyte(sharpened))
io.imsave(r'..\Images\output\final.png', img_as_ubyte(final))
plt.show()