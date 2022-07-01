import pandas
from src.subplots import *

import pandas.util._test_decorators as td

import pandas._testing as tm

from pandas.tests.plotting.common import TestPlotBase

@td.skip_if_no_mpl
class TestGroupbySubplots(TestPlotBase):

    def get_group(self):
        df = pandas.DataFrame([[1,2,3], [1,3,5],[2,2,6],[2,3,8]], columns = ["A", "B", "C"])
        return df.groupby(["A", "B"])

    def test_subplots_bar(self):
        group = self.get_group()
        group.subplots.bar(rot = 1)
        tm.close()

    def test_subplots_bar_with_params(self):
        group = self.get_group()
        group.subplots(sharex = True).bar(rot = 1)
        tm.close()

