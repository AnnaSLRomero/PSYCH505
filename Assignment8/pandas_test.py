import pandas as pd
import json as json
import os

filename = 'participantData_Nov28.csv'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'exp','data',filename)

df = pd.read_json(filename+'_block1.txt')


print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))

print("Response Time mean")
print(sum(df['resp_time'])/len(df['resp_time']))

print("Subject accuracy mean")
print(sum(df['sub_acc'])/len(df['sub_acc']))

print("Subject response mean")
print(sum(df['sub_resp'])/len(df['sub_resp']))

print("Correct response mean")
print(sum(df['corr_resp'])/len(df['corr_resp']))

