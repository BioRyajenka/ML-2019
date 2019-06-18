import matplotlib.pyplot as plt
import seaborn as sns


def show_plot(real_returns, real_accumulative_returns, filename=None):
    sns.set(style="whitegrid", font="serif")

    plt.plot(real_returns, label="current return")
    plt.plot(real_accumulative_returns, label="overall return")
    # x = np.arange(0, len(times))
    # plt.xticks(x, times)
    # plt.ylim(ymin=-10000, ymax=10000)

    plt.grid(True)
    plt.legend(loc=2, frameon=True)

    if filename: plt.savefig(filename)
    plt.show()
