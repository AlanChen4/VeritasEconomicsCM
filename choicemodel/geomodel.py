import geopandas as gpd
import mapclassify
import matplotlib.pyplot as plt
import os
import pandas as pd

from .constants import GEO_ID_TO_COOR
from pathlib import Path
from shapely.geometry import Point


def household_after_prob_rate(row, prob_a, prob_b):
    """
    Multiply and return the household count after considering probability for switchover
    :param row: row containing data (name, households)
    :param prob_a: switch over rates under plan A
    :param prob_b: switch over rates under plan B
    :return: household count
    """
    try:
        return row['households'] * (prob_a.loc[row['name']]['plan 1 rate'] + prob_b.loc[row['name']]['plan 2 rate'])
    # this occurs when a row is passed without a name
    except KeyError:
        pass


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
        gdf['GEOID'] = gdf.apply(self.search_block_group, shapefile=tn, axis=1)
        df = pd.DataFrame(gdf)
        df.to_csv('geomap_model.csv')

    @staticmethod
    def search_block_group(geo_id_row, shapefile):
        for index, row in shapefile.iterrows():
            if row['geometry'].contains(Point(
                    geo_id_row['longitude'], geo_id_row['latitude']
            )):
                return row['GEOID']

    def show_map(self, prob_a, prob_b):
        """
        :param prob_a: switchover rate for plan A
        :param prob_b: switchover rate for plan B
        """
        # convert index type from tuple to str
        prob_a.index = [i[0] for i in list(prob_a.index)]
        prob_b.index = [i[0] for i in list(prob_b.index)]

        # import TN shapefile and convert GEOID column to numeric data type
        tn = gpd.read_file(self.shapefile_path, names=['GEOID', 'geometry'])
        tn['GEOID'] = pd.to_numeric(tn['GEOID'])

        # remove unused columns
        unused_geo_attributes = list(tn.columns)
        unused_geo_attributes.remove('GEOID')
        unused_geo_attributes.remove('geometry')
        tn = tn.drop(columns=unused_geo_attributes)

        # import geomap model
        geo_model = pd.read_csv(self.geomap_model_path, usecols=['households', 'GEOID', 'name'])

        # multiply by participation rates
        geo_model['households'] = geo_model.apply(household_after_prob_rate, prob_a=prob_a, prob_b=prob_b,
                                                  axis=1)

        # merge datasets
        for_plotting = tn.merge(geo_model, left_on='GEOID', right_on='GEOID')

        # sum rows based on GEOID to get total number of households in each GEOID
        aggregation_functions = {'geometry': 'first', 'households': 'sum'}
        for_plotting = for_plotting.groupby(for_plotting['GEOID']).aggregate(aggregation_functions)

        # plot
        fig, ax = plt.subplots(1, figsize=(14, 6))
        fig.canvas.set_window_title('Market Segments Visualized')
        ax.set_title('Market Segments Visualized')

        for_plotting.plot(column='households', cmap='Reds', linewidth=1, ax=ax, edgecolor='0.6',
                          legend=True, legend_kwds={'loc': 'lower right'},
                          scheme='quantiles')
        plt.show()
