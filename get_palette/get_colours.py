import pandas as pd
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import colorsys
from base64 import b64decode
from io import BytesIO

def make_image_df(self, img):

	# resize image to keep size relatively small and keep calculations running quickly
	basewidth = 100
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)

	# get channels and turn colours into dataframe columns
	arr = np.array(img.convert('RGB')) # need .convert('RGB') as sometimes png may not be loaded as such

	r = arr[:,:,0].flatten()
	g = arr[:,:,1].flatten()
	b = arr[:,:,2].flatten()

	df = pd.DataFrame({'r' : list(r), 'g' : list(g), 'b' : list(b)})

	return df

def prettify_colours(self, centroids):

	# for a more visually appealing palette, let's order the colours by hue
	colours = []
	for row in range(len(centroids)):

	    c = list(centroids[row,:]/255)

	    colours.append(list(colorsys.rgb_to_hsv(*c)))
	    
	colours.sort()

	colours = [list(colorsys.hsv_to_rgb(*c)) for c in colours]

	return colours


def kmeans(self, img, n_colours=10):

	df = make_image_df(img)

	# pick how many colours will populate our palette, then perform a KMeans, and finally get the centroids identifying the colours we will display
	n_clusters = n_colours

	kmeans = KMeans(n_clusters=n_clusters).fit(df)

	centroids = kmeans.cluster_centers_

	colours = prettify_colours(centroids)

	return colours



def create_palette_image(self, img, colours)

	n_clusters = len(colours)

	# Let's create a new image that will work as a canvas to display input image and palette
	full_w = 1000
	full_h = 1000

	new_img = Image.new('RGBA', (full_w, full_h), "white")

	#
	frame_s = round(full_w / 60)

	intrabox_w = round(full_w / 100)

	box_w = round((full_w - ((frame_s*2) + (intrabox_w*(n_clusters-1)))) / n_clusters)
	box_h = round(full_h / 4)

	x = frame_s
	for col in colours:

	    col_box = Image.new('RGBA', (box_w, box_h), tuple(np.round(np.array(col)*255).astype(int)))

	    new_img.paste(col_box, (x, full_h-frame_s-box_h))

	    x = x + box_w + intrabox_w

	#
	basewidth = round(full_w - (frame_s*2))
	baseheight = round(full_h - (frame_s + box_h) - (full_h/10*2))

	# adjust height to fit box
	wpercent = (baseheight / float(img_orig.size[1]))
	wsize = int((float(img_orig.size[0]) * float(wpercent)))
	img_orig = img_orig.resize((wsize, baseheight), Image.ANTIALIAS)

	# if width still not fitting, also adjust that
	if img_orig.size[0] > basewidth:
	    wpercent = (basewidth / float(img_orig.size[0]))
	    hsize = int((float(img_orig.size[1]) * float(wpercent)))
	    img_orig = img_orig.resize((basewidth, hsize), Image.ANTIALIAS)

	#
	wsize = img_orig.size[0]
	hsize = img_orig.size[1]

	pos_x = frame_s + round((basewidth-wsize)/2)
	pos_y = round(full_h/10) + round((baseheight-hsize)/2)

	coords = (pos_x, pos_y)

	new_img.paste(img_orig, coords)

	return new_img


def image2b64(self, img):

	buffered = BytesIO()
	new_img.save(buffered, format="PNG")
	img_str = b64encode(buffered.getvalue()).decode('utf-8')

	return img_str
	




