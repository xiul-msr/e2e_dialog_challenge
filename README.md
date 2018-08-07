# SLT 2018 Special Session - Microsoft Dialogue Challenge: Building End-to-End Task-Completion Dialogue Systems

## News
- [ ] 12/18/2018 – 12/21/2018: [SLT Workshop](http://www.slt2018.org/news/)
- [ ] 11/25/2018: Paper acceptance announcement.
- [ ] 11/11/2018: Paper submission.
- [ ] 11/04/2018: Results (including human evaluation) Announcement.
- [ ] 10/14/2018: System submission. (Format to be announaced.)
- [x] 08/03/2018: Movie domain is up, see [cmd.md](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/cmd.md) for instruction.
- [x] 07/28/2018: Restaurant and Taxi domains: [Data](https://github.com/xiul-msr/e2e_dialog_challenge/data/) and [Simulators](https://github.com/xiul-msr/e2e_dialog_challenge/system/) are up, see [cmd.md](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/cmd.md) for instruction.
- [x] 07/16/2018: [Registration](https://docs.google.com/forms/d/e/1FAIpQLScWl3BYiCLHjR2hGrkehx1kS53vvMTmQ2ktuvGNYSAtiQLSpw/viewform) is now open.
- [x] 07/06/2018: [Task description](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/microsoft-dialogue-challenge-slt2018.pdf) is up.

## Task
This special session introduces a Dialogue Challenge for building end-to-end task-completion dialogue systems, with the goal of encouraging the dialogue research community to collaborate and benchmark on standard datasets and unified experimental environment. In this special session, we will release human-annotated conversational data in three domains (movie-ticket booking, restaurant reservation, and taxi booking), as well as an experiment platform with built-in simulators in each domain, for training and evaluation purposes. The final submitted systems will be evaluated both in simulated setting and by human judges.

Please check this [description](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/microsoft-dialogue-challenge-slt2018.pdf) for more details about the task.

## Data
In this dialogue challenge, we will release well-annotated datasets for three task-completion domains: movie-ticket booking, restaurant reservation, and taxi ordering. Here shows the statistics of the three datasets.

|Task|Intents|Slots|Dialogues|
| -----| ----- | ----- | ----- |
|Movie-Ticket Booking|11|29|2890|
|Restaurant Reservation|11|30|4103|
|Taxi Ordering|11|29|3094|

## Evaluation
As described in the [task description](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/microsoft-dialogue-challenge-slt2018.pdf) (Section 4), we will evaluate the dialogue systems using both automatic and human evaluations on three criteria.
* Success Rate: the fraction of dialogs that finish successfully.
* Average Turns: the average length of the dialogue
* Average Reward: the average reward received during the conversation.
There is a strong correlation among the three metrics: generally speaking, a good policy should have a high success rate, high average reward and low average turns. Here, we choose success rate as our major evaluation metric.

We will also conduct human evaluation for the competition. We will ask human judges to interact with the final systems submitted by participants. Besides the measurements aforementioned, each user will also give a rating on a scale of 1 to 5 based on the naturalness, coherence, and task-completion capability of the system, at the end of each dialogue session.

## Baseline Agents
* A rule-based agent is provided.
* A standard RL agent (DQN model) is provided.

<!---
## Timeline
|Phase|Dates|
| ------ | -------------- |
|TBA|TBA|
|1. Development Phase|June 1 – Sept 9|
|1.1 Code (data extraction code, seq2seq baseline)|June 1|
|1.2 "Trial" data made available|June 18|
|1.3 Official training data made available| By July 1|
|2. Evaluation Phase|Sept 10 – 24|
|2.1 Test data made available|Sept 10|
 -->

## Organizers
* [Xiujun Li](https://www.microsoft.com/en-us/research/people/xiul/)
* [Sarah Panda](https://www.linkedin.com/in/sarah-panda-7345267b)
* [Jingjing Liu](https://www.microsoft.com/en-us/research/people/jingjl/)
* [Jianfeng Gao](https://www.microsoft.com/en-us/research/people/jfgao/)

## Reference
If you submit any system to this challenge or publish any other work making use of the resources provided on this project, we ask you to cite the following task description papers:

```
@article{li2018microsoft,
  title={Microsoft Dialogue Challenge: Building End-to-End Task-Completion Dialogue Systems},
  author={Li, Xiujun and Panda, Sarah and Liu, Jingjing and Gao, Jianfeng},
  journal={arXiv preprint arXiv:1807.11125},
  year={2018}
}

@article{li2016user,
  title={A User Simulator for Task-Completion Dialogues},
  author={Li, Xiujun and Lipton, Zachary C and Dhingra, Bhuwan and Li, Lihong and Gao, Jianfeng and Chen, Yun-Nung},
  journal={arXiv preprint arXiv:1612.05688},
  year={2016}
}
```

## Contact
* For questions specific to the challenge, you can contact us at <xiul@microsoft.com>.

## FQA
1. How to implement an agent: see [here](https://github.com/xiul-msr/e2e_dialog_challenge/issues/1)
