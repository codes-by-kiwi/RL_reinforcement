import pandas as pd

config_1_results_repetition_1 = pd.read_csv('config_1_results_repetition_1 (2).csv')
config_1_results__repetition_2 = pd.read_csv('config_1_results_repetition_2 (2).csv')
config_2_results_repetition_1 = pd.read_csv('config_2_results_repetition_1 (2).csv')
config_2_results_repetition_2 = pd.read_csv('config_2_results_repetition_2 (2).csv')
config_3_results_repetition_1 = pd.read_csv('config_3_results_repetition_1 (2).csv')
config_3_results_repetition_2 = pd.read_csv('config_3_results_repetition_2 (2).csv')

file_names = ['config_1_results_repetition_1 (2).csv', 'config_1_results_repetition_2 (2).csv','config_2_results_repetition_1 (2).csv', 'config_2_results_repetition_2 (2).csv','config_3_results_repetition_1 (2).csv', 'config_3_results_repetition_2 (2).csv']
file_names_config_1 = ['config_1_results_repetition_1 (2).csv', 'config_1_results_repetition_2 (2).csv']
file_names_config_2 = ['config_2_results_repetition_1 (2).csv', 'config_2_results_repetition_2 (2).csv']
file_names_config_3 = ['config_3_results_repetition_1 (2).csv', 'config_3_results_repetition_2 (2).csv']

rewards_all_runs_config_1 = {i: [] for i in range(1, 3)}
rewards_all_runs_config_2 = {i: [] for i in range(1, 3)}
rewards_all_runs_config_3 = {i: [] for i in range(1, 3)}

for idx, file_name in enumerate(file_names_config_1, start=1):
    df = pd.read_csv(file_name)  # Read CSV file
    episodes = df['Episode'].values
    rewards = df['Total Reward'].values
    rewards_all_runs_config_1[idx] = rewards

for idx, file_name in enumerate(file_names_config_2, start=1):
    df = pd.read_csv(file_name)  # Read CSV file
    episodes = df['Episode'].values
    rewards = df['Total Reward'].values
    rewards_all_runs_config_2[idx] = rewards

for idx, file_name in enumerate(file_names_config_3, start=1):
    df = pd.read_csv(file_name)  # Read CSV file
    episodes = df['Episode'].values
    rewards = df['Total Reward'].values
    rewards_all_runs_config_3[idx] = rewards

plt.figure(figsize=(10, 6))

for repetition in range(1, 3):
    if len(rewards_all_runs_config_1[repetition]) > 0:
        plt.plot(episodes[:len(rewards_all_runs_config_1[repetition])], rewards_all_runs_config_1[repetition], label=f'Config 1 - Repetition {repetition}')

max_length_config_1 = min(len(run) for run in rewards_all_runs_config_1.values())
avg_rewards_config_1 = np.mean([run[:max_length_config_1] for run in rewards_all_runs_config_1.values()], axis=0)

plt.plot(avg_rewards_config_1, label='Config 1 - Average Reward', color='black', linestyle='--', linewidth=2)

for repetition in range(1, 3):
    if len(rewards_all_runs_config_2[repetition]) > 0:
        plt.plot(episodes[:len(rewards_all_runs_config_2[repetition])], rewards_all_runs_config_2[repetition], label=f'Config 2 - Repetition {repetition}')

max_length_config_2 = min(len(run) for run in rewards_all_runs_config_2.values())
avg_rewards_config_2 = np.mean([run[:max_length_config_2] for run in rewards_all_runs_config_2.values()], axis=0)

plt.plot(avg_rewards_config_2, label='Config 2 - Average Reward', color='red', linestyle='--', linewidth=2)

for repetition in range(1, 3):
    if len(rewards_all_runs_config_3[repetition]) > 0:
        plt.plot(episodes[:len(rewards_all_runs_config_3[repetition])], rewards_all_runs_config_3[repetition], label=f'Config 3 - Repetition {repetition}')

max_length_config_3 = min(len(run) for run in rewards_all_runs_config_3.values())
avg_rewards_config_3 = np.mean([run[:max_length_config_3] for run in rewards_all_runs_config_3.values()], axis=0)

plt.plot(avg_rewards_config_3, label='Config 3 - Average Reward', color='blue', linestyle='--', linewidth=2)

plt.xlabel('Episodes')
plt.ylabel('Total Reward')
plt.title('Total Reward per Episode for Config 1 and Config 2 and Config 3')
plt.legend(loc='upper left')
plt.grid(True)

plt.show()

