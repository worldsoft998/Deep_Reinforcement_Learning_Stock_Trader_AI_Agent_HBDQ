import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', type=str, required=True,
                    help='either "train" or "test"')
args = parser.parse_args()

a = np.load(f'drl_trader_rewards/{args.mode}.npy')

print(f"Average reward: {a.mean():.2f}, Min: {a.min():.2f}, Max: {a.max():.2f}")

plt.hist(a, bins=20)
plt.title(f"DQN Agent in {args.mode.capitalize()}ing")
plt.show()

"""
To train: ```python drl_stock_trader.py -m train && python rewards_output.py -m train```
To Test: ```python drl_stock_trader.py -m test && python rewards_output.py -m test```
"""
