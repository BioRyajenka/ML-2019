import matplotlib.pyplot as plt
import seaborn as sns


def filter_times(times, n):
    smth = int(len(times) / n)
    for i in range(len(times)):
        if i % smth != 0:
            times[i] = ''
        else:
            times[i] = times[i].split(' ')[0]


def show_plot(real_returns, real_accumulative_returns, times, filename=None):
    sns.set(style="whitegrid", font="serif")
    print("plotting")

    filter_times(times, 25)

    x = list(range(0, len(times)))
    plt.plot(x, real_returns, label="current return")
    plt.plot(x, real_accumulative_returns, label="overall return")

    plt.xticks(x, times, rotation='vertical')

    plt.grid(False, axis='x')
    plt.grid(True, axis='y')

    plt.legend(loc=2, frameon=True)

    if filename: plt.savefig(filename)
    plt.show()
