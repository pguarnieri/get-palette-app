import pandas as pd
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import colorsys

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
