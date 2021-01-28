import geopandas as gpd
import geoplot as g_plt
import matplotlib.pyplot as plt
import os
import pandas as pd

from .constants import GEO_ID_TO_COOR
from pathlib import Path


class GeoModel:

    def __init__(self,
                 shapefile_path='/data/tn/tl_2016_47_cousub.shp',
                 tn_data_path='/data/tn_data.csv',
                 conversion_path='/data/convert.csv'):
        self.shapefile_path = str(Path(os.path.dirname(__file__)).parent) + shapefile_path
        self.tn_data_path = str(Path(os.path.dirname(__file__)).parent) + tn_data_path
        self.conversion_path = str(Path(os.path.dirname(__file__)).parent) + conversion_path

    def create_model(self):
        """
        Makes all the conversions and transformations necessary to display the information
        on the geo plot

        - value assigned to each block group is through this calculation:
            - # of households in each block group x probability of switching
        """
        # read data into following dataframe format: (this will be used later to make plot)
        #
        #                name         lat     lon     # households     % prob switching
        # 47165-blah   top tier       36      -84          x                 .05
        #     .            .          .        .           .                  .
        #     .            .          .        .           .                  .
        #     .            .          .        .           .                  .
        # 47231-blah   professional   36      -84          x                 .05

        # read in file and set block group geo_id as index
        df = pd.read_csv(self.tn_data_path, index_col=0)

        # create column with number of households
        df['households'] = df[:].max(axis=1)

        # create column with name where households are located. if no households, None is placed
        df['name'] = df.apply(lambda x: x.idxmax() if sum(x) != 0 else None,
                              axis=1)

        # remove columns with the group block names, as these are no longer needed
        df.drop(df.columns[:-2], axis=1, inplace=True)

        # add latitude value
        df['latitude'] = df.apply(lambda x: GEO_ID_TO_COOR[str(x.name)][0], axis=1)

        # add longitude value
        df['longitude'] = df.apply(lambda x: GEO_ID_TO_COOR[str(x.name)][1], axis=1)

    def show_map(self):
        tn = gpd.read_file(self.shapefile_path)
        tn.plot()
        plt.show()
