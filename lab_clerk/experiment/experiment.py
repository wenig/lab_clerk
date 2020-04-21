import pandas as pd
from uuid import uuid1
import datetime as dt
import os


class Experiment:
    EXPERIMENT_FILE = "experiments.pkl"
    EVALUATION_FILE = "evaluations.pkl"

    def __init__(self, directory: str = ".", metrics: list = None, attributes: dict = None):
        self.experiment_id = uuid1()
        self.metrics = metrics or []
        self.attributes = attributes or {}
        self.directory = directory
        self.experiments_file = os.path.join(self.directory, Experiment.EXPERIMENT_FILE)
        self.evaluations_file = os.path.join(self.directory, Experiment.EVALUATION_FILE)

    def _add_experiment(self):
        exps = self._load_experiments()
        exps = exps.append(dict(id=self.experiment_id, attributes=self.attributes), ignore_index=True)
        exps.to_pickle(self.experiments_file)

    def _load_experiments(self) -> pd.DataFrame:
        if os.path.exists(self.experiments_file):
            return pd.read_pickle(self.experiments_file)
        return pd.DataFrame(columns=("id", "attributes"))

    def _get_evaluation_template(self) -> pd.DataFrame:
        return pd.DataFrame(columns=(
            "experiment_id",
            "step",
            "time",
            "metrics",
            "vals"
        ))

    def _load_results(self) -> pd.DataFrame:
        if os.path.exists(self.evaluations_file):
            return pd.read_pickle(self.evaluations_file)
        return self._get_evaluation_template()

    def add_results(self, step: int, *vals):
        self.results = self.results.append({
            "experiment_id": self.experiment_id,
            "step": step,
            "time": int(dt.datetime.utcnow().timestamp()),
            "metrics": self.metrics,
            "vals": vals
        }, ignore_index=True)

    def _commit_results(self):
        self.results.to_pickle(self.evaluations_file)

    def __enter__(self):
        self._add_experiment()
        self.results = self._load_results()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._commit_results()