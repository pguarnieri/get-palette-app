#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

#%%
from PIL import Image

img = Image.open('madmax.jpg')

#%% resize for speed
basewidth = 100
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)

#%% get channels
arr = np.array(img)

r = arr[:,:,0].flatten()
g = arr[:,:,1].flatten()
b = arr[:,:,2].flatten()

df = pd.DataFrame({'r' : list(r), 'g' : list(g), 'b' : list(b)})

#%%
kmeans = KMeans(n_clusters=10).fit(df)

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

