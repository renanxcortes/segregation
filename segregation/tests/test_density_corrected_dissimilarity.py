import unittest
import libpysal
import geopandas as gpd
import numpy as np
from segregation.density_corrected_dissimilarity import Density_Corrected_Dissim


class Density_Corrected_Dissim_Tester(unittest.TestCase):

    def test_Density_Corrected_Dissim(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        df = s_map[['geometry', 'HISP_', 'TOT_POP']]
        index = Density_Corrected_Dissim(df, 'HISP_', 'TOT_POP')
        np.testing.assert_almost_equal(index.statistic, 0.2962244660362303)

if __name__ == '__main__':
    unittest.main()
