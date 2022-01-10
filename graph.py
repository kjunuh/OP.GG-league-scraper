from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt

folder = 'data/'

def plotChamps(username):
    global folder
    data = pd.read_csv(folder+username+'.csv')

    for champ in data.loc[data['Games Played'] >= 5]['Champion'].unique():
        x,y = [],[]
        d = data.loc[data['Champion'] == champ]
        for i in sorted(data['Season'].unique()):
            x.append(i)
            if d.loc[d['Season'] == i].empty:
                y.append(0)
            else:
                y.append(d.loc[d['Season'] == i]['Games Played'].values)
        plt.plot(x,y, label=champ, alpha=.5, linewidth=3)

    tGames = [[],[]]
    for i in data['Season'].unique():
        tGames[0].append(i)
        tGames[1].append(data.loc[data['Season'] == i]['Games Played'].sum())
    plt.plot(tGames[0],tGames[1], label='Total Games', alpha=.5, linewidth=3)

    plt.xlabel('Season')
    plt.ylabel('Ranked Games Played')
    plt.legend(loc='best')
    plt.show()

def plotGames(userList):
    global folder
    for user in userList:
        tGames = [[],[]]
        data = pd.read_csv(folder+user+'.csv')
        for i in data['Season'].unique():
            tGames[0].append(i)
            tGames[1].append(data.loc[data['Season'] == i]['Games Played'].sum())
        plt.plot(tGames[0],tGames[1], label=user, alpha=.5, linewidth=3)

    plt.xlabel('Season')
    plt.ylabel('Ranked Games Played')
    plt.legend(loc='best')
    plt.show()

def plotCS(username):
    global folder
    data = pd.read_csv(folder+username+'.csv')
    for champ in data.loc[data['Games Played'] >= 30]['Champion'].unique():
        d = data.loc[data['Champion'] == champ]
        plt.plot(d['Season'].values,d['CS/m'].values, label=champ, alpha=.5, linewidth=3)

    plt.xlabel('Season')
    plt.ylabel('CS/M')
    plt.legend(loc='best')
    plt.show()
ugglee = ['forlorn64', 'chrismonytf', 'parad0x05', '9wonwon', 'jonbom', 'junpi', 'aurumrock', 'hipbo', 'theristis', 'cocheese01', 'minibatman', 'nickizer534', ]
# plotGames(['elfsuf','coolwhip420', 'nraddlygew', 'sekou', 'stealthinator', 'emended', 'xerelic', 'poweredbyrice', 'duckyduckplaysmc', 'meteoryte'])
plotGames(ugglee)
# plotCS('xerelic')