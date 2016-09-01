'''First part: Word list gen, Second part: Scene list gen each part with 8 
    trials and 12 targets and 4 lures each trial'''

from csv import DictReader
from random import choice
from random import shuffle

'''Takes a csv file, key, and value as input and returns a dictionary'''
def dict_create(file, key, value):
    f = open(file)
    r = DictReader(f)
    d={}
    for row in r:
        d[row[key]]=row[value]
    return d

'''Function takes the a dictionary, a valence for the dictionary, a number
    (words per list), and a condition and returns a list with two elements:
    a study dictionary and the corresponding test dictionary'''
def create_list(d, valence, n, condition, k, needValence):
    study=[]
    test=[]
    for i in range(0,8):
        study_d={}
        test_d={}
        m=0
        for j in range(0,n):
            '''For both the study list and test list'''
            targ_list=[]
            lure_list=[]        
            word = choice(list(d.keys()))
            if needValence:
                v = float(d.get(word))
                targ_list.append(v)
            targ_list.append(condition+'_'+valence)
            targ_list.append('Target')
            study_d[word]=targ_list
            test_d[word]=targ_list
            '''For the test list only'''
            if needValence:
                if m<k:
                    for key in d.keys():
                        v_lure= float(d.get(key))
                        if v_lure > v-.1 and v_lure < v+.1:
                            lure_list.append(v_lure)
                            lure_list.append(condition+'_'+valence)
                            lure_list.append('Lure')
                            test_d[key]=lure_list
                            m+=1
                            break
        study.append(study_d)
        test.append(test_d)
    result=[]
    result.append(study)
    result.append(test)
    return result

'''Appends the contents of the old list to the new list'''
def appender(new_list, old_list):
    for e in old_list:
        new_list.append(e)
    return new_list
    
'''Open csv files and create the pure lists for further operation'''
neg_dict = dict_create('neg_pool.csv', 'description', 'valence_mean')
neg = create_list(neg_dict,'Negative', 12, 'Pure', 3, True)
neg_study = neg[0]
neg_test = neg[1]

pos_dict = dict_create('pos_pool.csv', 'description', 'valence_mean')
pos = create_list(pos_dict, 'Positive', 12, 'Pure', 3, True)
pos_study = pos[0]
pos_test = pos[1]

neu_dict = dict_create('neu_pool.csv', 'description', 'valence_mean')
neu = create_list(neu_dict,'Neutral', 12, 'Pure', 3, True)
neu_study = neu[0]
neu_test = neu[1]

'''Creates the mixed lists'''
neg_mixed = create_list(neg_dict, 'Negative', 4, 'Mixed', 1, True)
neg_mixed_study = neg_mixed[0]
neg_mixed_test = neg_mixed[1]

pos_mixed = create_list(pos_dict, 'Positive', 4, 'Mixed', 1, True)
pos_mixed_study = pos_mixed[0]
pos_mixed_test = pos_mixed[1]

neu_mixed = create_list(neu_dict, 'Neutral', 4, 'Mixed', 1, True)
neu_mixed_study = neu_mixed[0]
neu_mixed_test = neu_mixed[1]

list_mixed_study = appender(neg_mixed_study, pos_mixed_study)
list_mixed_study = appender(list_mixed_study, neu_mixed_study)
shuffle(list_mixed_study)

list_mixed_test = appender(neg_mixed_test, pos_mixed_test)
list_mixed_test = appender(list_mixed_test, neu_mixed_test)
shuffle(list_mixed_test)

'''Open csv files and create the pure lists for the scene study'''
in_dict = dict_create('indoor.csv', 'filename', 'in_out')
ind = create_list(in_dict, 'indoor', 12, 'pure', 4, False)
in_study = ind[0]
in_test = ind[1]

out_dict = dict_create('outdoor.csv', 'filename', 'in_out')
out = create_list(out_dict, 'outdoor', 12, 'pure', 4, False)
out_study = out[0]
out_test = out[1]

'''Create the mixed lists'''
in_mixed = create_list(in_dict, 'indoor', 6, 'mixed', 2, False)
in_mixed_study = in_mixed[0]
in_mixed_test = in_mixed[1]

out_mixed = create_list(out_dict, 'outdoor', 6, 'mixed', 2, False)
out_mixed_study = out_mixed[0]
out_mixed_test = out_mixed[1]

pic_mixed_study = appender(in_mixed_study, out_mixed_study)
shuffle(pic_mixed_study)
pic_mixed_test = appender(in_mixed_test, out_mixed_test)
shuffle(pic_mixed_test)
for i in range(0,len(pic_mixed_study)):
	print(pic_mixed_study[i])