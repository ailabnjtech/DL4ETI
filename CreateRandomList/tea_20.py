import numpy as np
import random

def creat_list(path):
    lists = [[] for i in range(14)]
    with open(path) as f:
        line = f.readline()
        while line:
            classnum = int(line.split("\t")[1])
            #NE
            if classnum == 0:
                lists[0].append(line.split("\t")[0])
            #EH
            if classnum == 1:
                lists[1].append(line.split("\t")[0])
            #EP
            if classnum == 2:
                lists[2].append(line.split("\t")[0])
            #EA
            if classnum == 3:
                lists[3].append(line.split("\t")[0])

            if classnum == 4:
                lists[4].append(line.split("\t")[0])

            if classnum == 5:
                lists[5].append(line.split("\t")[0])

            if classnum == 6:
                lists[6].append(line.split("\t")[0])

            if classnum == 7:
                lists[7].append(line.split("\t")[0])

            if classnum == 8:
                lists[8].append(line.split("\t")[0])

            if classnum == 9:
                lists[9].append(line.split("\t")[0])

            if classnum == 10:
                lists[10].append(line.split("\t")[0])

            if classnum == 11:
                lists[11].append(line.split("\t")[0])

            if classnum == 12:
                lists[12].append(line.split("\t")[0])

            if classnum == 13:
                lists[13].append(line.split("\t")[0])

            line = f.readline()
    f.close()
    return np.array(lists)

list = creat_list("file_list_tea_20_grades.txt")
random_list = open("tea_20_list.txt","w")
for c in range(len(list)):
    random.shuffle(list[c])
    for item in list[c]:
        random_list.write(str(item)+"\t"+str(c)+"\n")
