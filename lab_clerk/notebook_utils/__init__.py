from pandas import DataFrame
from ipywidgets import SelectMultiple, Select
import matplotlib.pyplot as plt
from typing import Callable
import numpy as np


def plot_tool(experiments: DataFrame, evaluations: DataFrame) -> Callable[[SelectMultiple, Select, SelectMultiple], None]:
    select_experiment_ids = SelectMultiple(
        options=experiments.id.values,
        value=[],
        # rows=10,
        description='Experiments',
        disabled=False)

    select_x = Select(
        options=evaluations.columns,
        value=None,
        description='X Axis',
        disabled=False)

    select_y = SelectMultiple(
        options=np.unique(evaluations.metrics.values.sum()),
        value=[],
        description='Y Axis',
        disabled=False)

    def plot(experiment_id=select_experiment_ids, x_axis=select_x, y_axis=select_y):
        if len(experiment_id) > 0:
            data = evaluations[evaluations.experiment_id.isin(experiment_id)]
        else:
            data = evaluations
        subplots = []
        n_metrics = len(y_axis) * 100
        for i, metric in enumerate(y_axis):
            if len(subplots) == 0:
                ax = plt.subplot(n_metrics + 11 + i)
            else:
                ax = plt.subplot(n_metrics + 11 + i, sharex=subplots[0])
            subplots.append(ax)
            ind = data.metrics.iloc[0].index(metric)
            plt.ylim(0.5, 1.0)
            plt.plot(data[x_axis], data.vals.apply(lambda y: y[ind]))
        plt.show()

    return plot
