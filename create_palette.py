#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

#%%
from PIL import Image

filename = 'bFC.png'

img = Image.open(filename)

img_orig = img.copy()

#%% resize for speed
basewidth = 100
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)

#%% get channels
arr = np.array(img.convert('RGB')) # need .convert('RGB') as sometimes png may not be loaded as such

r = arr[:,:,0].flatten()
g = arr[:,:,1].flatten()
b = arr[:,:,2].flatten()

df = pd.DataFrame({'r' : list(r), 'g' : list(g), 'b' : list(b)})

#%%
n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters).fit(df)

centroids = kmeans.cluster_centers_

#%%
import matplotlib.pyplot as plt

plt.imshow([centroids/255])


# %% order by hue
import colorsys

colours = []
for row in range(len(centroids)):

    c = list(centroids[row,:]/255)

    colours.append(list(colorsys.rgb_to_hsv(*c)))

#%%
colours.sort()

colours = [list(colorsys.hsv_to_rgb(*c)) for c in colours]

plt.imshow([np.array(colours)])

# %%
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

full_w = 1000
full_h = 1000

new_img = Image.new('RGBA', (full_w, full_h), "white")

# %%
frame_s = round(full_w / 60)

intrabox_w = round(full_w / 100)

box_w = round((full_w - ((frame_s*2) + (intrabox_w*(n_clusters-1)))) / n_clusters)
box_h = round(full_h / 4)

x = frame_s
for col in colours:

    col_box = Image.new('RGBA', (box_w, box_h), tuple(np.round(np.array(col)*255).astype(int)))

    new_img.paste(col_box, (x, full_h-frame_s-box_h))

    x = x + box_w + intrabox_w

#%%
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

#%% 
wsize = img_orig.size[0]
hsize = img_orig.size[1]

pos_x = frame_s + round((basewidth-wsize)/2)
pos_y = round(full_h/10) + round((baseheight-hsize)/2)

coords = (pos_x, pos_y)

new_img.paste(img_orig, coords)

# %%
#plt.imshow(new_img)
new_img.save("output_"+filename, "PNG")

# %%
