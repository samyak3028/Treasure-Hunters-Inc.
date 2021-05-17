# Treasure-Hunters-Inc.

## Introduction
The objective of this assignment is to implement a treasure hunt game using Reinforcement learning algorithm. I've designed a very simple 14 x 14 map with few obstacles and reward pointsto find the optimal path. Q-Learning algorithm is used to predict the efficient moves in this assignment.

### Reinforcement learning
Reinforcement Learning (RL) is a type of machine learning technique that enables an agent to learn in an interactive environment by trial and error using feedback from its own actions and experiences. As compared to unsupervised learning, reinforcement learning is different in terms of goals. The reinforcement learning algorithm is an independent, self-teaching system.


Q-Learning attempts to learn the value of being in each state and taking a specific action there. This table 196 X 5where each row is a state and 5 columns correspond to the actions up/down/left/right/neutral. This table is gradually updated as we observe the rewards the agent obtain for various actions using Bellman Equation: Q(s,a) = r + γ(max(Q(ś,á)) ‘s’ is current state, ‘a’ is the action the agent takes from the current state, ‘ ś ’ represents the state resulting from the action ‘r’ is the reward for taking the action and ‘γ’ is the discount factor. So, the Q value for the state‘s’ taking the action ‘a’ is the sum of the instant reward and the discounted future reward (value of the resulting state). The discount factor ‘γ’ determines the importance of future rewards. If the agent go to a state further away from the goal state, but from there the chances of encountering a state with obstacles is less, then the future reward is more even though the instant reward is less. For each iteration (attempt made by the agent), the agent will try to achieve the goal state and for every transition it will keep on updating the values of the Q-table.

### Working
Firstly, reward points are set which depicts real time scenarios like moving on ground consumes some energy/resources negative value is assigned to motivate for shorter path and an obstacle is not assigned any value as that block will never be crossed.

Secondly, a map function is defined which sets the dimension and colour of various features to construct a map and map constants are also determine.

![Markov Model Built](https://github.com/samyak3028/Treasure-Hunters-Inc./blob/main/map.png?raw=true)



Thirdly, there are various functions related to movement of objects which includes “Move_state”  determines what are the possible walks in which object can move based on direction like north, south, east , and west, “possible_move” determines the possible move from a arbitary state ,“best_next_move” determines the optimal move from a position, and next_move determines the next move for exploring and exploiting.

Fourthly, all the states are converted into positions, model is trained multiple times.

![Markov Model Built](https://github.com/samyak3028/Treasure-Hunters-Inc./blob/main/output.png?raw=true)


Finally, Output is generated and path is determined on the basis of highest value in Q matrix.


![Markov Model Built](https://github.com/samyak3028/Treasure-Hunters-Inc./blob/main/mapoutput.png?raw=true)








