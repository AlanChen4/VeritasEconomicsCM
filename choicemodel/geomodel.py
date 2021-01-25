import geopandas as gpd
import geoplot as g_plt
import matplotlib.pyplot as plt
import pandas as pd

tn = gpd.read_file('../data/tn/tl_2016_47_cousub.shp')
tn.plot()
plt.show()
