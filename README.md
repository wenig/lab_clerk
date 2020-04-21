# lab_clerk

## Installation
```shell script
$ python setup.py install
```

## Usage
### in Experiment
```python
from lab_clerk import Experiment

with Experiment(metrics=["accuracy"], attributes={"meta-data": "meta-value"}) as experiment:
    # do something, e.g. train a neural network
    # evaluate your experiment
    accuracy = 0.99  # your evaluation
    experiment.add_results(1, accuracy)
```

### for Evaluation in Jupyter Notebook
```python
import pandas as pd
from lab_clerk import plot_tool
from ipywidgets import interact

experiments = pd.read_pickle("experiments.pkl")  # created with lab_clerk.Experiment
evaluations = pd.read_pickle("evaluations.pkl")  # created with lab_clerk.Experiment

interact(plot_tool(experiments, evaluations))
```
After that, a plotting tool should appear in your jupyter notebook.