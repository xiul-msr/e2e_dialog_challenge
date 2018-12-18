# SLT 2018 Special Session - Microsoft Dialogue Challenge: Building End-to-End Task-Completion Dialogue Systems

## Schedule: Dec. 18, 2018, 1PM - 5PM,  [Olympia Plenary Room](http://www.slt2018.org/technical-programme/)
1.  1:00 - 1:10PM Jianfeng Gao: opening<br/>
2.  1:10 – 1:40PM Gokhan Tur (Uber): "Past, Present, and Future of Conversational AI" ([slides](/slides/Uber_SLT_2018_Gokhan_Tur.pdf))<br/>
3.  1:40 – 2:10PM Minlie Huang (Tsinghua): "Towards Building More Intelligent Conversational System: Semantics, Consistency & Interactiveness" ([slides](./slides/2018-SLT-Tsinghua-MinlieHuang.pptx))<br/>
4.  2:10 – 2:40PM Vivian Chen (NTU): "Towards Open-Domain Conversational AI" ([slides](./slides/181217_SLT-MSChallenge_Vivian.pptx))<br/>
5.  2:40 – 3:00PM break<br/>
6.  3:00 – 3:20PM Sungjin Lee (MSR): "MS dialogue challenge: result and outlook" ([slides](./slides/MS_dialog_challenge_result_outlook_sungjin.pptx))<br/>
7.  3:20 – 3:35PM Oral presentation 1 by Sihong Liu - "Universe Model: A Human-like User Simulator Based on Dialogue Context" ([slides](./slides/Oral_ppt_sihong_liu.pptx))<br/>
8.  3:35 – 3:50PM Oral presentation 2 by Yu-An Wang - "Double dueling Agent for Dialogue Policy Learning" ([slides](./slides/Oral_slides_yu-an_wang.pptx))<br/>
9.  3:50 – 4:30PM Panel discussion (chaired by Jianfeng Gao): 45mins, Panelist:<br/>
    - Alex Acero (Apple)<br/>
    - Vivian Chen (NTU)<br/>
    - Minlie Huang (Tsinghua)<br/>
    - Sungjin Lee (MSR)<br/>
    - Spyros Matsoukas (Amazon)<br/>
    - Gokhan Tur (Uber)<br/>


## News
- [ ] 12/18/2018 – 12/21/2018: [SLT Workshop](http://www.slt2018.org/news/)<br/>
      Dec. 18, 1:00PM - 3:30PM: Invited talks: 1hr, Speakers: <br/>
        - Sungjin Lee (MSR) - "MS dialogue challenge: result and outlook"<br/>
        - Vivian Chen (NTU) - "Towards Open-Domain Conversational AI"<br/>
        - Minlie Huang (Tsinghua) - "Towards Building More Intelligent Dialogue Systems: Semantics, Consistency, and Interactiveness"<br/> 
        - Gokhan Tur (Uber) - "Past, Present, and Future of Conversational AI"<br/>
        - Oral presentation: Sihong Liu - "Universe Model: A Human-like User Simulator Based on Dialogue Context"<br/>
        - Oral presentation: Yu-An Wang - "Double dueling Agent for Dialogue Policy Learning"<br/>
      Dec. 18, 3:30PM - 4:30PM: Panel discussion (chaired by Jianfeng Gao): 45mins, Panelist: <br/>
        - Alex Acero (Apple)<br/>
        - Vivian Chen (NTU)<br/>
        - Minlie Huang (Tsinghua)<br/>
        - Sungjin Lee (MSR)<br/>
        - Spyros Matsoukas (Amazon)<br/>
        - Gokhan Tur (Uber)<br/>
- [x] 11/25/2018: Paper acceptance announcement.
- [x] 11/09/2018: Paper submission. [Call for Papers](https://github.com/xiul-msr/e2e_dialog_challenge/blob/master/SLT%202018%20-%20MS%20Dialogue%20Challenge%20-%20CFP.pdf).
- [x] 11/08/2018: [Results](https://xiul-msr.github.io/e2e_dialog_challenge/board/leaderboard) (including human evaluation) Announced.
- [x] 10/25/2018: System submission (https://msrprograms.cloudapp.net/MDC2018)
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

## System Submission Guidelines

Open an account in https://msrprograms.cloudapp.net/MDC2018 and create a submission with an abstract and code in the form of zip file(<100MB), trained agent model, and also NLU and NLG models if applicable. Include instructions for execution as below. Submission can be updated without limit no later than 10/14/2018 11:59 PM PST. 

Instructions to run the sample submission in the SubmissionSample folder.
1.	Extract run.zip file (Zip the contents of system/src into run.zip) 
2.	Run testrun.py to interact with the agent as below example. 

      > python testrun.py --agt 0 --usr 1 --max_turn 40 --kb_path ./run/deep_dialog/data_movie/movie.kb.1k.v1.p --goal_file_path ./run/deep_dialog/data_movie/user_goals_first.v2.p --slot_set ./run/deep_dialog/data_movie/slot_set.txt --act_set ./run/deep_dialog/data_movie/dia_acts.txt --dict_path ./run/deep_dialog/data_movie/slot_dict.v1.p --nlg_model_path ./run/deep_dialog/models/nlg/movie/lstm_tanh_[1533529279.91]_87_99_199_0.988.p --nlu_model_path ./run/deep_dialog/models/nlu/movie/lstm_[1533588045.3]_38_38_240_0.998.p --diaact_nl_pairs ./run/deep_dialog/data_movie/dia_act_nl_pairs.v7.json --intent_err_prob 0.00 --slot_err_prob 0.00 --episodes 500 --act_level 0 --run_mode 0 --cmd_input_mode 0

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
* [Yu Wang](https://www.linkedin.com/in/yu-wang-a95b2b1)
* [Siqi Sun](https://www.linkedin.com/in/siqi-sun)
* [Sarah Panda](https://www.linkedin.com/in/sarah-panda-7345267b)
* [Jingjing Liu](https://www.microsoft.com/en-us/research/people/jingjl/)
* [Jianfeng Gao](https://www.microsoft.com/en-us/research/people/jfgao/)
* [Hao Fang](https://www.linkedin.com/in/hao-fang-99778b25)

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
