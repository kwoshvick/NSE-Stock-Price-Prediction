import pandas as pd
import csv


# def money_to_float(money_str):
#     return 12
#
# file =  pd.read_csv('EQTY.csv')
# #
# # print(file[[-1]])
#
# file[[-1]] = file[[-1]].apply(money_to_float)
#
# print(file[[-1]])

mylist = list()


with open('SCOM.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         print(row)
         try:
             int(row[-1])
         except:
             n = row[-1]
             m = n.find("M")
             x = n.replace('M','')
             n = float(x)*1000000
             # print(int(n))
             row[-1] = int(n)
             mylist.append(row)












myFile = open('safaricom.csv', 'w')
writeFile = csv.writer(myFile, delimiter=',')
writeFile.writerows(mylist)



# m = list(file[[-1]])
#
# print(m)

#
#
# for index, i in file.iterrows():
#     # print(i[-1])
#
#     try:
#         int(file[[-1]])
#     except:
#         print(i)
        # print(file[[-1]])
        # file[[-1]] = 0
        # bh =0
        # n = i[-1]
        # print(n)
        # m = n.find("M")
        # x = n.replace('M','')
        #
        # n = float(x)*1000000
        #
        # print(int(n))


# print(file[[-1]])


# n = '1.42M'
#
# print(n.find("M"))


#
# x = n.replace('M','')
#
# n = float(x)*1000000
#
# print(int(n))