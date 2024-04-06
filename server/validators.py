from PIL import Image
from rest_framework.exceptions import ValidationError
import os


def validate_icon_image(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError("The maximum allowed dimensions for the image is 70*70")


def validate_image_file_extensions(value):
    ext = os.path.splitext(value.name[1])
    valid_extensions = ['.jpg', ".jpeg", ".png"]
    if ext not in valid_extensions:
        raise ValidationError("Unsupported file extensions")
