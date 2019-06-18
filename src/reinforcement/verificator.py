import numpy as np


def verify(returns, model, checking_start_in_percents):
    checking_start = len(returns) * checking_start_in_percents / 100
    real_returns, real_accumulative_returns = [], []
    curr_money = 1

    for idx, return_ in enumerate(returns):
        portfolio = model.predict_portfolio()
        real_return = np.dot(portfolio, return_.T)

        model.learn_step(return_)

        if idx > checking_start:
            curr_money *= (1 + real_return / 100)

            real_returns.append(real_return)
            real_accumulative_returns.append((curr_money - 1) * 100)

    return real_returns, real_accumulative_returns
