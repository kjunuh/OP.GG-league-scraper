import re
import csv

def cleanFile(file):
    with open(file+".txt", "r") as f:
        data = f.read()
    with open(file+"clean"+".txt", "w") as x:
        html = re.sub('<[^>]+>', '', data)
        tabs = re.sub('\t', "", html)
        x.write(re.sub('\n\n', "", tabs))
    return(file)

def parseData(file):
    with open(file+"clean"+".txt", "r") as f:
        data = []
        for line in f:
            data.append(line.strip())
    data = data[data.index("1")+1:]
    # print(data)
    splitInd = []
    for i in range(len(data)):
        # print(data[i][0], data[i][0].isalpha(), i)
        if data[i][0].isalpha():splitInd.append(i)
    splitInd.append(len(data))
    champs = []
    # print(splitInd)
    for i in range(len(splitInd)-1):
        champs.append(data[splitInd[i]:splitInd[i+1]])
    full = []
    # print(split)
    # print(champs)
    tGames = 0
    for champ in champs:
        cInd = []
        stats = [int(file[1:])]
        statStrs = ["Champion", "Games Played", "Wins", "Losses", "Winrate", "Kills", "Deaths", "Assists", "Gold", "CS"]
        for i in range(len(champ[0])):
            if champ[0][i].isupper(): cInd.append(i)
        stats.append(champ[0][:cInd[1]])
        # print(champ[0])

        if champ[0][-1] == '%':
            if champ[0][cInd[2]] == 'W': # 100% win
                stats.append(int(champ[0][-6])) # Games Played
                tGames += int(champ[0][-6])
                stats.append(int(champ[0][-6])) # Wins
                stats.append(0) # Losses
                stats.append(100) # Winrate
            else: # 100% loss
                stats.append(int(champ[0][-4])) # Games Played
                tGames += int(champ[0][-4])
                stats.append(0) # Wins
                stats.append(int(champ[0][-4])) # Losses
                stats.append(0) # Winrate
            stats.append(float(champ[1].strip(" /"))) #Kills
            stats.append(float(champ[2].strip(" /"))) #Deaths
            pInd = 0
            for i in range(len(champ[3])):
                if champ[2][i] == "." : 
                    pInd = i+2
                    break
            # print(champ)
            stats.append(float(champ[3][:pInd]))
            stats.append(int(champ[4].replace(",","")))
            stats.append(float(champ[5].split('(')[1].strip(')')))
            # stats.append(float(champ[3][pInd:].strip(":1")))
        else:
            if len(cInd) == 4:
                wl = champ[0][cInd[1]*2:]
            elif len(cInd) == 6:
                wl = champ[0][cInd[2]*2:]
                # print(champ[0], wl)
            elif len(cInd) == 8:
                wl = champ[0][cInd[3]*2:]
                # print(champ[0], wl)
            else:
                print('caps wrong ur dumb\n', champ[0])
            wl = wl.split("W")
            # print(wl)
            stats.append(int(wl[0])+int(wl[1].strip("L"))) # Games Played
            tGames += int(wl[0])+int(wl[1].strip("L"))
            stats.append(int(wl[0])) # Wins
            stats.append(int(wl[1].strip("L"))) # Losses
            stats.append(int(wl[0])/(int(wl[0])+int(wl[1].strip("L")))) # Winrate
            stats.append(float(champ[2].strip(" /"))) #Kills
            stats.append(float(champ[3].strip(" /"))) #Deaths

            pInd = 0
            for i in range(len(champ[4])):
                if champ[4][i] == "." : 
                    pInd = i+2
                    break
            # print(champ[4],pInd,champ[4][:pInd],champ[4][pInd:])
            stats.append(float(champ[4][:pInd]))
            stats.append(int(champ[5].replace(",","")))
            stats.append(float(champ[6].split('(')[1].strip(')')))
            # stats.append(float(champ[4][pInd:].strip(":1")))
        
        full.append(stats)
        #print(champ)
    # print(full)
    print(tGames, end=',')
    return full

# md = {"s5": {"Viktor": {"Kills":3, "assists":2}}}
# print(md["s5"]['Viktor']['Kills'])
header = ["Season", "Champion", "Games Played", "Wins", "Losses", "Winrate", "Kills", "Deaths", "Assists", "Gold", "CS/m"]
bigData = []
for n in range(6):
    bigData.append(parseData(cleanFile("s"+str(n+6))))



with open("data.csv", "w+", newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    # print(bigData)
    for elem in bigData:
        writer.writerows(elem)
        # writer.writerow(["\n"])
        # print(elem)