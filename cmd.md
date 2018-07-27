# SLT 2018 Special Session - Microsoft Dialogue Challenge: Building End-to-End Task-Completion Dialogue Systems

This document describes how to run the simulation and different dialogue agents (rule-based, reinforcement learning). More instructions to plug in your customized agents or user simulators are in the Recipe section of the paper.

## Content
* [Data](#data)
* [Parameter](#parameter)
* [Running Dialogue Agents](#running-dialogue-agents)
* [Evaluation](#evaluation)
* [Reference](#reference)

## Parameters

### Basic setting
`--agt`: the agent id<br/>
`--usr`: the user (simulator) id<br/>
`--max_turn`: maximum turns<br/>
`--episodes`: how many dialogues to run<br/>
`--slot_err_prob`: slot level err probability<br/>
`--slot_err_mode`: which kind of slot err mode<br/>
`--intent_err_prob`: intent level err probability


### Data setting
`--kb_path`: the kb path for agent side<br/>
`--goal_file_path`: the user goal file path for user simulator side

### Model setting
`--dqn_hidden_size`: hidden size for RL (DQN) agent<br/>
`--batch_size`: batch size for DQN training<br/>
`--simulation_epoch_size`: how many dialogue to be simulated in one epoch<br/>
`--warm_start`: use rule policy to fill the experience replay buffer at the beginning<br/>
`--warm_start_epochs`: how many dialogues to run in the warm start

### Display setting
`--run_mode`: 0 for display mode (NL); 1 for debug mode (Dia_Act); 2 for debug mode (Dia_Act and NL); >3 for no display (i.e. training)<br/>
`--act_level`: 0 for user simulator is Dia_Act level; 1 for user simulator is NL level<br/>
`--auto_suggest`: 0 for no auto_suggest; 1 for auto_suggest<br/>
`--cmd_input_mode`: 0 for NL input; 1 for Dia_Act input. (this parameter is for AgentCmd only)

### Others
`--write_model_dir`: the directory to write the models<br/>
`--trained_model_path`: the path of the trained RL agent model; load the trained model for prediction purpose.

`--learning_phase`: train/test/all, default is all. You can split the user goal set into train and test set, or do not split (all); We introduce some randomness at the first sampled user action, even for the same user goal, the generated dialogue might be different.<br/>


## Data

### Movie domain
all the movie data is under this folder: ./src/deep_dialog/data

* Movie Knowledge Bases<br/>
`movie_kb.1k.p` --- 94% success rate (for `user_goals_first_turn_template_subsets.v1.p`)<br/>
`movie_kb.v2.p` --- 36% success rate (for `user_goals_first_turn_template_subsets.v1.p`)

* User Goals<br/>
`user_goals_first_turn_template.v2.p` --- user goals extracted from the first user turn<br/>
`user_goals_first_turn_template.part.movie.v1.p` --- a subset of user goals [Please use this one, the upper bound success rate on movie_kb.1k.json is 0.9765.]

* NLG Rule Template<br/>
`dia_act_nl_pairs.v6.json` --- some predefined NLG rule templates for both User simulator and Agent.

* Dialog Act Intent<br/>
`dia_acts.txt`

* Dialog Act Slot<br/>
`slot_set.txt`


### Restaurant domain
all the restaurant data is under this folder: ./src/deep_dialog/data_restaurant

* Restaurant Knowledge Bases<br/>
`restaurant.kb.1k.v1.p` --- 47.80% success rate (for `user_goals_first.v1.p`)<br/>
`restaurant.kb.2k.v1.p` --- 66.72% success rate (for `user_goals_first.v1.p`)

* User Goals<br/>
`user_goals_first.v1.p` --- user goals extracted from the first user turn<br/>

* NLG Rule Template<br/>
`sim_dia_act_nl_pairs.v2.json` --- some predefined NLG rule templates for both User simulator and Agent.

* Dialog Act Intent<br/>
`dia_acts.txt`

* Dialog Act Slot<br/>
`restaurant_slots.txt`


### Taxi domain
all the restaurant data is under this folder: ./src/deep_dialog/data_taxi

* Restaurant Knowledge Bases<br/>
`taxi.kb.1k.v1.p` --- 46.22% success rate (for `user_goals_first.v3.p`)<br/>
`taxi.kb.2k.v1.p` --- 73.00% success rate (for `user_goals_first.v3.p`)

* User Goals<br/>
`user_goals_first.v3.p` --- user goals extracted from the first user turn<br/>

* NLG Rule Template<br/>
`sim_dia_act_nl_pairs.json` --- some predefined NLG rule templates for both User simulator and Agent.

* Dialog Act Intent<br/>
`dia_acts.txt`

* Dialog Act Slot<br/>
`taxi_slots.txt`


## Running Dialogue Agents

### Movie domain

#### Rule Agent
```sh
python run.py --agt 5 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --intent_err_prob 0.00
	      --slot_err_prob 0.00
	      --episodes 500
	      --act_level 0
```

#### Cmd Agent
NL Input
```sh
python run.py --agt 0 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --intent_err_prob 0.00
	      --slot_err_prob 0.00
	      --episodes 500
	      --act_level 0
	      --run_mode 0
	      --cmd_input_mode 0
```
Dia_Act Input
```sh
python run.py --agt 0 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p 
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --intent_err_prob 0.00
	      --slot_err_prob 0.00
	      --episodes 500
	      --act_level 0
	      --run_mode 0
	      --cmd_input_mode 1
```

#### End2End RL Agent
Train End2End RL Agent without NLU and NLG (with simulated noise in NLU)
```sh
python run.py --agt 9 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 0
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --warm_start 1
	      --warm_start_epochs 120
```
Train End2End RL Agent with NLU and NLG
```sh
python run.py --agt 9 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 1
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --warm_start 1
	      --warm_start_epochs 120
```
Test RL Agent with N dialogues:
```sh
python run.py --agt 9 --usr 1 --max_turn 40
	      --kb_path ./deep_dialog/data/movie_kb.1k.p
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 300 
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --goal_file_path ./deep_dialog/data/user_goals_first_turn_template.part.movie.v1.p
	      --trained_model_path ./deep_dialog/checkpoints/rl_agent/noe2e/agt_9_478_500_0.98000.p
	      --run_mode 3
```

### Restaurant domain

#### Rule Agent
```sh
python run.py --agt 10 --usr 2 --max_turn 30
	      --kb_path ./deep_dialog/data_restaurant/restaurant.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_restaurant/user_goals_first.v1.p
	      --slot_set ./deep_dialog/data_restaurant/restaurant_slots.txt
	      --act_set ./deep_dialog/data_restaurant/dia_acts.txt
	      --dict_path ./deep_dialog/data_restaurant/slot_dict.v2.p
	      --nlg_model_path ./deep_dialog/models/nlg/restaurant/lstm_tanh_[1532068150.19]_98_99_294_0.983.p
	      --nlu_model_path ./deep_dialog/models/nlu/restaurant/lstm_[1532107808.26]_68_74_20_0.997.p
	      --diaact_nl_pairs ./deep_dialog/data_restaurant/sim_dia_act_nl_pairs.v2.json
	      --intent_err_prob 0.00
	      --slot_err_prob 0.00
	      --episodes 500
	      --act_level 0
```


#### End2End RL Agent
Train End2End RL Agent without NLU and NLG (with simulated noise in NLU)
```sh
python run.py --agt 12 --usr 2 --max_turn 30
	      --kb_path ./deep_dialog/data_restaurant/restaurant.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_restaurant/user_goals_first.v1.p
	      --slot_set ./deep_dialog/data_restaurant/restaurant_slots.txt
	      --act_set ./deep_dialog/data_restaurant/dia_acts.txt
	      --dict_path ./deep_dialog/data_restaurant/slot_dict.v2.p
	      --nlg_model_path ./deep_dialog/models/nlg/restaurant/lstm_tanh_[1532068150.19]_98_99_294_0.983.p
	      --nlu_model_path ./deep_dialog/models/nlu/restaurant/lstm_[1532107808.26]_68_74_20_0.997.p
	      --diaact_nl_pairs ./deep_dialog/data_restaurant/sim_dia_act_nl_pairs.v2.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 0
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --warm_start 1
	      --warm_start_epochs 120
```
Train End2End RL Agent with NLU and NLG
```sh
python run.py --agt 12 --usr 2 --max_turn 30
	      --kb_path ./deep_dialog/data_restaurant/restaurant.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_restaurant/user_goals_first.v1.p
	      --slot_set ./deep_dialog/data_restaurant/restaurant_slots.txt
	      --act_set ./deep_dialog/data_restaurant/dia_acts.txt
	      --dict_path ./deep_dialog/data_restaurant/slot_dict.v2.p
	      --nlg_model_path ./deep_dialog/models/nlg/restaurant/lstm_tanh_[1532068150.19]_98_99_294_0.983.p
	      --nlu_model_path ./deep_dialog/models/nlu/restaurant/lstm_[1532107808.26]_68_74_20_0.997.p
	      --diaact_nl_pairs ./deep_dialog/data_restaurant/sim_dia_act_nl_pairs.v2.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 1
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --warm_start 1
	      --warm_start_epochs 120
```
Test RL Agent with N dialogues:
```sh
python run.py --agt 12 --usr 2 --max_turn 30
	      --kb_path ./deep_dialog/data_restaurant/restaurant.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_restaurant/user_goals_first.v1.p
	      --slot_set ./deep_dialog/data_restaurant/restaurant_slots.txt
	      --act_set ./deep_dialog/data_restaurant/dia_acts.txt
	      --dict_path ./deep_dialog/data_restaurant/slot_dict.v2.p
	      --nlg_model_path ./deep_dialog/models/nlg/restaurant/lstm_tanh_[1532068150.19]_98_99_294_0.983.p
	      --nlu_model_path ./deep_dialog/models/nlu/restaurant/lstm_[1532107808.26]_68_74_20_0.997.p
	      --diaact_nl_pairs ./deep_dialog/data_restaurant/sim_dia_act_nl_pairs.v2.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 300 
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --trained_model_path ./deep_dialog/checkpoints/rl_agent/noe2e/agt_9_478_500_0.98000.p
	      --run_mode 3
```

### Taxi domain

#### Rule Agent
```sh
python run.py --agt 8 --usr 3 --max_turn 30
	      --kb_path ./deep_dialog/data_taxi/taxi.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_taxi/user_goals_first.v3.p
	      --slot_set ./deep_dialog/data_taxi/taxi_slots.txt
	      --act_set ./deep_dialog/data_taxi/dia_acts.txt
	      --dict_path ./deep_dialog/data_taxi/slot_dict.v1.p
	      --nlg_model_path ./deep_dialog/models/nlg/taxi/lstm_tanh_[1532457558.95]_95_99_194_0.985.p
	      --nlu_model_path ./deep_dialog/models/nlu/taxi/lstm_[1532583523.63]_88_99_400_0.998.p
	      --diaact_nl_pairs ./deep_dialog/data_taxi/sim_dia_act_nl_pairs.json
	      --intent_err_prob 0.00
	      --slot_err_prob 0.00
	      --episodes 500
	      --act_level 0
```

#### End2End RL Agent
Train End2End RL Agent without NLU and NLG (with simulated noise in NLU)
```sh
python run.py --agt 13 --usr 3 --max_turn 30
	      --kb_path ./deep_dialog/data_taxi/taxi.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_taxi/user_goals_first.v3.p
	      --slot_set ./deep_dialog/data_taxi/taxi_slots.txt
	      --act_set ./deep_dialog/data_taxi/dia_acts.txt
	      --dict_path ./deep_dialog/data_taxi/slot_dict.v1.p
	      --nlg_model_path ./deep_dialog/models/nlg/taxi/lstm_tanh_[1532548061.28]_92_99_190_0.986.p
	      --nlu_model_path ./deep_dialog/models/nlu/taxi/lstm_[1532621815.29]_38_39_380_0.992.p
	      --diaact_nl_pairs ./deep_dialog/data_taxi/sim_dia_act_nl_pairs.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 0
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --warm_start 1
	      --warm_start_epochs 120
```
Train End2End RL Agent with NLU and NLG
```sh
python run.py --agt 13 --usr 3 --max_turn 30
	      --kb_path ./deep_dialog/data_taxi/taxi.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_taxi/user_goals_first.v3.p
	      --slot_set ./deep_dialog/data_taxi/taxi_slots.txt
	      --act_set ./deep_dialog/data_taxi/dia_acts.txt
	      --dict_path ./deep_dialog/data_taxi/slot_dict.v1.p
	      --nlg_model_path ./deep_dialog/models/nlg/taxi/lstm_tanh_[1532548061.28]_92_99_190_0.986.p
	      --nlu_model_path ./deep_dialog/models/nlu/taxi/lstm_[1532621815.29]_38_39_380_0.992.p
	      --diaact_nl_pairs ./deep_dialog/data_taxi/sim_dia_act_nl_pairs.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 500
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --run_mode 3
	      --act_level 1
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --warm_start 1
	      --warm_start_epochs 120
```
Test RL Agent with N dialogues:
```sh
python run.py --agt 13 --usr 3 --max_turn 30
	      --kb_path ./deep_dialog/data_taxi/taxi.kb.1k.v1.p
	      --goal_file_path ./deep_dialog/data_taxi/user_goals_first.v3.p
	      --slot_set ./deep_dialog/data_taxi/taxi_slots.txt
	      --act_set ./deep_dialog/data_taxi/dia_acts.txt
	      --dict_path ./deep_dialog/data_taxi/slot_dict.v1.p
	      --nlg_model_path ./deep_dialog/models/nlg/taxi/lstm_tanh_[1532548061.28]_92_99_190_0.986.p
	      --nlu_model_path ./deep_dialog/models/nlu/taxi/lstm_[1532621815.29]_38_39_380_0.992.p
	      --diaact_nl_pairs ./deep_dialog/data_taxi/sim_dia_act_nl_pairs.json
	      --dqn_hidden_size 80
	      --experience_replay_pool_size 1000
	      --episodes 300 
	      --simulation_epoch_size 100
	      --write_model_dir ./deep_dialog/checkpoints/rl_agent/
	      --slot_err_prob 0.00
	      --intent_err_prob 0.00
	      --batch_size 16
	      --trained_model_path ./deep_dialog/checkpoints/rl_agent/noe2e/agt_9_478_500_0.98000.p
	      --run_mode 3
```


## Evaluation
To evaluate the performance of agents, three metrics are available: success rate, average reward, average turns. Here we show the learning curve with success rate.

1. Plotting Learning Curve
``` python draw_learning_curve.py --result_file ./deep_dialog/checkpoints/rl_agent/noe2e/agt_9_performance_records.json```
2. Pull out the numbers and draw the curves in Excel

## Contact
* For questions specific to the challenge, you can contact us at <xiul@microsoft.com>.
