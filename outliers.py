import json
import sys
import os
import numpy as np
import scipy.stats as stats

files = os.listdir('ipl_cricsheet')

total_games = 0

outliers = {}

for f in files:
    if f == 'README.txt':
        continue
    with open('ipl_cricsheet/' + f, 'r') as json_file:
        dicti = json.load(json_file)

    for inn in dicti['innings']:
        bowlers = []
        runs_by_over = np.zeros(20)
        for over in inn['overs']:
            bowlers.append(over['deliveries'][0]['bowler'])
            for dlv in over['deliveries']:
                runs_by_over[over['over']] += dlv['runs']['batter']
        # print(bowlers)
        # print(runs_by_over)
        # print(np.mean(runs_by_over))
        # print(stats.zscore(runs_by_over))

        zscores = stats.zscore(runs_by_over)

        for i in range(len(bowlers)):
            if zscores[i] < -1:
                if bowlers[i] not in outliers:
                    outliers[bowlers[i]] = 0
                outliers[bowlers[i]] += 1

res = sorted( ((v,k) for k,v in outliers.items()), reverse=True)
for i in res:
    print(i)



#print(total_runs * 6 / total_balls)    
    
##batters = {}
##bowlers = {}
##
##for inn in dicti['innings']:
##    for over in inn['overs']:
##        for dlv in over['deliveries']:
##            # Add player if not encountered yet
##            if dlv['batter'] not in batters:
##                batters[dlv['batter']] = {'runs':0, 'balls':0}
##            if dlv['bowler'] not in bowlers:
##                bowlers[dlv['bowler']] = {'runs':0, 'balls':0}
##
##            # Calculate balls added to batter and bowler for this delivery
##            if 'extras' not in dlv or ('wides' not in dlv['extras'] and 'no ball' not in dlv['extras']):
##                batters[dlv['batter']]['balls'] += 1
##                bowlers[dlv['bowler']]['balls'] += 1
##            # Calculate runs added to batter and bowler for this delivery
##            batters[dlv['batter']]['runs'] += dlv['runs']['batter']
##            bowlers[dlv['bowler']]['runs'] += dlv['runs']['batter']
##
##            if 'extras' in dlv and 'byes' not in dlv['extras'] and 'legbyes' not in dlv['extras']:
##                bowlers[dlv['bowler']]['runs'] += dlv['runs']['extras']
##                                
###print(batters)
###print(bowlers)
##
##for bat in batters:
##    print(bat + ': ' + str(batters[bat]['runs']) + '(' + str(batters[bat]['balls']) + ')')
##for bowl in bowlers:
##    print(bowl + ': ' + str(round(bowlers[bowl]['runs'] * 6 / bowlers[bowl]['balls'], 2)))
