import unittest
import libpysal
import geopandas as gpd
import numpy as np
from segregation.aspatial import Dissim, MultiDissim
from segregation.inference import SingleValueTest, TwoValueTest


class Inference_Tester(unittest.TestCase):
    def test_Inference(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        index1 = Dissim(s_map, 'HISP_', 'TOT_POP')
        index2 = Dissim(s_map, 'BLACK_', 'TOT_POP')
        
        groups_list = ['WHITE_', 'BLACK_', 'ASIAN_','HISP_']
        m_index = MultiDissim(s_map, groups_list)
		
        m_index_1 = MultiDissim(s_map[0:200], groups_list)
        m_index_2 = MultiDissim(s_map[200:] , groups_list)
        
        # Single Value Tests #
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "systematic", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.01603886544282861)
        
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "bootstrap", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.31992467511262773)
        
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "evenness", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.01596295861644252)
        
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "permutation", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.32184656076566864)
        
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "systematic_permutation", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.01603886544282861)
        
        np.random.seed(123)
        res = SingleValueTest(index1, null_approach = "even_permutation", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.01619436868061094)
        
        np.random.seed(123)
        res = SingleValueTest(m_index, null_approach = "bootstrap", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.4143544081847027)
        
        np.random.seed(123)
        res = SingleValueTest(m_index, null_approach = "evenness", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), 0.01633979237418177)

        # Two Value Tests #
        np.random.seed(123)
        res = TwoValueTest(index1, index2, null_approach = "random_label", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), -0.0031386146371949076)
        
        np.random.seed(123)
        res = TwoValueTest(index1, index2, null_approach = "counterfactual_composition", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), -0.005032145622504718)
        
        np.random.seed(123)
        res = TwoValueTest(index1, index2, null_approach = "counterfactual_share", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), -0.034350440515125)
        
        np.random.seed(123)
        res = TwoValueTest(index1, index2, null_approach = "counterfactual_dual_composition", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), -0.004771386292706747)
		
        np.random.seed(123)
        res = TwoValueTest(m_index_1, m_index_2, null_approach = "random_label", iterations_under_null = 50)
        np.testing.assert_almost_equal(res.est_sim.mean(), -0.0024327144012562685)


if __name__ == '__main__':
    unittest.main()
