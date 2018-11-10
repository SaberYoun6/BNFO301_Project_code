from __future__ import division
__author__ = 'NR'
'''
Perform permutation test on AML/ALL gene expression data
'''

import csv
from math import sqrt
from random import shuffle
import matplotlib.pyplot as plt

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

def plot_t_values(simulated_t_values, t_obs):
    plt.hist(simulated_t_values, bins=100)
    plt.axvline(x=t_obs, color='red')
    plt.title("Distribution of simulated t values")
    plt.xlabel("t")
    plt.ylabel("Frequency")
    plt.text(t_obs, 25, "<-- observed t")
    plt.show()


################
# MAIN PROGRAM #
################
dynamic_shuffle=[]
# read in data and get diagnosis indices
true_labels = get_labels_from_file('leukemia_big.csv')
genes = get_expression_from_csv('leukemia_big.csv')
ALL = get_diagnosis_columns('ALL', true_labels)
AML = get_diagnosis_columns('AML', true_labels)
pvals = []
tob=[]
tails= 1.994 ## Fundamental of Statistics by Micheal Sullivan III, on A-12 .05 0r .025  
for gene in genes:
    sim_t_val = []  # Store the simulated t values here.
    repeat_num = 1000  # The number of times labels should be shuffled and simulated t value calculates should happen.
    t_obs = get_test_statistic(gene, ALL, AML)  # Calculate the true t value for the gene
    tob.append(t_obs)
    ## FILL IN THE REST ##
    counts=0
    for increment in range(repeat_num):
        shuffled_label = shuffle_diagnosis_labels(true_labels)
        sALL=get_diagnosis_columns('ALL', shuffled_label)
        sAML=get_diagnosis_columns('AML', shuffled_label)
        t_sim=get_test_statistic(gene,sALL,sAML)
        sim_t_val.append(t_sim)
        if   abs(t_sim) > abs(t_obs):
          counts+=1
    pvals.append(counts/1000)
c=0
for i in pvals:
     if i < .05:
       c+=1
print("The number of genes with a permuation test p-value less than .05 is %i" % c)
print("The length of pvals is %i" % len(pvals))
plot_t_values(sim_t_val[0:1000],tob[0])
#print(sim_t_val[1:1000])
cv=0
for it in tob:
    if abs(it) < tails :
        cv+=1
print("The number of genes with a t-test pvalue less than 0.05 is %i\n" % cv )
print("A p-value is the chance of any event occuring within the range of a null hyptothesis, to see if the test is statistical reletvant.")

