from base64 import b64decode
from io import BytesIO
import PIL.Image
import PIL.ExifTags

def get_image_b64(img_b64):
	
	image = PIL.Image.open(BytesIO(b64decode(img_b64)))

	# rotate image according to exif
	try:
	    for orientation in PIL.ExifTags.TAGS.keys():
	        if PIL.ExifTags.TAGS[orientation]=='Orientation':
	            break

	    exif=dict(image._getexif().items())

	    if exif[orientation] == 3:
	        image=image.rotate(180, expand=True)
	    elif exif[orientation] == 6:
	        image=image.rotate(270, expand=True)
	    elif exif[orientation] == 8:
	        image=image.rotate(90, expand=True)

	except (AttributeError, KeyError, IndexError):
	    # cases: image don't have getexif
	    pass
	
	return image