from src.reinforcement.parser import parse_data
from src.reinforcement.models import GreedyModel, WeightedMovingAverageModel, ReinforcementComparisonModel, PursuitGreedyModel
from src.reinforcement.verificator import verify
from src.reinforcement.plotter import show_plot

filepath = "data/1000traders_2years.txt"

if __name__ == "__main__":
    returns, times, n_traders = parse_data(filepath, max_traders=10)

    model = PursuitGreedyModel(n_traders, betta=3e-4)

    real_returns, real_accumulative_returns = verify(returns, model, 50)

    show_plot(real_returns, real_accumulative_returns)