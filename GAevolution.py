# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd
import random
import copy
import numpy as np

########################################################### 
#step0. input data
generation = 2
past_generation = generation-1
population = 20
selection_type = 1
crossover_type = 5
elite = 4
crossover = 12
mutation = 4

list_gen=['gen{:}'.format(past_generation)]
list_chromos=[]
for i in range(population):
    list_chromos.append('chromo{:}'.format(i+1))



try:
    file_path = '../data/gen{:}_chromo_information.txt'.format(past_generation)
    file_open = open(file_path, 'r', encoding='utf-8')
except FileNotFoundError:
    print(f"{file_path} not found :")        
else:
    past_gen_chromo_data=[ __ for __ in range(population)]  
    with open(file_path, 'r', encoding='utf-8') as fr:
        with open('chromo_information.py', 'w', encoding='utf-8') as py_file:
                py_file.write("def chromos_information():\n\t")
                py_file.write("past_chromos=[\n")
                data = fr.readlines()[:population]
                c=0
                for line in data:
                    a=line.split()
                    #print(a)
                    past_gen_chromo_data[c]=a
                    c += 1
                
                for p in range(population):
                    joined_data = " ".join(past_gen_chromo_data[p])
                    py_file.write(joined_data)
                    py_file.write('\n')
                
                py_file.write("]\n")
                py_file.write("\t")
                py_file.write("return past_chromos\n")
                py_file.write("chromos = chromos_information()")
    
    chromos = [[0 for __ in range(6)] for __ in range(population)]
    import chromo_information as file
    file.chromos_information()
    chromos = file.chromos_information()


##########################################################
#step2. b_GA_Ranking.py
##########################################################
key_data = pd.read_csv('../data/gen1_6value.txt', sep='\t',index_col=0)
sort_chromos=[[0 for __ in range(6)] for __ in range(population)]
chromos_Redot = [[0 for __ in range(2)] for __ in range(population)]
sort_Redot    = [[0 for __ in range(2)] for __ in range(population)]

def ranking(population,key_data,chromos_Redot,sort_Redot,chromos):
    for path_chromos in range(0,len(list_chromos),1):
        chromos_Redot[path_chromos][0] = path_chromos + 1
        chromos_Redot[path_chromos][1] = np.round(key_data['Redox potential (b3lyp, V)'][path_chromos],3)
        print("Redox potential (V) of chromo", chromos_Redot[path_chromos][0] ," : ", chromos_Redot[path_chromos][1]) 


    sort_Redot = sorted(chromos_Redot, key=lambda chromos_Redot: chromos_Redot[1],reverse=True)
    
    print("=============================")
    for path_chromos in range(0,len(list_chromos),1):
        print("Ranking",path_chromos+1, ": Chromo", sort_Redot[path_chromos][0])
    print("=============================")

    for i in range(population):
        number = int(sort_Redot[i][0]) - 1
        sort_chromos[i]=copy.deepcopy(chromos[number])

    return sort_Redot

sort_Redot=ranking(population,key_data,chromos_Redot,sort_Redot,chromos)

#Evolution
new_chromos=[[0 for __ in range(6)] for __ in range(population)]

#Elitism Selction
for i in range(elite):
    new_chromos[i] = copy.deepcopy(sort_chromos[i])

sample=[]
for i in range(1,101):
    sample.append(i)
rank_random=random.sample(sample,2)
def crossover_rank_select(n,sort_chromos):
    crossover_select_chromo = []
    crossover_select_number = 0
    if n in range(1,10):  
        crossover_select_chromo = sort_chromos[0]
        crossover_select_number = 1        
    elif n in range(10,19): #chromo2 : 0.09
        crossover_select_chromo = sort_chromos[1]
        crossover_select_number = 2         
    elif n in range(19,28): #chromo3 : 0.09
        crossover_select_chromo = sort_chromos[2]
        crossover_select_number = 3
    elif n in range(28,37): #chromo4 : 0.09
        crossover_select_chromo = sort_chromos[3]
        crossover_select_number = 4        
    elif n in range(37,44): #chromo5 : 0.07
        crossover_select_chromo = sort_chromos[4]
        crossover_select_number = 5           
    elif n in range(44,51): #chromo6 : 0.07
        crossover_select_chromo = sort_chromos[5]
        crossover_select_number = 6
    elif n in range(51,58): #chromo7 : 0.07
        crossover_select_chromo = sort_chromos[6]
        crossover_select_number = 7
    elif n in range(58,65): #chromo8 : 0.07
        crossover_select_chromo = sort_chromos[7]
        crossover_select_number = 8
    elif n in range(65,70): #chromo9 : 0.05
        crossover_select_chromo = sort_chromos[8]
        crossover_select_number = 9
    elif n in range(70,75): #chromo10 : 0.05
        crossover_select_chromo = sort_chromos[9]
        crossover_select_number = 10
    elif n in range(75,80): #chromo11 : 0.05
        crossover_select_chromo = sort_chromos[10]
        crossover_select_number = 11
    elif n in range(80,85): #chromo12 : 0.05
        crossover_select_chromo = sort_chromos[11]
        crossover_select_number = 12        
    elif n in range(85,88): #chromo13 : 0.03
        crossover_select_chromo = sort_chromos[12]
        crossover_select_number = 13
    elif n in range(88,91): #chromo14 : 0.03
        crossover_select_chromo = sort_chromos[13]
        crossover_select_number = 14
    elif n in range(91,94): #chromo15 : 0.03
        crossover_select_chromo = sort_chromos[14]
        crossover_select_number = 15
    elif n in range(94,97): #chromo16 : 0.03
        crossover_select_chromo = sort_chromos[15]
        crossover_select_number = 16
    elif n in range(97,98): #chromo17 : 0.01
        crossover_select_chromo = sort_chromos[16]
        crossover_select_number = 17
    elif n in range(98,99): #chromo18 : 0.01
        crossover_select_chromo = sort_chromos[17]
        crossover_select_number = 18
    elif n in range(99,100): #chromo19 : 0.01
        crossover_select_chromo = sort_chromos[18]
        crossover_select_number = 19        
    elif n in range(100,101): #chromo20 : 0.01
        crossover_select_chromo = sort_chromos[19]
        crossover_select_number = 20
    return crossover_select_chromo, crossover_select_number
        
