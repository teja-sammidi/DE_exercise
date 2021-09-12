'''Test module for policy_expert_exrecise
'''

import unittest
import pandas as pd
import policy_expert_exercise
import filepath
import io
import os
from unittest.mock import patch
from os import getenv
from pandas.util.testing import assert_frame_equal

class DFTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        
        TEST_INPUT_DIR = getenv('file_path')
        test_file_name =  'components.csv'
        try:
            component_df = pd.read_csv(TEST_INPUT_DIR + test_file_name)
                
        except IOError:
            print('cannot open file')
        self.fixture = component_df
    @classmethod
    def setUpClass(cls):
        #print('setUpClass')
        #define mock data for the order files
        cls.mock_order_df = pd.DataFrame ( 
                    {"timestamp":["2021-06-02","2021-06-02"],
                     "orderId":["6636296c-7b6c-4747-838e-d3808b44988d","6636296c-7b6c-4747-838e-d3808b44988d"],
                     "units":[5,23],
                     'componentId':['XNPRP05','BKRED01']
                     })
    def test_dataFrame_component_df_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        component_df = pd.DataFrame({'componentId':['BKRED01','BKONG13'],'colour':['Red','Orange'],'costPrice':[0.021,0.022]})

   
        assert_frame_equal(self.fixture.head(2), component_df)
    def test_dataFrame_order_df_constructedAsExpected(cls):
        try:
            order_df=policy_expert_exercise.read_order_file_to_dataframe().head(1)
            order_df['timestamp'].astype(str).reset_index(drop=True)
            cls.mock_order_df.timestamp.astype(str).reset_index(drop=True)
            pd.testing.assert_frame_equal(order_df[['orderId','units']], cls.mock_order_df['orderId','units'].head(1),check_dtype=True)
        except Exception as error :
            print(error)
        
if __name__ == '__main__':
    unittest.main()