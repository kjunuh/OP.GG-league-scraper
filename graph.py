from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt

folder = 'data/'

def plotChamps(username):
    global folder
    data = pd.read_hdf(folder+username+'.h5', 'df')
    dic = {}
    fig, ax = plt.subplots()
    for champ in data.loc[data['Games Played'] >= 15]['Champion'].unique():
        # x,y = [],[]
        d = data.loc[data['Champion'] == champ]
        # print(champ)
        try: len(dic[champ])
        except: dic[champ] = []
        for i in sorted(data['Season'].unique()):
            # x.append(i)
            if d.loc[d['Season'] == i].empty:
                dic[champ].append(0)
            else:
                dic[champ].append(d.loc[d['Season'] == i]['Games Played'].values[0])
        # print(champ)

    # tGames = [[],[]]
    seasons = []
    for i in data['Season'].unique():
        seasons.append(i)
    #     dic['Total Games'] = data.loc[data['Season'] == i]['Games Played'].sum()
        
    # ax.stackplot(tGames[0],tGames[1], label='Total Games', alpha=.5, linewidth=3)
    # print(seasons, dic)
    ax.stackplot(seasons, dic.values(), labels=dic.keys(), alpha=0.8)
    ax.legend(loc='upper left')
    ax.set_title(username+' Champion Games per Season')
    ax.set_xlabel('Season')
    ax.set_ylabel('Ranked Games Played')

    plt.show()

def plotGames(userList):
    global folder
    for user in userList:
        tGames = [[],[]]
        data = pd.read_hdf(folder+user+'.h5', 'df')
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
    data = pd.read_hdf(folder+username+'.h5', 'df')
    for champ in data.loc[data['Games Played'] >= 10]['Champion'].unique():
        d = data.loc[data['Champion'] == champ]
        plt.plot(d['Season'].values,d['CS/m'].values, label=champ, alpha=.5, linewidth=3)

    plt.xlabel('Season')
    plt.ylabel('CS/M')
    plt.legend(loc='best')
    plt.show()

iu = ['CyborgSteve', 'D3f3ctive', 'Kevalon', 'AmericanHussar', 'co1iflower', '10slayer', 'MrLDS', 'YourLocalThicc', 'NiabiIsHere', 'Wulfph']
ugglee = ['forlorn64', 'chrismonytf', 'parad0x05', '9wonwon', 'jonbom', 'junpi', 'aurumrock', 'hipbo', 'theristis', 'cocheese01', 'minibatman', 'nickizer534', ]
tfec = ['elfsuf','coolwhip420', 'nraddlygew', 'sekou', 'stealthinator', 'emended', 'xerelic', 'poweredbyrice', 'duckyduckplaysmc', 'meteoryte']
# plotGames(tfec)
# plotChamps('soccer11235')

# plotChamps('xerelic')
# plotChamps('cyborgsteve')
# plotCS('CyborgSteve')
# plotChamps('kevalon')