from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')

# print(data.loc[data['Champion'] == 'Xerath']['Games Played'])
# print(data.loc[data['Champion'] == 'Xerath']['Season'])

print(data['Champion'].unique())

for champ in data.loc[data['Games Played'] >= 15]['Champion'].unique():
    x,y = [],[]
    d = data.loc[data['Champion'] == champ]
    # print(d)
    for i in sorted(data['Season'].unique()):
        # print(i)
        x.append(i)
        if d.loc[d['Season'] == i].empty:
            # print('\t',i)
            y.append(0)
        else:
            # print(d.loc[d['Season'] == i]['Games Played'].values)
            y.append(d.loc[d['Season'] == i]['Games Played'].values)
    print(x,y)
    plt.plot(x,y, label=champ, alpha=.5, linewidth=3)
    # plt.plot(d['Season'],d['Games Played'], label=champ)

# champ = 'Xerath'
# plt.plot(data.loc[data['Champion'] == champ]['Season'],data.loc[data['Champion'] == champ]['Games Played'], label=champ)
# champ = 'Thresh'
# plt.plot(data.loc[data['Champion'] == champ]['Season'],data.loc[data['Champion'] == champ]['Games Played'], label=champ)
# champ = 'Le'
# plt.plot(data.loc[data['Champion'] == champ]['Season'],data.loc[data['Champion'] == champ]['Games Played'], label='LeBlanc')
# champ = 'Viktor'
# plt.plot(data.loc[data['Champion'] == champ]['Season'],data.loc[data['Champion'] == champ]['Games Played'], label=champ)
# champ = 'Orianna'
# plt.plot(data.loc[data['Champion'] == champ]['Season'],data.loc[data['Champion'] == champ]['Games Played'], label=champ)
plt.plot([5,6,7,8,9,10,11], [15,121,328,97,196,216,133], label='Total Games')
plt.xlabel('Season')
plt.ylabel('Ranked Games Played')
plt.legend(loc='best')
plt.show()