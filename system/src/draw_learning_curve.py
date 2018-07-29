'''
Created on Nov 3, 2016

draw a learning curve

@author: xiul
'''

import argparse, json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="darkgrid")
sns.set(font_scale=1.6)

width = 8
height = 5.8
plt.figure(figsize=(width, height))

linewidth=1.1

colors = ['#2f79c0', '#278b18', '#ff5186', '#8660a4', '#D49E0F', '#a8d40f']


def read_success_rate_records(path):
    """ load the performance score (.json) file """
    
    success_rate = []
    data = json.load(open(path, 'rb'))
    for key in sorted(data['success_rate'].keys(), key=lambda k:int(k)):
        # print key
        if int(key) > -1:
            success_rate.append(data['success_rate'][key])
            # print("%s\t%s\t%s\t%s" % (key, data['success_rate'][key], data['ave_turns'][key], data['ave_reward'][key]))

    smooth_num = 1
    d = [success_rate[i*smooth_num:i*smooth_num + smooth_num] for i in xrange(len(success_rate)/smooth_num)]

    success_rate_new = []
    cache = 0
    alpha = 0.9
    for i in d:
        cur = sum(i)/float(smooth_num)
        cache = cache * alpha + (1 - alpha) * cur
        success_rate_new.append(cache)

    return success_rate_new


def read_performance_records(path):
    """ load the performance score (.json) file """
    
    data = json.load(open(path, 'rb'))
    for key in data['success_rate'].keys():
        if int(key) > -1:
            print("%s\t%s\t%s\t%s" % (key, data['success_rate'][key], data['ave_turns'][key], data['ave_reward'][key]))
            
def load_performance_file(path):
    """ load the performance score (.json) file """
    
    data = json.load(open(path, 'rb'))
    numbers = {'x': [], 'success_rate':[], 'ave_turns':[], 'ave_rewards':[]}
    keylist = [int(key) for key in data['success_rate'].keys()]
    keylist.sort()
    
    cache = 0
    alpha = 0.9
    
    for key in keylist:
        if int(key) > -1:
            cur = data['success_rate'][str(key)]
            cache = cache * alpha + (1 - alpha) * cur
            
            numbers['x'].append(int(key))
            numbers['success_rate'].append(cache)
            numbers['ave_turns'].append(data['ave_turns'][str(key)])
            numbers['ave_rewards'].append(data['ave_reward'][str(key)])
    return numbers

def draw_learning_curve(numbers):
    """ draw the learning curve """
    
    plt.xlabel('Simulation Epoch')
    plt.ylabel('Success Rate')
    plt.title('Learning Curve')
    plt.grid(True)

    plt.plot(numbers['x'], numbers['success_rate'], 'r', lw=1)
    plt.show()
    

""" draw restaurant curves """            
def end_to_end_curve_restaurant(params):
    """ Restaurant domain """
    
    global_idx = 500
    datapoint = []
    draw_list = range(1, 2)
    # draw_list = [6]
    for i in draw_list:
        datapoint.append(read_success_rate_records('./deep_dialog/checkpoints/restaurant/nl/dqn/agt_12_performance_records.json'))
    min_len = min(len(i) for i in datapoint)
    #print [len(i) for i in datapoint]
    
    data_1 = np.asarray([i[0:min_len] for i in datapoint])
    mean_1 = np.mean(data_1,axis=0)
    var_1 = np.std(data_1,axis=0)
    
    #idx = min(mean_1.shape[0], global_idx)
    #l1, = plt.plot(range(idx),mean[0:idx],colors[2], label='DQN', linewidth=linewidth)
    #plt.fill_between(range(mean.shape[0]), mean+var/2, mean-var/2, facecolor=colors[2], alpha=0.2)
        
    max_x = min(min_len, global_idx)
    folders = 1
    
    #success_1 = []
    success_2 = []
    success_3 = []
    for i in xrange(folders):
        #success_1.append([0]*max_x)
        success_2.append([0]*max_x)
        success_3.append([0]*max_x)
    
    for key in range(max_x):
        for i in xrange(folders):
            #success_1[i][key] = data_1[i]['success_rate'][key]
            success_2[i][key] = 0.1284
            success_3[i][key] = 0.478
    
    #data_1 = np.asarray(success_1)
    #mean_1 = np.mean(data_1, axis=0)
    #var_1 = np.std(data_1, axis=0)
    
    data_2 = np.asarray(success_2)
    mean_2 = np.mean(data_2, axis=0)
    var_2 = np.std(data_2, axis=0)
    
    data_3 = np.asarray(success_3)
    mean_3 = np.mean(data_3, axis=0)
    var_3 = np.std(data_3, axis=0)
    
    l1, = plt.plot(range(mean_1.shape[0]), mean_1, linewidth=1.0, color=colors[0])
    plt.fill_between(range(mean_1.shape[0]), mean_1+var_1, mean_1-var_1, facecolor=colors[0], edgecolor='none', alpha=0.2)
    
    l2, = plt.plot(range(mean_2.shape[0]), mean_2, linewidth=1.0, color=colors[1])
    plt.fill_between(range(mean_2.shape[0]), mean_2+var_2, mean_2-var_2, facecolor=colors[1], edgecolor='none', alpha=0.2)
    
    l3, = plt.plot(range(mean_3.shape[0]), mean_3, linewidth=1.0, color=colors[2])
    plt.fill_between(range(mean_3.shape[0]), mean_3+var_3, mean_3-var_3, facecolor=colors[2], edgecolor='none', alpha=0.2)
    
    sns.set_style("dark")
    
    plt.ylabel('Success Rate', fontsize=14)
    plt.xlabel('Simulation Epoch', fontsize=14)
    plt.axis((0, max_x, 0, 0.6))
    #plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=13)
    plt.xticks([0, 100, 200, 300, 400, 500], [0, 100, 200, 300, 400, 500], fontsize=13)
    plt.legend([l1, l2, l3], ['RL Agent', 'Rule Agent', 'Upper Bound'], loc=4, fontsize=13) #loc=(0.9, 0.16))
    #plt.title('Learning curves')
    plt.grid(True)
    
    plt.show()
    
