The file descriptions are as follows:

_______________________________________________________________
baselinegraph.ipynb - graphing baseline results given in homework
configurations_RL.ipynb -all configurations tried for ablation
config_3_results_repetition_2.csv - result of configuration running
config_3_results_repetition_1.csv - result of configuration running
config_1_results_repetition_2.csv- result of configuration running
config_1_results_repetition_1.csv- result of configuration running
config_2_results_repetition_1.csv- result of configuration running
config_2_results_repetition_2.csv- result of configuration running
ablationstudygraphs.ipynb = all graphs for the configurations
_______________________________________________________________
TNandBuffernormal.ipynb - without violation in the TN network, 3 viable runs, target steps = 2000,
num_episodes = 100 (results)
Rewards_TNandBuffer.csv - without violation in the TN network, 3 viable runs, target steps = 2000,
num_episodes = 100(code)
_______________________________________________________________
TNnormal.ipynb - TN without violation - target steps = 2000, num_repetitions = 5, num_episodes=100
______________________________________________________________
TNwv.ipynb - TN with violation - target steps = 2000, num_repetitions = 5, num_episodes=100
TNwvgraph.ipynb
TNwvvalues.docx
______________________________________________________________
simple_initial_model.ipynb = without TN and ER, 200 target steps, num_repetitions=1,
num_episodes=100
simple_initial_model_values.docx = resulting values for simple initial model
initialmodelgraph.ipynb= resulting graph for simple initial model
_______________________________________________________________
rlwithbuffer.ipynb- buffer, 2000 target steps, num_repetitions = 5, num_episodes=100
rlwithbuffer.csv
RLBuffergraphing.ipynb
_______________________________________________________________
TNandBuffer.ipynb - with violation in TN network, 2000 target steps, num_repetitions = 5,
num_episodes=100
TNandBuffergraphing.ipynb
TNandBuffer_rewards.csv
________________________________________________________________
All the ipynb files were converted to py files and put in this folder.

Please note that according to the environment the code is being run on whether it is Colab or Jupyter, 
the error of the arguments of the Please note that according to the environment the code is being run on,
 whether it is Colab or Jupyter, the error related to the arguments of the next_state, immediate_reward, terminated,
 info = cartpole_env.step(action) function call may change from 4 to 5.

This is because different versions or configurations of the gym environment (e.g., OpenAI Gym)
 may have slight variations in their return values depending on the specific library or setup.
 In some versions of gym, the step function may return only four variables: next_state, immediate_reward, terminated, info. 
Please note that I tried to stick to Gym Version: 0.26.2

