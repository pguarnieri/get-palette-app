from base64 import b64decode
from io import BytesIO
import PIL.Image

def get_image_b64(img_b64):
	
	img = PIL.Image.open(BytesIO(b64decode(img_b64)))
	
	return img