#==========================================================================
# PROGRAM:... ....... Lab 02 - Coding Practice
# AUTHOR:............ Phan, Anna
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
#==========================================================================
from collections import Counter
import csv

input_file = open('bird_observations_large.txt', 'r')

birds_list = []

for line in input_file:
    birds_list.append(line)

c = Counter(birds_list)

with open('count_birds_large.csv','w', newline='') as csvfile:
    fieldnames = ['species', 'count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for bird, count in sorted(c.items()):
        writer.writerow([bird, count])

#How do I get rid of the extra quotes?