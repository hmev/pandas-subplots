# pandas-subplots

A pandas interface to create subplots based on grouped data. 

## How to:

By replacing "data.plot" to "group.subplots", you can reuse existed plotting methods to create a figure with subplots.

```python
group.subplots.bar(rot = 1)
```

You can pass pandas' subplots params 

As 'subplots' is spliited from 'PlotAccessor', you could pass subplot-related params directly to config the layout.

```python
group.subplots(sharex = True).bar(rot = 1)
```

## How do parameters pass:

The pandas-subplots extension acts only as a bridge between pandas' "create_subplots" and pandas' plotting accessors. All parameters are finally injected to these pandas framework.

1. Parameters accepted in "group.subplots" are injected to "create_subplots", such as:

```
figsize:    Pandas' native option to create subplots. A tuple (width, height) in inches
sharex:     Pandas' native option to create subplots. Whether x-axes will be shared among subplots.
sharey:     Pandas' native option to create subplots. Whether y-axes will be shared among subplots.
layout:     Pandas' native option to create subplots. The layout of the plot: (rows, columns).

**kwargs:   Other options to create subplots.
```

2. Parameters accepted in subplotting accessors such as "group.subplots.plot" or "group.subplots.bar" are finally injected to the related pandas' plot accessor.