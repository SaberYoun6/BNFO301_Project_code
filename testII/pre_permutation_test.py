#!/usr/bin/env python
__author__ = 'NR'
__author__= 'Samuel Young'
'''
Perform permutation test on AML/ALL gene expression data
'''
import time
import csv
from math import sqrt,fabs
from random import shuffle
import random  as rd
import matplotlib.pyplot as plt
import numpy as npy
########################
# Function Definitions #
########################

def get_diagnosis_columns(diag, header):
    '''get list of indices corresponding to given diagnosis in header line
    '''
    return [index for index, value in enumerate(header) if diag == value]

def get_labels_from_file(infile):
    '''Get diagnoses from header line in csv file
    '''
    with open(infile) as f:
        header_line = next(f)  # Get the first line in the file
        header_line = header_line.strip()  # line contains white characters that need to be stripped first
        diagnoses = header_line.split(',')  # contains diagnosis labels.
        return diagnoses

def get_expression_from_csv(infile):
    '''get expression data from csv. **Uses csv packages**. Returns a 2D list'''
    with open(infile) as f:
        next(f)  # skip the first line
        lines = [line for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                                             quotechar='"')]  # read in data using csv package
    return lines

def get_diagnosis_columns(diag, header):
    '''get list of indices corresponding to given diagnosis in header line'''
    return [index for index, value in enumerate(header) if diag == value]

def mean(values):
    ''' Calculate the mean of a sequence of numbers'''
    return float(sum(values)) / len(values)

def sample_variance(values):
    ''' Calculate the sample variance'''
    sample_mean = mean(values)
    return sum([(value - sample_mean) ** 2 for value in values]) / (len(values) - 1)

def get_test_statistic(x, sample1, sample2):
    '''Calculates a two sample test statistic. Assumes unequal sample variances.
    Sample1 and Sample2 are the indices that correspond each sample'''
    x_1 = [x[i] for i in sample1]
    x_2 = [x[j] for j in sample2]
    difference_in_means = mean(x_1) - mean(x_2)
    denominator = sqrt((sample_variance(x_1) / len(x_1)) + (sample_variance(x_2) / len(x_2)))
    return difference_in_means / denominator

def shuffle_diagnosis_labels(diagnosis_list):
    '''shuffle a list of diagnosis lists. Returns a list of the same
    length as the input list'''
    # NOTE: shuffle works in place and returns None. Because of this,
    # you have to duplicate the diagnosis list then shuffle.
    new_list = diagnosis_list[:]  # duplicate diagnosis list. Why do you think there's a slice operator in the expression?
    shuffle(new_list)  # shuffle the new list
    return new_list
#def get_sample_variance(x):
#    var=sum(x-get_x_bar(x))**2/len(x)-1
#    return var
#def get_x_bar(x):
#    xbar=sum(x)/len(x)
#    return xbar
#def get_number(x):
#    number=len(x)
#    return number
#def obtain_t_test(xbar_1,xbar_2,vari_1,var_2,numb_1,numb_2):
#    true_xbar=xbar_1-xbar_2
#    true_vari= math.sqrt((vari_1**2/numb_1),+(var_2**2/numb_2))
#    true_t_test= true_xbar/true_vari
#    return true_t_test
def truffle_shuffle(dict_rand_shuf):
    equipment=[]
    for i, c in enumerate(dict_rand_shuf):
           equipment.append(mean(dict_rand_shuf[c]))
    return equipment
################
# MAIN PROGRAM #
################

# read in data and get diagnosis indices
true_labels =  get_labels_from_file('leukemia_big.csv')
genes = get_expression_from_csv('leukemia_big.csv')
ALL = get_diagnosis_columns('ALL', true_labels)
AML = get_diagnosis_columns('AML', true_labels)
i=0
incr=0
x = genes[0]
intial_value = get_test_statistic(x,ALL,AML) 
new_value= float(intial_value)
print(new_value)
#print(x)
t_test = []
for seq in genes:
    all_genes=get_test_statistic(seq,ALL,AML)
    all_genes=float(all_genes)
#    print(type(all_genes))
#    print(type(new_value))
    if all_genes >= intial_value or all_genes <= intial_value:
       t_test.append(all_genes)
       the_mean=mean(t_test)
       

print(the_mean)


        
        
dynamic_shuffle = []
dynamical_shuffle = []
comparison_shuffle = []
comparison_AML = []
temp_list=[]
foo= []
tup=()
truth_label=[]
semi_sorted_dict={}
dict_rand_shuf={}
#dynamical_shuf=get_test_statistic(x,sALL,sAML)
#print(dynamical_shuf)
#print(intial_value)
for seq in genes:
    for increment in range(1000):
        shuffled_label = shuffle_diagnosis_labels(true_labels)
        sALL=get_diagnosis_columns('ALL', shuffled_label)
        sAML=get_diagnosis_columns('AML', shuffled_label)
        dynamical_shuf=get_test_statistic(seq,sALL,sAML)
        if dynamical_shuf >= the_mean or dynamical_shuf <= the_mean:
            dynamic_shuffle.append(dynamical_shuf)
for i in range(0,len(dynamic_shuffle),1000):
    temp_list.append(mean(dynamic_shuffle[i:i+1000]))
    mean_true_list=mean(temp_list)
    foo.append(dynamic_shuffle[i:i+1000])
print(mean_true_list)
print(abs(mean_true_list))
if  intial_value > 1+mean_true_list or intial_value < abs(1+mean_true_list):
    comparison_shuffle.append(intial_value)
print(comparison_shuffle)
'''
for c,v in enumerate(genes):
##        print(type(c))
        all_genes_s=get_test_statistic(genes[c],sALL,sAML)
        all_genes_s=float(all_genes_s)
        if all_genes_s >= the_mean or all_genes_s <= the_mean:
             dynamic_shuffle.append(all_genes_s)
        tup=((dynamic_shuffle))
        dict_rand_shuf[c]=tup
print(truffle_shuffle(dict_rand_shuf))
'''
#            dict_rand_shuf[inc]=dynamic_shuffle
#            print( dict_rand_shuf[inc])
#print(generation_x)
#print(abs(generation_x))
#print(new_foo)
'''
for k,v in dict_rand_shuf.items():
    print ("keys: %d "  % k)
    print("value: " + str(v) )
print (comparsion_shuffle,bins='auto',range=(0,4),density=True)#normed=True doesn't work
plt.xlabel("t-test of randomized  genes")
plt.ylabel("probability of gene")
plt.title(" Histogram of genes")
plt.grid(True)
plt.show()
'''




