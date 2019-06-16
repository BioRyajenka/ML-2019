import pandas as pd
import numpy as np


class Evaluator():
    def __init__(self, file, start, end):
        df = pd.read_csv(file)

        starts = np.array(df.loc[df['TIME'] == start].values[0][1:])
        ends = np.array(df.loc[df['TIME'] == end].values[0][1:])

        self.returns = {}
        for trader_id, rt in zip(df.columns.values[1:], ends - starts):
            self.returns[trader_id] = rt / 100

    def evaluate_portfolio(self, portfolio):
        def normalize_portfolio():
            summ = np.sum(list(portfolio.values()))
            for key in portfolio.keys():
                portfolio[key] /= summ

        normalize_portfolio()
        res = 0
        for key, value in portfolio.items():
            res += value * (self.returns[key])
        return res * 100
