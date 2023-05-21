import json
import sys
import os

files = os.listdir('ipl_cricsheet')

total_games = 0
btr = sys.argv[1]

batter = {}
for f in files:
    if f == 'README.txt':
        continue
    with open('ipl_cricsheet/' + f, 'r') as json_file:
        dicti = json.load(json_file)
    
    # Find player
    found = False
    for team in dicti['info']['players']:
        for p in dicti['info']['players'][team]:
            if btr in p:
                found = True;
                break;
    if not found:
        continue

    ssn = str(dicti['info']['season'])
    if (ssn not in batter):
        batter[ssn] =  {'runs': 0, 'balls': 0, 'wickets': 0, 'boundaries' : 0, 'dot balls': 0}

    for inn in dicti['innings']:
        for over in inn['overs']:
            for dlv in over['deliveries']:
                if dlv['batter'] != btr:
                    continue
                
                # Calculate balls added to batter and bowler for this delivery
                if 'extras' not in dlv or 'no ball' in dlv['extras']:
                    batter[ssn]['balls'] += 1
                # Calculate runs added to batter and bowler for this delivery
                batter[ssn]['runs'] += dlv['runs']['batter']
                if dlv['runs']['batter'] == 0:
                    batter[ssn]['dot balls'] += 1
                elif dlv['runs']['batter'] >= 4:
                    batter[ssn]['boundaries'] += 1
                
                # Calculate wickets added to bowler for this delivery
                if 'wickets' in dlv:
                    batter[ssn]['wickets'] += 1
# print(batter)
# print(batter.keys())
for ssn in sorted(batter.keys()):
    if (batter[ssn]['balls'] == 0 or batter[ssn]['boundaries'] == 0 or batter[ssn]['dot balls'] == 0): continue
    print(ssn + ' Runs: ' + str(batter[ssn]['runs']) + ' Avg: ' + str(round(batter[ssn]['runs']/batter[ssn]['wickets'], 2)) + ' ' + 'SR: ' + str(round(batter[ssn]['runs']*100/batter[ssn]['balls'], 2)) 
+ ' ' + 'DBP: ' + str(round(batter[ssn]['dot balls']*100/batter[ssn]['balls'], 2))
+ ' ' + 'BPB: ' + str(round(batter[ssn]['balls']/batter[ssn]['boundaries'], 2)))
    
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
