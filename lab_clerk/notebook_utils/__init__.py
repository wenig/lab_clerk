from pandas import DataFrame
from ipywidgets import SelectMultiple
import matplotlib.pyplot as plt
from typing import Callable


def plot_tool(experiments: DataFrame, evaluations: DataFrame) -> Callable[[SelectMultiple, SelectMultiple, SelectMultiple], None]:
    select_experiment_ids = SelectMultiple(
        options=experiments.id.values,
        value=[],
        description='Experiments',
        disabled=False)

    select_x = SelectMultiple(
        options=evaluations.columns,
        value=[],
        description='X Axis',
        disabled=False)

    select_y = SelectMultiple(
        options=evaluations.columns,
        value=[],
        description='Y Axis',
        disabled=False)

    def plot(experiment_id: SelectMultiple = select_experiment_ids,
             x_axis: SelectMultiple = select_x,
             y_axis: SelectMultiple = select_y):
        data = evaluations[evaluations.experiment_id.isin(experiment_id)]
        plt.plot(data[list(x_axis)], data[list(y_axis)].apply(lambda x: x.map(lambda y: y[0])))

    return plot
