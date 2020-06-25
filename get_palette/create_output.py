import numpy as np
import PIL.Image
from base64 import b64encode
from io import BytesIO

def create_palette_image(img, colours):

	n_clusters = len(colours)

	# Let's create a new image that will work as a canvas to display input image and palette
	full_w = 1000
	full_h = 1000

	new_img = PIL.Image.new('RGBA', (full_w, full_h), "white")

	#
	frame_s = round(full_w / 60)

	intrabox_w = round(full_w / 100)

	box_w = round((full_w - ((frame_s*2) + (intrabox_w*(n_clusters-1)))) / n_clusters)
	box_h = round(full_h / 4)

	x = frame_s
	for col in colours:

	    col_box = PIL.Image.new('RGBA', (box_w, box_h), tuple(np.round(np.array(col)*255).astype(int)))

	    new_img.paste(col_box, (x, full_h-frame_s-box_h))

	    x = x + box_w + intrabox_w

	#
	basewidth = round(full_w - (frame_s*2))
	baseheight = round(full_h - (frame_s + box_h) - (full_h/10*2))

	# adjust height to fit box
	wpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(wpercent)))
	img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

	# if width still not fitting, also adjust that
	if img.size[0] > basewidth:
	    wpercent = (basewidth / float(img.size[0]))
	    hsize = int((float(img.size[1]) * float(wpercent)))
	    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

	#
	wsize = img.size[0]
	hsize = img.size[1]

	pos_x = frame_s + round((basewidth-wsize)/2)
	pos_y = round(full_h/10) + round((baseheight-hsize)/2)

	coords = (pos_x, pos_y)

	new_img.paste(img, coords)

	return new_img


def image2b64(img):

	buffered = BytesIO()
	img.save(buffered, format="PNG")
	img_str = b64encode(buffered.getvalue()).decode('utf-8')

	return img_str