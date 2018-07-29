
"""
Created on June 7, 2016

a rule-based user simulator

@author: xiul, t-zalipt
"""

import random, copy

from debug_scripts import mis_pairs

class UserSimulator:
    """ Parent class for all user sims to inherit from """

    def __init__(self, movie_dict=None, act_set=None, slot_set=None, start_set=None, params=None):
        """ Constructor shared by all user simulators """
        
        self.movie_dict = movie_dict
        self.act_set = act_set
        self.slot_set = slot_set
        self.start_set = start_set
        
        self.max_turn = params['max_turn']
        self.slot_err_probability = params['slot_err_probability']
        self.slot_err_mode = params['slot_err_mode']
        self.intent_err_probability = params['intent_err_probability']
        

    def initialize_episode(self):
        """ Initialize a new episode (dialog)"""

        print "initialize episode called, generating goal"
        self.goal =  random.choice(self.start_set)
        self.goal['request_slots']['ticket'] = 'UNK'
        episode_over, user_action = self._sample_action()
        assert (episode_over != 1),' but we just started'
        return user_action

    def next(self, system_action):
        pass
    
    
    def set_nlg_model(self, nlg_model):
        self.nlg_model = nlg_model  
    
    def set_nlu_model(self, nlu_model):
        self.nlu_model = nlu_model
    
    
    
    def add_nl_to_action(self, user_action):
        """ Add NL to User Dia_Act """
        
        user_nlg_sentence = self.nlg_model.convert_diaact_to_nl(user_action, 'usr')
        user_action['nl'] = user_nlg_sentence
        
        if self.simulator_act_level == 1:
            #print 'original user action', user_action
            #or_usr_action = {'diaact':user_action['diaact'], 'request_slots':user_action['request_slots'], 'inform_slots':user_action['inform_slots'], 'nl':user_action['nl']}
            
            user_nlu_res = self.nlu_model.generate_dia_act(user_action['nl']) # NLU
            if user_nlu_res != None:
                #user_nlu_res['diaact'] = user_action['diaact'] # or not?
                user_action.update(user_nlu_res)
            
            # debug  
            #if or_usr_action['diaact'] == user_nlu_res['diaact'] and or_usr_action['inform_slots'].keys() == user_nlu_res['inform_slots'].keys() \
            #    and or_usr_action['request_slots'].keys() == user_nlu_res['request_slots'].keys():
            #    pass
            #else:
                #print 'usr_nlu_res', user_nlu_res
            #    if or_usr_action not in mis_pairs: 
            #        mis_pair = {'or_act': copy.deepcopy(or_usr_action), 'nlu_act': copy.deepcopy(user_nlu_res)}
            #        mis_pairs.append(mis_pair)