import matplotlib.pyplot as plt


plt.plot([6,7,8,9,10,11], [11,53,105,56,117,129,], label='Sekou',linewidth=3)
plt.plot([5,6,7,8,9,10,11], [15,121,328,97,196,216,133], label='xerelic',linewidth=3)
plt.plot([5,6,7,8,9,10,11], [53,300,349,16,54,234,43], label='Elfsuf',linewidth=3)
plt.plot([7,8,9,10,11], [8,156,142,205,208,], label='Duckyduckplaysmc',linewidth=3)

plt.xlabel('Season')
plt.ylabel('Total Ranked Games Played')
plt.legend(loc='best')
plt.show()

# example ajax page https://na.op.gg/summoner/champions/ajax/champions.rank/summonerId=86862704&season=15& (omar)
