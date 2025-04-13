from PIL import Image, ImageEnhance, ImageFilter

def apply_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def apply_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_black_and_white(image):
    return image.convert("L")

def apply_sharpen(image):
    return image.filter(ImageFilter.SHARPEN)
