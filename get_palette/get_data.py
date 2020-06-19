from base64 import b64decode
from io import BytesIO
from PIL import Image

def get_image_b64(self, img_b64):

	img = Image.open(BytesIO(b64decode(img_b64)))

	return img