import pandas

from functools import (
    wraps
)

from pandas.plotting._matplotlib.tools import (
    create_subplots,
    flatten_axes
    # maybe_adjust_figure
)

from typing import (
    final
)

from pandas.core.base import (
    PandasObject
)

from pandas.core.groupby.groupby import (
    BaseGroupBy,
    GroupBy
)

@final
class GroupBySubplotImpl:
    """
    Implementation to create subplots based on groupby.
    """

    def __init__(self, 
        group: GroupBy, 
        **kwargs):
        self._groupby = group

        # Fix a bug for pandas.DataFrame.GroupBy
        if self._groupby.level is not None:
            self._groupby.keys = None

        self._subplots_kwargs = kwargs

    def __getattr__(self, plotfunc: str):
        if not hasattr(pandas.DataFrame.plot, plotfunc):
            raise Exception(f"Cannot find plotting accessor \"{plotfunc}\" for DataFrame.")

        @wraps(plotfunc)
        def func(*args, **kwargs):
            naxes = len(self._groupby)
            fig, axes = create_subplots(
                naxes=naxes,
                **self._subplots_kwargs
            )
            for (key, data), ax in zip(self._groupby, flatten_axes(axes)):
                getattr(data.plot, plotfunc)(ax = ax, *args, **kwargs)

            # if pandas.__version__ >= "1.5.0":
            #     maybe_adjust_figure(fig, bottom = 0.15, top = 0.9, left = 0.1, right = 0.9, wspace = 0.2)
            return fig

        return func

@final
class GroupBySubplot(PandasObject):
    """
    Class implementing the .subplots attribute for groupby objects.
    """

    def __init__(self, 
        groupby: GroupBy) -> None:
        self._groupby = groupby

    def __call__(self, 
        figsize = None,
        sharex: bool = False,
        sharey: bool = False,
        layout = None,
        **kwargs) -> GroupBySubplotImpl:
        '''interface for subplots
            :params: figsize: Pandas' native option to create subplots. A tuple (width, height) in inches
            :params: sharex: Pandas' native option to create subplots. Whether x-axes will be shared among subplots.
            :params: sharey: Pandas' native option to create subplots. Whether y-axes will be shared among subplots.
            :params: layout: Pandas' native option to create subplots. The layout of the plot: (rows, columns).

            :params: **kwargs: Other options to create subplots.
        '''
        return GroupBySubplotImpl(
            self._groupby,
            figsize = figsize,
            sharex = sharex,
            sharey = sharey,
            layout = layout,
            **kwargs
            )

    def __getattr__(self, name: str):

        @wraps(name)
        def attr(**kwargs):
            impl = GroupBySubplotImpl(self._groupby)
            return getattr(impl, name)(**kwargs)

        return attr

BaseGroupBy.subplots = property(GroupBySubplot)