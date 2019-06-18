import numpy as np
import matplotlib.pyplot as plt


class ReinforcementLearning():



    def weighted_moving_average(self):
        alpha = 1e-4
        weighted_returns = np.zeros_like(self.returns[0])
        portfolios = []

        for idx, return_ in enumerate(self.returns):
            portfolio = np.zeros_like(self.returns[0])
            portfolio[weighted_returns.argmax()] = 1
            portfolios.append(portfolio)

            weighted_returns = weighted_returns * (1-alpha) + return_ * alpha

        return portfolios

    def reinforcement_comparison(self):
        alpha = 1e-2
        betta = 1e-2
        r_t = np.zeros_like(self.returns[0])
        p_t = np.zeros_like(self.returns[0])
        portfolios = []

        for idx, return_ in enumerate(self.returns):
            p_t = p_t + betta * (return_ - r_t)

            portfolio = np.exp(p_t)
            portfolio /= np.sum(portfolio)

            portfolios.append(portfolio)

            r_t = r_t + alpha * (return_ - r_t)

        return portfolios

    def pursuit_greedy(self):
        greedy_portfolios = self.greedy()
        betta = 1e-6
        portfolio = np.ones_like(0)
        portfolios = []

        for greedy_portfolio in greedy_portfolios:
            portfolio = portfolio + betta * (greedy_portfolio - portfolio)
            portfolio /= np.sum(portfolio)
            portfolios.append(portfolio)

        return portfolios


