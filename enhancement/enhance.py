from skimage import filters, exposure, restoration, color

def enhance_image(image):

    denoised = restoration.denoise_bilateral(image, channel_axis=-1)
    sharpened = filters.unsharp_mask(denoised, radius=1, amount=0.8)
    hsv = color.rgb2hsv(sharpened)
    hsv[:, :, 2] = exposure.equalize_adapthist(hsv[:, :, 2])
    final = color.hsv2rgb(hsv)

    return denoised, sharpened, final