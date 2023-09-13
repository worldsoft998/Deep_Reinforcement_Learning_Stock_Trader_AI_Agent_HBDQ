Stock Trader Based on Deep Reinforcement Learning AI Agent 

(Repo: Deep_Reinforcement_Learning_Stock_Trader_AI_Agent_HBDQ) 


An DQN (Deep Q Network or Deep Q-Learning network) AI Agent was developed by combining reinforcement learning (Q-Learning) and deep neural networks classifier  with multilayer perceptron (MLP) which chooses to sell, buy, or keep stocks from various companies. 

This AI agent was made with Tensorflow's Keras API, Sklearn, Pandas, and Numpy. 

This Agent was developed to choose whether to buy/sell/keep stocks from  Apple, Motorola Solutions and Starbucks. Of course it can be modified to trade for other stock combinations.

The agent was able to achieve a profit of $21000 in 20 episodes of trading stocks. 

More in depth stats of the Agents after 20 episodes: 

	Average Value of Portfolio: 37720, 
	Min Value of Portfolio: 26000, 
	Max Value of Portfolio: 41380. 


AI Technologies Involved
=======================

Reinforcement Learning

Q-Learning

Deep Q-Learning (DQL)
combine Q-learning with deep neural networks. This approach is coined as Deep Q-Learning (DQL)

Deep Q-Network: A combination of Q-Learning (QL) and Neural Networks.



AI Modules to be Applied
=====================
tensorflow
sklearn


Run the Trader
===========

To Train: python drl_stock_trader.py -m train && python rewards_output.py -m train

To Test: python drl_stock_trader.py -m test && python rewards_output.py -m test

The results:  The folder "drl_trader_rewards" contains the rewards output after the test.


Main Classes and Functions:
=====================


def MLP(input_dim, n_action, n_hidden_layers=1, hidden_dim=32):

class StockTradeEnviron:

class DQN_Agents(object):

def play_one_instance(agent_, env_, is_train):


Input Datasets
==========

aapl_msi_sbux.csv

Historic stock prices from Apple, Motorola Solutions and Starbucks. 

