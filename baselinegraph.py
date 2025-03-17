import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/RandomBaselineCartPole.csv')

episode_return = df['Episode_Return']
episode_return_smooth = df['Episode_Return_smooth']
env_step = df['env_step']

plt.plot(env_step, episode_return, label='Episode Return')
plt.plot(env_step, episode_return_smooth, label='Smoothed Episode Return')

plt.xlabel('Environment Step')
plt.ylabel('Total Reward')
plt.title('Q Learning with Neural Network Graph using CartPole (Baseline)')

plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/RandomBaselineCartPole.csv')

episode_return = df['Episode_Return']
episode_return_smooth = df['Episode_Return_smooth']
env_step = df['env_step']

plt.plot(env_step, episode_return, label='Episode Return')
# plt.plot(env_step, episode_return_smooth, label='Smoothed Episode Return')

plt.xlabel('Environment Step')
plt.ylabel('Total Reward')
plt.title('Q Learning with Neural Network Graph using CartPole (Baseline)')

plt.legend()
plt.show()

print(df)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/RandomBaselineCartPole.csv')

episode_return = df['Episode_Return']
episode_return_smooth = df['Episode_Return_smooth']
env_step = df['env_step']

plt.clf()  # Clears any previous plots
# plt.plot(env_step, episode_return, label='Episode Return')
plt.plot(env_step, episode_return_smooth, label='Smoothed Episode Return', linewidth=1)

plt.xlabel('Environment Step')
plt.ylabel('Total Reward')
plt.title('Q Learning with Neural Network Graph using CartPole (Baseline)')

plt.legend()
plt.show()

df = df.sort_values('env_step')
plt.plot(df['env_step'], df['Episode_Return_smooth'], label='Smoothed Episode Return')
print(df)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/RandomBaselineCartPole.csv')
df = df.sort_values('env_step')

episode_return = df['Episode_Return']
episode_return_smooth = df['Episode_Return_smooth']
env_step = df['env_step']

plt.clf()
plt.plot(env_step, episode_return_smooth, label='Smoothed Episode Return', linewidth=1)

plt.xlabel('Environment Step')
plt.ylabel('Total Reward')
plt.title('Q Learning with Neural Network Graph using CartPole (Baseline)')

plt.legend()
plt.show()

import numpy as np

window_size = 50
window = np.ones(window_size) / window_size
episode_return_smooth = np.convolve(episode_return, window, mode='valid')
df['Episode_Return_smooth'] = df['Episode_Return'].rolling(window=50).mean()
plt.plot(env_step[:len(episode_return_smooth)], episode_return_smooth, label='Convolved Episode Return', linewidth=1)

plt.xlabel('Environment Step')
plt.ylabel('Moving Average Reward over 50 steps')