""" draw taxi curves """            
def end_to_end_curve_taxi(params):
    """ Taxi domain """
    
    global_idx = 500
    datapoint = []
    draw_list = range(1, 2)
    # draw_list = [6]
    for i in draw_list:
        datapoint.append(read_success_rate_records('./deep_dialog/checkpoints/taxi/non_nl/dqn/agt_13_performance_records.json'))
    min_len = min(len(i) for i in datapoint)
    #print [len(i) for i in datapoint]
    
    data_1 = np.asarray([i[0:min_len] for i in datapoint])
    mean_1 = np.mean(data_1, axis=0)
    var_1 = np.std(data_1, axis=0)
    #idx = min(mean_1.shape[0], global_idx)
    #l1, = plt.plot(range(idx),mean[0:idx],colors[2], label='DQN', linewidth=linewidth)
    #plt.fill_between(range(mean.shape[0]), mean+var/2, mean-var/2, facecolor=colors[2], alpha=0.2)
    
    max_x = min(min_len, global_idx) #min_len
    folders = 1
    
    #success_1 = []
    success_2 = []
    success_3 = []
    for i in xrange(folders):
        #success_1.append([0]*max_x)
        success_2.append([0]*max_x)
        success_3.append([0]*max_x)
    
    for key in range(max_x):
        for i in xrange(folders):
            #success_1[i][key] = data_1[i]['success_rate'][key]
            success_2[i][key] = 0.1226
            success_3[i][key] = 0.4622
    
    #data_1 = np.asarray(success_1)
    #mean_1 = np.mean(data_1, axis=0)
    #var_1 = np.std(data_1, axis=0)
    
    data_2 = np.asarray(success_2)
    mean_2 = np.mean(data_2, axis=0)
    var_2 = np.std(data_2, axis=0)
    
    data_3 = np.asarray(success_3)
    mean_3 = np.mean(data_3, axis=0)
    var_3 = np.std(data_3, axis=0)
    
    l1, = plt.plot(range(mean_1.shape[0]), mean_1, linewidth=1.0, color=colors[0])
    plt.fill_between(range(mean_1.shape[0]), mean_1+var_1, mean_1-var_1, facecolor=colors[0], edgecolor='none', alpha=0.2)
    
    l2, = plt.plot(range(mean_2.shape[0]), mean_2, linewidth=1.0, color=colors[1])
    plt.fill_between(range(mean_2.shape[0]), mean_2+var_2, mean_2-var_2, facecolor=colors[1], edgecolor='none', alpha=0.2)
    
    l3, = plt.plot(range(mean_3.shape[0]), mean_3, linewidth=1.0, color=colors[2])
    plt.fill_between(range(mean_3.shape[0]), mean_3+var_3, mean_3-var_3, facecolor=colors[2], edgecolor='none', alpha=0.2)
    
    sns.set_style("dark")
    
    plt.ylabel('Success Rate', fontsize=14)
    plt.xlabel('Simulation Epoch', fontsize=14)
    plt.axis((0, max_x, 0, 0.6))
    #plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=13)
    plt.xticks([0, 100, 200, 300, 400, 500], [0, 100, 200, 300, 400, 500], fontsize=13)
    plt.legend([l1, l2, l3], ['RL Agent', 'Rule Agent', 'Upper Bound'], loc=4, fontsize=13) #loc=(0.9, 0.16))
    #plt.title('Learning curves')
    plt.grid(True)
    
    plt.show()    
     

 
def main(params):
    cmd = params['cmd']
    
    if cmd == 0:
        numbers = load_performance_file(params['result_file'])
        draw_learning_curve(numbers)
    elif cmd == 1:
        read_performance_records(params['result_file'])
    elif cmd == 2: # restaurant domain
        end_to_end_curve_restaurant(params)
    elif cmd == 3: # taxi domain
        end_to_end_curve_taxi(params)
    elif cmd == 4:
        pass
    elif cmd == 5:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--cmd', dest='cmd', type=int, default=1, help='cmd')
    
    parser.add_argument('--result_file', dest='result_file', type=str, default='./deep_dialog/checkpoints/rl_agent/11142016/noe2e/agt_9_performance_records.json', help='path to the result file')
    
    args = parser.parse_args()
    params = vars(args)
    print json.dumps(params, indent=2)

    main(params)