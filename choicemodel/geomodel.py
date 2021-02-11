import geopandas as gpd
import matplotlib.pyplot as plt
import os
import pandas as pd

from .constants import GEO_ID_TO_COOR
from pathlib import Path
from shapely.geometry import Point


class GeoModel:

    def __init__(self,
                 shapefile_path='/data/tn/tl_2016_47_cousub.shp',
                 tn_data_path='/data/tn_data.csv',
                 geomap_model_path='/data/geomap_model.csv'):
        self.shapefile_path = str(Path(os.path.dirname(__file__)).parent) + shapefile_path
        self.tn_data_path = str(Path(os.path.dirname(__file__)).parent) + tn_data_path
        self.geomap_model_path = str(Path(os.path.dirname(__file__)).parent) + geomap_model_path

    def create_csv_model(self):
        """
        Makes all the conversions and transformations necessary to display the information
        on the geo plot. Final output is in csv file format

        - value assigned to each block group is through this calculation:
            - # of households in each block group x probability of switching
        """
        # read data into following dataframe format: (this will be used later to make plot)
        #
        #                name         lat     lon     # households     % prob switching     block group
        # 47165-blah   top tier       36      -84          x                 .05               geo_id
        #     .            .          .        .           .                  .                  .
        #     .            .          .        .           .                  .                  .
        #     .            .          .        .           .                  .                  .
        # 47231-blah   professional   36      -84          x                 .05               geo_id

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

        # create GeoDataFrame
        gdf = gpd.GeoDataFrame(
            df, geometry=gpd.points_from_xy(df.longitude, df.latitude)
        )

        # import shapefile to check for overlapping block groups
        tn = gpd.read_file(self.shapefile_path)

        # check for overlapping block groups
        gdf['GEOID'] = gdf.apply(self.search_block_group, args=(tn,), axis=1)
        df = pd.DataFrame(gdf)
        df.to_csv('geomap_model.csv')

    @staticmethod
    def search_block_group(geo_id_row, shapefile):
        for index, row in shapefile.iterrows():
            if row['geometry'].contains(Point(
                geo_id_row['longitude'], geo_id_row['latitude']
            )):
                return row['GEOID']

    def show_map(self):
        # import TN shapefile and convert GEOID column to numeric data type
        tn = gpd.read_file(self.shapefile_path, names=['GEOID', 'geometry'])
        tn['GEOID'] = pd.to_numeric(tn['GEOID'])

        # remove unused columns
        unused_geo_attributes = list(tn.columns)
        unused_geo_attributes.remove('GEOID')
        unused_geo_attributes.remove('geometry')
        tn = tn.drop(columns=unused_geo_attributes)

        # import geomap model
        geo_model = pd.read_csv(self.geomap_model_path)
        geo_model = geo_model.drop(['geometry'], axis=1)

        # merge datasets
        for_plotting = tn.merge(geo_model, left_on='GEOID', right_on='GEOID')

        # plot
        fig, ax = plt.subplots(1, figsize=(14, 6))
        fig.canvas.set_window_title('Market Segments Visualized')
        ax.set_title('Market Segments Visualized')

        for_plotting.plot(column='households', cmap='Reds', linewidth=1, ax=ax, edgecolor='0.6',
                          legend=True, legend_kwds={'loc': 'lower right'},
                          scheme='quantiles')
        plt.show()
