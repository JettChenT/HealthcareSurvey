import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
df = pd.read_excel('./Healthcare survey(1-101).xlsx')
size = len(df['ID'])
sc = [[0,0] for _ in range(size)]
df['sc'] = sc
# sc = [0 for _ in range(size)]
q1Sc = {
    'Max':5,
    'Excellent':5,
    'Very good':4,
    'Good':3,
    'Fair':2,
    'Poor':1
}

q2Sc = {
    'Max':3,
    'No, not limited at all': 3,
    'Yes, limited a little': 2,
    'Yes, limited a lot':1
}

q3Sc = {
    'Max':3,
    'No, not limited at all': 3,
    'Yes, limited a little': 2,
    'Yes, limited a lot':1
}

q4Sc = {
    'Max':2,
    'Yes':1,
    'No':2
}

q5Sc = {
    'Max':2,
    'Yes':1,
    'No':2
}

q6Sc = {
    'Max':2,
    'Yes':1,
    'No':2,
}
q7Sc = {
    'Max':2,
    'Yes':1,
    'No':2
}
q8Sc = {
    'Max':5,
    'Not at all':5,
    'A little Bit':4,
    'Moderately':3,
    'Quite a bit':2,
    'Exteremly':1
}
q9Sc = {
    'Max':6,
    'All of the time':6,
    'Most of the time':5,
    'A good bit of the time':4,
    'Some of the time':3,
    'A little of the time':2,
    'None of the time':1
}

q10Sc = {
    'Max':6,
    'All of the Time':6,
    'Most of the time':5,
    'A good bit of the time':4,
    'Some of the time':3,
    'A little of the time':2,
    'None of the time':1
}
q11Sc = {
    'Max':6,
    'All of the time':1,
    'Most of the time':2,
    'A good bit of the time':3,
    'Some of the time':4,
    'A little of the time':5,
    'None of the time':6
}
q12Sc = {
    'Max':6,
    'All of the time':1,
    'Most of the time':2,
    'A good bit of the time':3,
    'Some of the time':4,
    'A little of the time':5,
    'None of the time':6
}
compSc = []
scoreGroup = []
ExpectRealityGroup = []
diff = 0
diff2 = 0
larger = 0
smaller = 0
for i in range(size):
    rw = df.iloc[i]
    age = rw['Enter your age:']
    if age >100:
        continue
    sc[i][1] = rw['Enter your age:']
    q2 = rw['Moderate activities, such as moving a table, pushing a vacuum cleaner, bowling or playing golf']
    sc[i][0]+=q2Sc[q2]/q2Sc['Max']*100
    q3 = rw['Climbing several flights of stairs']
    sc[i][0]+=q3Sc[q3]/q3Sc['Max']*100
    q4 = rw['Accomplished less than you would like']
    sc[i][0]+=q4Sc[q4]/q4Sc['Max']*100
    q5 = rw['Were limited in the kind of work or other activities']
    sc[i][0]+=q5Sc[q5]/q5Sc['Max']*100
    q6 = rw['Accomplished less than you would like2']
    sc[i][0]+=q6Sc[q6]/q6Sc['Max']*100
    q7  = rw["Didn't work or other activities as carefully as usual"]
    sc[i][0]+=q7Sc[q7]/q7Sc['Max']*100
    q8 = rw["During the past 4 weeks, how much did pain interfere with your normal work(including both work outside the home and housework)?"]
    sc[i][0]+=q8Sc[q8]/q8Sc['Max']*100
    q9 = rw["Have you felt calm and peaceful?"]
    sc[i][0]+=q9Sc[q9]/q9Sc['Max']*100
    q10 = rw["Did you have a lot of energy?"]
    sc[i][0]+=q10Sc[q10]/q10Sc['Max']*100
    q11 = rw["Have you felt downhearted and blue?"]
    sc[i][0]+=q11Sc[q11]/q11Sc['Max']*100
    q12 = rw["During the past 4 weeks how much of the time has your physical health or emotional problems interfered with your social activities?"]
    sc[i][0]+=q12Sc[q12]/q12Sc['Max']*100
    sc[i][0] = sc[i][0]/11


y = [sc[i][0] for i in range(size)]
print(sum(y)/len(y))
x = [sc[i][1] for i in range(size)]
print(sum(x)/len(x))
colors = (0,0,0)
area = 100
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.title('age/score comparison')
plt.ylabel('score')
plt.xlabel('age')
plt.show()