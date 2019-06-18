import operator

import numpy as np


def parse_data(filepath, max_traders=int(1e6), max_total_return=1500):
    def fill_empties(xs):
        return list(map(lambda x: '0' if x == '' else x, xs))

    def get_values_from_line(line):
        ret = line[:-1].split(",")
        time = ret[0]
        ret = ret[1:]
        ret = np.array(fill_empties(ret), dtype=np.float)
        return time, ret

    f = open(filepath, "r")
    lines = [x for x in f][1:]

    rets = [get_values_from_line(x) for x in lines]

    indexes = [i for i, v in enumerate(rets[-1][1]) if abs(v) < max_total_return]
    indexes = indexes[:max_traders]

    total_returns = [np.array(operator.itemgetter(*indexes)(r[1])) for r in rets]

    returns = [next_line - prev_line for prev_line, next_line in zip(total_returns[:-1], total_returns[1:])]
    times = [r[0] for r in rets][1:]
    n_traders = len(returns[0])

    return returns, times, n_traders