where_crossover=[[t for __ in range(2)] for t in range(crossover//2)]
def crossover_rank(elite,crossover,crossover_type,sort_chromos,i,where_crossover):
    crossover_before_chromo1 = []
    crossover_before_chromo2 = []
    crossover_select_number1 = 0
    crossover_select_number2 = 0    
    crossover_after_chromo1=[0,0,0,0,0,0]
    crossover_after_chromo2=[0,0,0,0,0,0]
        
    def crossover_penta_play(crossover_before_chromo1,crossover_before_chromo2,crossover_after_chromo1,crossover_after_chromo2):
        crossover_after_chromo1[::2]=copy.deepcopy(crossover_before_chromo1[::2])
        crossover_after_chromo1[1::2]=copy.deepcopy(crossover_before_chromo2[1::2])
        crossover_after_chromo2[::2]=copy.deepcopy(crossover_before_chromo2[::2])
        crossover_after_chromo2[1::2]=copy.deepcopy(crossover_before_chromo1[1::2])
                    
    while True: 
        rank_random=random.sample(sample,2)
        crossover_before_chromo1,crossover_select_number1 = crossover_rank_select(rank_random[0],sort_chromos)
        crossover_before_chromo2,crossover_select_number2 = crossover_rank_select(rank_random[1],sort_chromos)
        
        if crossover_before_chromo1 == crossover_before_chromo2:
            rank_random=random.sample(sample,2)
            crossover_before_chromo1,crossover_select_number1 = crossover_rank_select(rank_random[0],sort_chromos)
            crossover_before_chromo2,crossover_select_number2 = crossover_rank_select(rank_random[1],sort_chromos)
            
        crossover_penta_play(crossover_before_chromo1,crossover_before_chromo2,crossover_after_chromo1,crossover_after_chromo2)
            
        where_crossover[i//2][0]=crossover_select_number1
        where_crossover[i//2][1]=crossover_select_number2
        break
    
    new_chromos[elite+i] = copy.deepcopy(crossover_after_chromo1)
    new_chromos[elite+i+1] = copy.deepcopy(crossover_after_chromo2)
    
    return where_crossover

#Crossover
for i in range(0,crossover-1,2):
    where_crossover=crossover_rank(elite,crossover,crossover_type,sort_chromos,i,where_crossover)

##################################################################
#3. mutation
#3-a. Replacement Mutation

def mutation_play(elite,crossover,mutation,sort_chromos,new_chromos):
    for i in range(mutation):
        for j in range(6):
            new_chromos[i+elite+crossover][j] = random.randint(1,30)
                
mutation_play(elite,crossover,mutation,sort_chromos,new_chromos)


chromos = new_chromos
#GA
list_gen=['gen{:}'.format(generation)]
list_chromos=[]
for i in range(population):
    list_chromos.append('chromo{:}'.format(i+1))

os.makedirs('../results/gen{:}'.format(generation), exist_ok=True)


########################################################################
#step3.xyz(new generation)
########################################################################
print("Done!!")
#######################################
def chromos_information():
    past_chromos = [[0 for __ in range(6)] for __ in range(population)]
    for i in range(population):
        #print(new_chromos[i],", #chromo",i+1)
        past_chromos[i]=new_chromos[i]
        print(past_chromos[i],", #chromo",i+1)
    
    return past_chromos

chromos_information()
#######################################

past_gen='gen{}_'.format(generation-1)
gen='gen{}_'.format(generation)
title='chromo_information'
        
with open( '../data/' + gen + title + '.txt', 'w') as txt_file:    
    for i in range(population):
        txt_file.write(str(new_chromos[i]))
        txt_file.write(", #gen")
        txt_file.write(str(generation))
        txt_file.write("_chromo")
        txt_file.write(str(i+1))
        txt_file.write('\n')


def data_xyz(chromos,i):
    s1 = [0,
        'B','N','P',
        'C','C','C','C',
        'C','C','C','C','C','C','C','C',
        'C','C','C','C','C','C','C','C','C','C','C','C',
        'C','C','C',
         ] 
    s2 = [0,
        0,0,0,
        'H','F','CL','C',
        'O','S','N','N','N','N','N','O',
        'C','B','N','N','P','C','N','C','N','N','C','N',
        'B','C','N',
         ] 
    s3_L_H = [0,
        0,0,0,
        0,0,0,0,
        0,0,0,0,0,0,0,0,
        'H','H','H',0,'H',0,'H','H','H','H',0,'H',
        0,0,0,
        ]
    s3_L_notH = [0,
        0,0,0,
        0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,'O',0,'O',0,0,0,0,'O',0,
        'O','C','C',
        ]
    s3_R_H = [0,
        0,0,0,
        0,0,0,0,
        'H','H',0,0,0,0,0,0,
        0,'H','H',0,'H',0,0,0,0,0,0,0,
        0,0,0,
        ]
    s3_R_notH = [0,
        0,0,0,
        0,0,0,0,
        0,0,'C','C','N','C','C','C',
        'O',0,0,'O',0,'O','O','C','C','C','O','C',
        'O','N','C',
        ]
    s4_R_M = [0,
        0,0,0,
        0,0,0,0,
        0,0,'O','S','H','N',0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,
        ]  
    s4_R_T = [0,
        0,0,0,
        0,0,0,0,
        0,0,0,0,0,0,'H',0,
        0,0,0,0,0,'H','H','H','O','S',0,'O',
        0,'H',0,
        ]
    s4_R_B = [0,
        0,0,0,
        0,0,0,0,
        0,0,0,0,0,0,'H',0,
        0,0,0,0,0,0,0,'H','H','H','C','N',
        0,'H',0,
        ]
    
    count_row = 0
        
    parameter_1 = []
    parameter_2 = []
    parameter_3 = []
    parameter_4 = []
    parameter_5 = []
    parameter_6 = []
            
    gene_number_1 = chromos[i][0]
    gene_number_2 = chromos[i][1]
    gene_number_3 = chromos[i][2]
    gene_number_4 = chromos[i][3]
    gene_number_5 = chromos[i][4]
    gene_number_6 = chromos[i][5]
    
    parameter_s1_1=('''{:}	1.021200 	-0.950300 	0.000100''').format(s1[gene_number_1])
    parameter_s1_2=('''{:}	-0.312100 	-1.359900 	0.000400''').format(s1[gene_number_2])
    parameter_s1_3=('''{:}	-1.333500 	-0.409900 	0.000300''').format(s1[gene_number_3])
    parameter_s1_4=('''{:}	-1.021500 	0.949600 	-0.000100''').format(s1[gene_number_4])
    parameter_s1_5=('''{:}	0.311800 	1.359200 	-0.000400''').format(s1[gene_number_5])
    parameter_s1_6=('''{:}	1.333200 	0.409300 	-0.000300''').format(s1[gene_number_6])

    parameter_s2_1=('''{:}	2.049100 	-1.905500 	0.000200''').format(s2[gene_number_1])
    parameter_s2_2=('''{:}	-0.625700 	-2.727600 	-0.000300''').format(s2[gene_number_2])
    parameter_s2_3=('''{:}	-2.675000 	-0.821700 	0.000300''').format(s2[gene_number_3])
    parameter_s2_4=('''{:}	-2.048600 	1.905500 	0.000700''').format(s2[gene_number_4])
    parameter_s2_5=('''{:}	0.626100 	2.726900 	-0.001000''').format(s2[gene_number_5])
    parameter_s2_6=('''{:}	2.674400 	0.821700 	0.000100''').format(s2[gene_number_6])

    parameter_s3_L_H_1=('''{:}	2.335629 	-2.192029 	-1.065352''').format(s3_L_H[gene_number_1])
    parameter_s3_L_H_2=('''{:}	-0.625700 	-3.159732 	1.054623''').format(s3_L_H[gene_number_2])
    parameter_s3_L_H_3=('''{:}	-3.232177 	-0.821700 	-0.994262''').format(s3_L_H[gene_number_3])
    parameter_s3_L_H_4=('''{:}	-2.048600 	2.229454 	1.093702''').format(s3_L_H[gene_number_4])
    parameter_s3_L_H_5=('''{:}	0.626100 	3.105363 	-1.076345''').format(s3_L_H[gene_number_5])
    parameter_s3_L_H_6=('''{:}	3.076090 	0.821700 	1.066986''').format(s3_L_H[gene_number_6])

    parameter_s3_L_notH_1=('''{:}	2.478524 	-2.334924 	-1.382294''').format(s3_L_notH[gene_number_1])
    parameter_s3_L_notH_2=('''{:}	-0.625700 	-3.225170 	1.425366''').format(s3_L_notH[gene_number_2])
    parameter_s3_L_notH_3=('''{:}	-3.385563 	-0.821700 	-1.332067''').format(s3_L_notH[gene_number_3])
    parameter_s3_L_notH_4=('''{:}	-2.514092 	2.370992 	1.359646''').format(s3_L_notH[gene_number_4])
    parameter_s3_L_notH_5=('''{:}	0.626100 	3.381468 	-1.361750''').format(s3_L_notH[gene_number_5])
    parameter_s3_L_notH_6=('''{:}	3.357146 	0.821700 	1.346933''').format(s3_L_notH[gene_number_6])
 
   ## s3_R : 6 rings Backbone 위-오른쪽(원자多) : gene 8~37 : 30개
    ## s3_R_H : 6 rings Backbone 위-오른쪽 *수소 : 25개
    parameter_s3_R_H_1=('''{:}	2.049100 	-2.251694 	1.023210''').format(s3_R_H[gene_number_1])
    parameter_s3_R_H_2=('''{:}	-0.625700 	-3.249883 	-0.945615''').format(s3_R_H[gene_number_2])
    parameter_s3_R_H_3=('''{:}	-3.074311 	-1.221011 	0.920898''').format(s3_R_H[gene_number_3])
    parameter_s3_R_H_4=('''{:}	-2.048600 	2.122312 	-1.057313''').format(s3_R_H[gene_number_4])
    parameter_s3_R_H_5=('''{:}	0.626100 	3.114512 	1.007046''').format(s3_R_H[gene_number_5])
    parameter_s3_R_H_6=('''{:}	3.148236 	0.821700 	-0.970405''').format(s3_R_H[gene_number_6])
     
    parameter_s3_R_notH_1=('''{:}	2.401200 	-2.232400 	1.152600''').format(s3_R_notH[gene_number_1])
    parameter_s3_R_notH_2=('''{:}	-0.733500 	-3.195300 	-1.153000''').format(s3_R_notH[gene_number_2])
    parameter_s3_R_notH_3=('''{:}	-3.134200 	-0.962600 	1.152800''').format(s3_R_notH[gene_number_3])
    parameter_s3_R_notH_4=('''{:}	-2.401600 	2.232900 	-1.151400''').format(s3_R_notH[gene_number_4])
    parameter_s3_R_notH_5=('''{:}	0.734000 	3.195600 	1.151100''').format(s3_R_notH[gene_number_5])
    parameter_s3_R_notH_6=('''{:}	3.134300 	0.962500 	-1.152200''').format(s3_R_notH[gene_number_6])

    parameter_s4_R_M_1=('''{:}	2.730700 	-2.538000 	2.201900''').format(s4_R_M[gene_number_1])
    parameter_s4_R_M_2=('''{:}	-0.834500 	-3.632600 	-2.202400''').format(s4_R_M[gene_number_2])
    parameter_s4_R_M_3=('''{:}	-3.563700 	-1.094500 	2.202000''').format(s4_R_M[gene_number_3])
    parameter_s4_R_M_4=('''{:}	-2.731300 	2.539100 	-2.200300''').format(s4_R_M[gene_number_4])
    parameter_s4_R_M_5=('''{:}	0.834700 	3.634000 	2.200200''').format(s4_R_M[gene_number_5])
    parameter_s4_R_M_6=('''{:}	3.564200 	1.093900 	-2.201300''').format(s4_R_M[gene_number_6])

    parameter_s4_R_T_1=('''{:}	3.407324 	-2.742219 	1.318128''').format(s4_R_T[gene_number_1])
    parameter_s4_R_T_2=('''{:}	0.200218 	-3.474196 	-1.744598''').format(s4_R_T[gene_number_2])
    parameter_s4_R_T_3=('''{:}	-4.174640 	-1.404055 	1.301802''').format(s4_R_T[gene_number_3])
    parameter_s4_R_T_4=('''{:}	-1.718159 	2.020845 	-2.038835''').format(s4_R_T[gene_number_4])
    parameter_s4_R_T_5=('''{:}	1.766185 	3.344155 	1.611670''').format(s4_R_T[gene_number_5])
    parameter_s4_R_T_6=('''{:}	2.513827 	0.649209 	-2.055782''').format(s4_R_T[gene_number_6])

    parameter_s4_R_B_1=('''{:}	1.716566 	-2.021061 	2.039286''').format(s4_R_B[gene_number_1])
    parameter_s4_R_B_2=('''{:}	-1.765639 	-3.343414 	-1.613816''').format(s4_R_B[gene_number_2])
    parameter_s4_R_B_3=('''{:}	-2.513024 	-0.649791 	2.056066''').format(s4_R_B[gene_number_3])
    parameter_s4_R_B_4=('''{:}	-3.407325 	2.743866 	-1.315814''').format(s4_R_B[gene_number_4])
    parameter_s4_R_B_5=('''{:}	-0.199659 	3.475026 	1.742540''').format(s4_R_B[gene_number_5])
    parameter_s4_R_B_6=('''{:}	4.174656 	1.404340 	-1.300651''').format(s4_R_B[gene_number_6])

    parameter_7_1=('''{:}	3.115988 	-2.974074 	0.000200''').format('N')
    parameter_7_2=('''{:}	-0.956239 	-4.200978 	-0.000300''').format('N')
    parameter_7_3=('''{:}	-4.149640 	-1.146565 	0.000300''').format('N')
    parameter_7_4=('''{:}	-3.128011 	2.961422 	0.000700''').format('N')
    parameter_7_5=('''{:}	0.950129 	4.201724 	-0.001000''').format('N')
    parameter_7_6=('''{:}	4.084326 	1.362262 	0.000100''').format('N')

    parameter_13_1=('''{:}	2.722993 	-2.545707 	3.311847''').format('H')
    parameter_13_2=('''{:}	-0.920443 	-3.632600 	-3.309068''').format('H')
    parameter_13_3=('''{:}	-3.808347 	-1.339147 	3.256702''').format('H')
    parameter_13_4=('''{:}	-3.046848 	2.854648 	-3.216646''').format('H')
    parameter_13_5=('''{:}	1.139924 	3.939224 	3.222832''').format('H')
    parameter_13_6=('''{:}	3.827912 	1.357612 	-3.246772''').format('H')

    parameter_15_1=('''{:}	3.371317 	-1.696642 	1.419875 
{:}	2.565741 	-3.359694 	1.194251 
{:}	1.588031 	-1.939345 	1.895886''').format('H','H','H')
    parameter_15_2=('''{:}	-0.265091 	-4.234068 	-1.186958  
{:}	-0.197447 	-2.512393 	-1.891841  
{:}	-1.836384 	-3.266448 	-1.432616''').format('H','H','H')
    parameter_15_3=('''{:}	-3.357864 	-2.064547 	1.340646  
{:}	-4.094514 	-0.356986 	1.255896 
{:}	-2.369485 	-0.594912 	1.914125''').format('H','H','H')
    parameter_15_4=('''{:}	-2.453143 	1.304692 	-1.811229  
{:}	-1.645447 	2.966819 	-1.586366 
{:}	-3.428493 	2.726100 	-1.108453''').format('H','H','H')
    parameter_15_5=('''{:}	1.335647 	4.163155 	1.112913 
{:}	1.268107 	2.442129 	1.819390 
{:}	-0.303229 	3.409497 	1.573006''').format('H','H','H')
    parameter_15_6=('''{:}	2.453596 	1.653449 	-1.751226 
{:}	3.190884 	-0.053791 	-1.665571
{:}	4.178302 	1.416391 	-1.091836''').format('H','H','H')
    # gene 26
    parameter_26_1=('''{:}	1.343157 	-3.006384 	2.474377 
{:}	0.827397 	-1.397495 	1.692670 
{:}	2.294511 	-1.447965 	2.837497''').format('H','H','H')
    parameter_26_2=('''{:}	-2.069401 	-4.438323 	-1.521598 
{:}	-1.736158 	-3.048661 	-2.714657 
{:}	-2.523497 	-2.691372 	-1.066008''').format('H','H','H')
    parameter_26_3=('''{:}	-1.670715 	0.039809 	1.717588
{:}	-2.069963 	-1.575891 	2.551682 
{:}	-3.177218 	-0.100482 	2.802194''').format('H','H','H')
    parameter_26_4=('''{:}	-4.248632 	2.012618 	-1.076903 
{:}	-3.490937 	3.077360 	-2.402732
{:}	-3.488130 	3.652585 	-0.632221''').format('H','H','H')
    parameter_26_5=('''{:}	-0.656383 	2.535083 	2.198073
{:}	-0.957140 	3.966819 	1.046866
{:}	0.080887 	4.202602 	2.574121''').format('H','H','H')
    parameter_26_6=('''{:}	4.292311 	1.744306 	-2.382400
{:}	4.960759 	0.613608 	-1.063195
{:}	4.311253 	2.296946 	-0.604809''').format('H','H','H')

    parameter_27_1=('''{:}	0.662243 	-2.367735 	2.021399
{:}	2.104272 	-1.468610 	2.920525''').format('H','H')
    parameter_27_2=('''{:}	-1.898020 	-4.042856 	-2.465494 
{:}	-2.638235 	-2.788188 	-1.210827''').format('H','H')
    parameter_27_3=('''{:}	-1.431373 	-0.895539 	2.097777 
{:}	-2.989845 	-0.099466 	2.893851''').format('H','H')
    parameter_27_4=('''{:}	-4.124519 	2.332213 	-2.056270 
{:}	-3.669390 	3.653038 	-0.735445''').format('H','H')
    parameter_27_5=('''{:}	-1.183470 	3.043633 	1.463049 
{:}	-0.124937 	4.178492 	2.597907''').format('H','H')
    parameter_27_6=('''{:}	4.869134 	0.952837 	-2.039532 
{:}	4.493156 	2.286055 	-0.706314''').format('H','H')

    parameter_28_1=('''{:}	3.576014 	-2.204980 	-1.485884 
{:}	1.609430 	-1.947057 	1.876326''').format('H','H')
    parameter_28_2=('''{:}	-0.298178 	-2.408657 	2.102223 
{:}	-1.807361 	-3.264575 	-1.425257''').format('H','H')
    parameter_28_3=('''{:}	-4.395196 	-0.376109 	-1.212949 
{:}	-2.389609 	-0.604588 	1.894091''').format('H','H')
    parameter_28_4=('''{:}	-1.643757 	2.736214 	1.943794 
{:}	-3.401470 	2.713121 	-1.109583''').format('H','H')
    parameter_28_5=('''{:}	1.042329 	4.407137 	-1.278949 
{:}	-0.275933 	3.403868 	1.561904''').format('H','H')
    parameter_28_6=('''{:}	2.673908 	1.252858 	2.108109 
{:}	4.150828 	1.404446 	-1.093425''').format('H','H')

    parameter_29_1=('''{:}	1.704535 	-2.718877 	-2.126015 
{:}	3.576713 	-2.275172 	-1.682310''').format('H','H')
    parameter_29_2=('''{:}	-0.934679 	-4.298299 	1.654552 
{:}	-0.316721 	-2.527690 	2.272510''').format('H','H')
    parameter_29_3=('''{:}	-2.865570 	-1.242064 	-2.255377 
{:}	-4.442007 	-0.401336 	-1.414649''').format('H','H')
    parameter_29_4=('''{:}	-3.618472 	2.309766 	1.635684 
{:}	-1.761143 	2.783649 	2.109567''').format('H','H')
    parameter_29_5=('''{:}	0.233436 	2.812266 	-2.268075 
{:}	1.018764 	4.444847 	-1.482747''').format('H','H')
    parameter_29_6=('''{:}	4.417251 	0.414952 	1.448592 
{:}	2.812492 	1.228448 	2.262088 ''').format('H','H')

    parameter_30_1=('''{:}	1.945030 	-1.696239 	-2.161438 
{:}	2.209068 	-3.431266 	-1.540497 
{:}	3.605676 	-2.201468 	-1.488683 
{:}	3.371317 	-1.696642 	1.419875 
{:}	2.565741 	-3.359694 	1.194251 
{:}	1.588031 	-1.939345 	1.895886''').format('H','H','H','H','H','H')
    parameter_30_2=('''{:}	0.090160 	-4.107324 	1.519965 
{:}	-1.677934 	-3.557246 	1.711947 
{:}	-0.289326 	-2.386589 	2.120516 
{:}	-0.265091 	-4.234068 	-1.186958 
{:}	-0.197447 	-2.512393 	-1.891841 
{:}	-1.836384 	-3.266448 	-1.432616''').format('H','H','H','H','H','H')
    parameter_30_3=('''{:}	-3.485029 	-1.892733 	-1.709684 
{:}	-2.785628 	-0.208301 	-2.082680 
{:}	-4.422484 	-0.364066 	-1.209730 
{:}	-3.357864 	-2.064547 	1.340646 
{:}	-4.094514 	-0.356986 	1.255896 
{:}	-2.369485 	-0.594912 	1.914125''').format('H','H','H','H','H','H')
    parameter_30_4=('''{:}	-3.004558 	1.502329 	1.911432 
{:}	-3.268915 	3.215993 	1.233883 
{:}	-1.620234 	2.746085 	1.959582 
{:}	-2.453143 	1.304692 	-1.811229 
{:}	-1.645447 	2.966819 	-1.586366 
{:}	-3.428493 	2.726100 	-1.108453''').format('H','H','H','H','H','H')
    parameter_30_5=('''{:}	-0.441657 	3.435477 	-1.757449 
{:}	1.266379 	2.768246 	-2.078410 
{:}	1.053578 	4.434858 	-1.276712 
{:}	1.335647 	4.163155 	1.112913 
{:}	1.268107 	2.442129 	1.819390 
{:}	-0.303229 	3.409497 	1.573006''').format('H','H','H','H','H','H')
    parameter_30_6=('''{:}	4.307770 	1.448433 	1.291073 
{:}	3.623676 	-0.247844 	1.637858 
{:}	2.655443 	1.264511 	2.128682 
{:}	2.453596 	1.653449 	-1.751226 
{:}	3.190884 	-0.053791 	-1.665571 
{:}	4.178302 	1.416391 	-1.091836''').format('H','H','H','H','H','H')
 

    for j in range(6):
 
            if j==0:
                #gene 1~3
                if 1<=chromos[i][0]<=3 :
                    parameter_1 = parameter_s1_1
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][0]<=6 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1
                    count_row += 2
                #gene 7
                elif chromos[i][0]==7 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_7_1
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][0]<=9 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_H_1
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][0]<=12 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1+'\n'+ parameter_s4_R_M_1
                    count_row += 4
                #gene 13
                elif chromos[i][0]==13 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1+'\n'+ parameter_s4_R_M_1 +'\n'+ parameter_13_1
                    count_row += 5
                #gene 14
                elif chromos[i][0]==14 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1+'\n'+ parameter_s4_R_T_1+'\n'+ parameter_s4_R_B_1
                    count_row += 5
                #gene 15
                elif chromos[i][0]==15 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1+'\n'+ parameter_15_1
                    count_row += 6
                #gene 16
                elif chromos[i][0]==16 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_H_1
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][0]<=18 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_H_1+'\n'+ parameter_s3_L_H_1
                    count_row += 4 
                #gene 19
                elif chromos[i][0]==19 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1
                    count_row += 4 
                #gene 20
                elif chromos[i][0]==20 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_H_1 +'\n'+ parameter_s3_L_H_1
                    count_row += 4 
                #gene 21
                elif chromos[i][0]==21 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1 +'\n'+ parameter_s4_R_T_1
                    count_row += 5
                #gene 22
                elif chromos[i][0]==22 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_H_1 +'\n'+ parameter_s4_R_T_1
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][0]<=25 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_H_1 +'\n'+ parameter_s4_R_T_1 +'\n'+ parameter_s4_R_B_1 
                    count_row += 6 
                #gene 26
                elif chromos[i][0]==26 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1 +'\n'+ parameter_s4_R_B_1 +'\n'+ parameter_26_1 
                    count_row += 8
                #gene 27
                elif chromos[i][0]==27 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_H_1 +'\n'+ parameter_s4_R_T_1 +'\n' + parameter_s4_R_B_1 +'\n'+ parameter_27_1 
                    count_row += 8
                #gene 28
                elif chromos[i][0]==28 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1 +'\n'+ parameter_28_1 
                    count_row += 6
                #gene 29
                elif chromos[i][0]==29 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1 +'\n'+ parameter_s4_R_T_1 +'\n'+ parameter_s4_R_B_1 +'\n'+ parameter_29_1 
                    count_row += 8
                #gene 30 
                elif chromos[i][0]==30 :
                    parameter_1 = parameter_s1_1 +'\n'+ parameter_s2_1 +'\n'+ parameter_s3_R_notH_1 +'\n'+ parameter_s3_L_notH_1 +'\n' + parameter_30_1 
                    count_row += 10
            ###########################################################################################################################################################################################################
            #2nd gene : chromos[i][1]
            elif j==1:
                #gene 1~3
                if 1<=chromos[i][1]<=3 :
                    parameter_2 = parameter_s1_2
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][1]<=6 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2
                    count_row += 2
                #gene 7
                elif chromos[i][1]==7 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_7_2
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][1]<=9 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_H_2
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][1]<=12 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2+'\n'+ parameter_s4_R_M_2
                    count_row += 4
                #gene 13
                elif chromos[i][1]==13 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2+'\n'+ parameter_s4_R_M_2 +'\n'+ parameter_13_2
                    count_row += 5
                #gene 14
                elif chromos[i][1]==14 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2+'\n'+ parameter_s4_R_T_2+'\n'+ parameter_s4_R_B_2
                    count_row += 5
                #gene 15
                elif chromos[i][1]==15 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2+'\n'+ parameter_15_2
                    count_row += 6
                #gene 16
                elif chromos[i][1]==16 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_H_2
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][1]<=18 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_H_2+'\n'+ parameter_s3_L_H_2
                    count_row += 4 
                #gene 19
                elif chromos[i][1]==19 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2
                    count_row += 4 
                #gene 20
                elif chromos[i][1]==20 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_H_2 +'\n'+ parameter_s3_L_H_2
                    count_row += 4 
                #gene 21
                elif chromos[i][1]==21 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2 +'\n'+ parameter_s4_R_T_2
                    count_row += 5
                #gene 22
                elif chromos[i][1]==22 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_H_2 +'\n'+ parameter_s4_R_T_2
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][1]<=25 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_H_2 +'\n'+ parameter_s4_R_T_2 +'\n'+ parameter_s4_R_B_2 
                    count_row += 6 
                #gene 26
                elif chromos[i][1]==26 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2 +'\n'+ parameter_s4_R_B_2 +'\n'+ parameter_26_2 
                    count_row += 8
                #gene 27
                elif chromos[i][1]==27 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_H_2 +'\n'+ parameter_s4_R_T_2 +'\n' + parameter_s4_R_B_2 +'\n'+ parameter_27_2 
                    count_row += 8
                #gene 28
                elif chromos[i][1]==28 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2 +'\n'+ parameter_28_2 
                    count_row += 6
                #gene 29
                elif chromos[i][1]==29 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2 +'\n'+ parameter_s4_R_T_2 +'\n'+ parameter_s4_R_B_2 +'\n'+ parameter_29_2 
                    count_row += 8
                #gene 30
                elif chromos[i][1]==30 :
                    parameter_2 = parameter_s1_2 +'\n'+ parameter_s2_2 +'\n'+ parameter_s3_R_notH_2 +'\n'+ parameter_s3_L_notH_2 +'\n' + parameter_30_2 
                    count_row += 10
            ###########################################################################################################################################################################################################
            #3rd gene : chromos[i][2]
            elif j==2:
                #gene 1~3
                if 1<=chromos[i][2]<=3 :
                    parameter_3 = parameter_s1_3
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][2]<=6 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3
                    count_row += 2
                #gene 7
                elif chromos[i][2]==7 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_7_3
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][2]<=9 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_H_3
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][2]<=12 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3+'\n'+ parameter_s4_R_M_3
                    count_row += 4
                #gene 13
                elif chromos[i][2]==13 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3+'\n'+ parameter_s4_R_M_3 +'\n'+ parameter_13_3
                    count_row += 5
                #gene 14
                elif chromos[i][2]==14 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3+'\n'+ parameter_s4_R_T_3+'\n'+ parameter_s4_R_B_3
                    count_row += 5
                #gene 15
                elif chromos[i][2]==15 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3+'\n'+ parameter_15_3
                    count_row += 6
                #gene 16
                elif chromos[i][2]==16 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_H_3
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][2]<=18 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_H_3+'\n'+ parameter_s3_L_H_3
                    count_row += 4 
                #gene 19
                elif chromos[i][2]==19 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3
                    count_row += 4 
                #gene 20
                elif chromos[i][2]==20 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_H_3 +'\n'+ parameter_s3_L_H_3
                    count_row += 4 
                #gene 21
                elif chromos[i][2]==21 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3 +'\n'+ parameter_s4_R_T_3
                    count_row += 5
                #gene 22
                elif chromos[i][2]==22 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_H_3 +'\n'+ parameter_s4_R_T_3
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][2]<=25 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_H_3 +'\n'+ parameter_s4_R_T_3 +'\n'+ parameter_s4_R_B_3 
                    count_row += 6 
                #gene 26
                elif chromos[i][2]==26 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3 +'\n'+ parameter_s4_R_B_3 +'\n'+ parameter_26_3 
                    count_row += 8
                #gene 27
                elif chromos[i][2]==27 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_H_3 +'\n'+ parameter_s4_R_T_3 +'\n' + parameter_s4_R_B_3 +'\n'+ parameter_27_3 
                    count_row += 8
                #gene 28
                elif chromos[i][2]==28 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3 +'\n'+ parameter_28_3 
                    count_row += 6
                #gene 29
                elif chromos[i][2]==29 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3 +'\n'+ parameter_s4_R_T_3 +'\n'+ parameter_s4_R_B_3 +'\n'+ parameter_29_3 
                    count_row += 8
                #gene 30
                elif chromos[i][2]==30 :
                    parameter_3 = parameter_s1_3 +'\n'+ parameter_s2_3 +'\n'+ parameter_s3_R_notH_3 +'\n'+ parameter_s3_L_notH_3 +'\n' + parameter_30_3 
                    count_row += 10
    ###########################################################################################################################################################################################################
            #4th gene : chromos[i][3]
            elif j==3:
                #gene 1~3
                if 1<=chromos[i][3]<=3 :
                    parameter_4 = parameter_s1_4
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][3]<=6 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4
                    count_row += 2
                #gene 7
                elif chromos[i][3]==7 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_7_4
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][3]<=9 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_H_4
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][3]<=12 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4+'\n'+ parameter_s4_R_M_4
                    count_row += 4
                #gene 13
                elif chromos[i][3]==13 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4+'\n'+ parameter_s4_R_M_4 +'\n'+ parameter_13_4
                    count_row += 5
                #gene 14
                elif chromos[i][3]==14 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4+'\n'+ parameter_s4_R_T_4+'\n'+ parameter_s4_R_B_4
                    count_row += 5
                #gene 15
                elif chromos[i][3]==15 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4+'\n'+ parameter_15_4
                    count_row += 6
                #gene 16
                elif chromos[i][3]==16 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_H_4
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][3]<=18 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_H_4+'\n'+ parameter_s3_L_H_4
                    count_row += 4 
                #gene 19
                elif chromos[i][3]==19 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4
                    count_row += 4 
                #gene 20
                elif chromos[i][3]==20 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_H_4 +'\n'+ parameter_s3_L_H_4
                    count_row += 4 
                #gene 21
                elif chromos[i][3]==21 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4 +'\n'+ parameter_s4_R_T_4
                    count_row += 5
                #gene 22
                elif chromos[i][3]==22 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_H_4 +'\n'+ parameter_s4_R_T_4
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][3]<=25 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_H_4 +'\n'+ parameter_s4_R_T_4 +'\n'+ parameter_s4_R_B_4 
                    count_row += 6 
                #gene 26
                elif chromos[i][3]==26 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4 +'\n'+ parameter_s4_R_B_4 +'\n'+ parameter_26_4 
                    count_row += 8
                #gene 27
                elif chromos[i][3]==27 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_H_4 +'\n'+ parameter_s4_R_T_4 +'\n' + parameter_s4_R_B_4 +'\n'+ parameter_27_4 
                    count_row += 8
                #gene 28
                elif chromos[i][3]==28 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4 +'\n'+ parameter_28_4 
                    count_row += 6
                #gene 29
                elif chromos[i][3]==29 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4 +'\n'+ parameter_s4_R_T_4 +'\n'+ parameter_s4_R_B_4 +'\n'+ parameter_29_4 
                    count_row += 8
                #gene 30
                elif chromos[i][3]==30 :
                    parameter_4 = parameter_s1_4 +'\n'+ parameter_s2_4 +'\n'+ parameter_s3_R_notH_4 +'\n'+ parameter_s3_L_notH_4 +'\n' + parameter_30_4 
                    count_row += 10
    ###########################################################################################################################################################################################################
            #5th gene : chromos[i][4]
            elif j==4:
                #gene 1~3
                if 1<=chromos[i][4]<=3 :
                    parameter_5 = parameter_s1_5
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][4]<=6 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5
                    count_row += 2
                #gene 7
                elif chromos[i][4]==7 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_7_5
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][4]<=9 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_H_5
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][4]<=12 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5+'\n'+ parameter_s4_R_M_5
                    count_row += 4
                #gene 13
                elif chromos[i][4]==13 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5+'\n'+ parameter_s4_R_M_5 +'\n'+ parameter_13_5
                    count_row += 5
                #gene 14
                elif chromos[i][4]==14 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5+'\n'+ parameter_s4_R_T_5+'\n'+ parameter_s4_R_B_5
                    count_row += 5
                #gene 15
                elif chromos[i][4]==15 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5+'\n'+ parameter_15_5
                    count_row += 6
                #gene 16
                elif chromos[i][4]==16 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_H_5
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][4]<=18 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_H_5+'\n'+ parameter_s3_L_H_5
                    count_row += 4 
                #gene 19
                elif chromos[i][4]==19 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5
                    count_row += 4 
                #gene 20
                elif chromos[i][4]==20 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_H_5 +'\n'+ parameter_s3_L_H_5
                    count_row += 4 
                #gene 21
                elif chromos[i][4]==21 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5 +'\n'+ parameter_s4_R_T_5
                    count_row += 5
                #gene 22
                elif chromos[i][4]==22 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_H_5 +'\n'+ parameter_s4_R_T_5
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][4]<=25 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_H_5 +'\n'+ parameter_s4_R_T_5 +'\n'+ parameter_s4_R_B_5 
                    count_row += 6 
                #gene 26
                elif chromos[i][4]==26 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5 +'\n'+ parameter_s4_R_B_5 +'\n'+ parameter_26_5 
                    count_row += 8
                #gene 27
                elif chromos[i][4]==27 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_H_5 +'\n'+ parameter_s4_R_T_5 +'\n' + parameter_s4_R_B_5 +'\n'+ parameter_27_5 
                    count_row += 8
                #gene 28
                elif chromos[i][4]==28 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5 +'\n'+ parameter_28_5 
                    count_row += 6
                #gene 29
                elif chromos[i][4]==29 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5 +'\n'+ parameter_s4_R_T_5 +'\n'+ parameter_s4_R_B_5 +'\n'+ parameter_29_5 
                    count_row += 8
                #gene 30
                elif chromos[i][4]==30 :
                    parameter_5 = parameter_s1_5 +'\n'+ parameter_s2_5 +'\n'+ parameter_s3_R_notH_5 +'\n'+ parameter_s3_L_notH_5 +'\n' + parameter_30_5 
                    count_row += 10
    ###########################################################################################################################################################################################################
            #6th gene : chromos[i][5]
            elif j==5:
                #gene 1~3
                if 1<=chromos[i][5]<=3 :
                    parameter_6 = parameter_s1_6
                    count_row += 1
                #gene 4~6
                elif 4<=chromos[i][5]<=6 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6
                    count_row += 2
                #gene 7
                elif chromos[i][5]==7 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_7_6
                    count_row += 3
                #gene 8~9
                elif 8<=chromos[i][5]<=9 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_H_6
                    count_row += 3
                #gene 10~12
                elif 10<=chromos[i][5]<=12 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6+'\n'+ parameter_s4_R_M_6
                    count_row += 4
                #gene 13
                elif chromos[i][5]==13 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6+'\n'+ parameter_s4_R_M_6 +'\n'+ parameter_13_6
                    count_row += 5
                #gene 14
                elif chromos[i][5]==14 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6+'\n'+ parameter_s4_R_T_6+'\n'+ parameter_s4_R_B_6
                    count_row += 5
                #gene 15
                elif chromos[i][5]==15 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6+'\n'+ parameter_15_6
                    count_row += 6
                #gene 16
                elif chromos[i][5]==16 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_H_6
                    count_row += 4 
                #gene 17~18
                elif 17<=chromos[i][5]<=18 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_H_6+'\n'+ parameter_s3_L_H_6
                    count_row += 4 
                #gene 19
                elif chromos[i][5]==19 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6
                    count_row += 4 
                #gene 20
                elif chromos[i][5]==20 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_H_6 +'\n'+ parameter_s3_L_H_6
                    count_row += 4 
                #gene 21
                elif chromos[i][5]==21 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6 +'\n'+ parameter_s4_R_T_6
                    count_row += 5
                #gene 22
                elif chromos[i][5]==22 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_H_6 +'\n'+ parameter_s4_R_T_6
                    count_row += 5
                #gene 23~25
                elif 23<=chromos[i][5]<=25 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_H_6 +'\n'+ parameter_s4_R_T_6 +'\n'+ parameter_s4_R_B_6 
                    count_row += 6 
                #gene 26
                elif chromos[i][5]==26 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6 +'\n'+ parameter_s4_R_B_6 +'\n'+ parameter_26_6 
                    count_row += 8
                #gene 27
                elif chromos[i][5]==27 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_H_6 +'\n'+ parameter_s4_R_T_6 +'\n' + parameter_s4_R_B_6 +'\n'+ parameter_27_6 
                    count_row += 8
                #gene 28
                elif chromos[i][5]==28 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6 +'\n'+ parameter_28_6 
                    count_row += 6
                #gene 29
                elif chromos[i][5]==29 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6 +'\n'+ parameter_s4_R_T_6 +'\n'+ parameter_s4_R_B_6 +'\n'+ parameter_29_6 
                    count_row += 8
                #gene 30
                elif chromos[i][5]==30 :
                    parameter_6 = parameter_s1_6 +'\n'+ parameter_s2_6 +'\n'+ parameter_s3_R_notH_6 +'\n'+ parameter_s3_L_notH_6 +'\n' + parameter_30_6 
                    count_row += 10
    ###########################################################################################################################################################################################################        
    parameter = parameter_1 +'\n'+ parameter_2 +'\n'+ parameter_3 +'\n'+ parameter_4 +'\n'+ parameter_5+'\n'+ parameter_6
    
    title ='{}_chromo{}__{}_{}_{}_{}_{}_{}'.format(generation,i+1,gene_number_1,gene_number_2,gene_number_3,gene_number_4,gene_number_5,gene_number_6)
    with open(title +'.xyz', 'w') as com_file:
            com_file.write(str(count_row))
            com_file.write('\n')
            com_file.write('GA\n')
            com_file.write(parameter)
            com_file.write('\n')


os.chdir('../results/' + list_gen[0])
for path_chromos in range(0,len(list_chromos),1):
    data_xyz(chromos,path_chromos)
os.remove('../../code/chromo_information.py')

#chromos xyz file generation completed
print("===========================")
print("Next generation chromo xyz files generation completed!")
print("===========================")