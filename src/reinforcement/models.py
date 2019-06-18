import numpy as np


class GreedyModel:
    def __init__(self, n_traders):
        self.n_traders = n_traders
        self.accumulative_returns = np.zeros(n_traders)

    def learn_step(self, return_):
        self.accumulative_returns += return_

    def predict_portfolio(self):
        portfolio = np.zeros(self.n_traders)
        portfolio[self.accumulative_returns.argmax()] = 1
        return portfolio


class WeightedMovingAverageModel:
    def __init__(self, n_traders, alpha=1e-2):
        self.n_traders = n_traders
        self.alpha = alpha
        self.weighted_returns = np.zeros(n_traders)

    def learn_step(self, return_):
        self.weighted_returns *= (1 - self.alpha)
        self.weighted_returns += return_ * self.alpha

    def predict_portfolio(self):
        portfolio = np.zeros(self.n_traders)
        portfolio[self.weighted_returns.argmax()] = 1
        return portfolio


class ReinforcementComparisonModel:
    def __init__(self, n_traders, alpha=1e-2, betta=1e-2, tau = 1):
        self.alpha = alpha
        self.betta = betta
        self.tau = tau
        self.r_t = np.zeros(n_traders)
        self.p_t = np.zeros(n_traders)

    def learn_step(self, return_):
        self.p_t += self.betta * (return_ - self.r_t - self.p_t)
        self.r_t += self.alpha * (return_ - self.r_t)

    def predict_portfolio(self):
        portfolio = np.exp(self.p_t / self.tau)
        return portfolio / np.sum(portfolio)


class PursuitGreedyModel:
    def __init__(self, n_traders, betta=1e-2):
        self.betta = betta
        self.greedy_model = GreedyModel(n_traders)
        self.current_portfolio = np.ones(n_traders)

    def learn_step(self, return_):
        self.greedy_model.learn_step(return_)
        greedy_portfolio = self.greedy_model.predict_portfolio()
        self.current_portfolio += self.betta * (greedy_portfolio - self.current_portfolio)

    def predict_portfolio(self):
        return self.current_portfolio
