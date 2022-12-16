import json
import sys
import os

narine = [[0]*20]*11
for i in narine:
    print(i)
total_runs = 0
total_balls = 0
bwlr = 'SP Narine'
files = os.listdir('ipl_cricsheet')

total_games = 0

for f in files:
    if f == 'README.txt':
        continue
    with open('ipl_cricsheet/' + f, 'r') as json_file:
        dicti = json.load(json_file)
    
    # Find player
    found = False
    for team in dicti['info']['players']:
        if bwlr in dicti['info']['players'][team]:
            found = True
    if not found:
        continue

    bowler = {'runs': 0, 'balls': 0, 'wickets': 0}
    for inn in dicti['innings']:
        for over in inn['overs']:
            for dlv in over['deliveries']:
                if dlv['bowler'] != bwlr:
                    continue
                
                # Calculate balls added to batter and bowler for this delivery
                if 'extras' not in dlv or ('wides' not in dlv['extras'] and 'no ball' not in dlv['extras']):
                    bowler['balls'] += 1
                # Calculate runs added to batter and bowler for this delivery
                bowler['runs'] += dlv['runs']['batter']
                # Calculate wickets added to bowler for this delivery
                if 'wickets' in dlv and dlv['wickets'][0]['kind'] != 'run out':
                    bowler['wickets'] += 1

                if 'extras' in dlv and 'byes' not in dlv['extras'] and 'legbyes' not in dlv['extras']:
                    bowler['runs'] += dlv['runs']['extras']
        break;

    print(bowler['wickets'])
                                    
    
    if bowler['balls'] == 0:
        continue;
    total_runs += bowler['runs']
    total_balls += bowler['balls']
    total_games += 1
##    print(str(bowler['wickets']) + ', ' + str(int(bowler['runs'] * 6 / bowler['balls'])))
    narine[bowler['wickets']][int(bowler['runs'] * 6 / bowler['balls'])] += 1

print(total_games)
for i in range(len(narine)):
    row = ''
    for j in range(len(narine[i])):
##        row += str(narine[i][j]) + '\t'
        narine[i][j] /= total_games
        narine[i][j] = round(narine[i][j], 3)
        row += str(narine[i][j]) + '\t'
##        print(j)
##    print(row)
for i in narine:
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
