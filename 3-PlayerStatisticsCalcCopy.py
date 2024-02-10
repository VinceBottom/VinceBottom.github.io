from requests import get
import pandas as pd
import difflib
import os
import string
import cloudscraper
import os
import re
import json
import openpyxl
import numpy as np
os.chdir("C:\\Users\\Vince\\Downloads")
allTableExportName = 'SeasonExport2-10-2024v7.csv'
teamTableExportName = 'TeamExport1.csv'
##load data
df1 = pd.read_csv("Game1StatSheet.csv")
df2 = pd.read_csv("Game2StatSheet.csv")
df3 = pd.read_csv("Game3StatSheet.csv")
df4 = pd.read_csv("Game4StatSheet.csv")
df5 = pd.read_csv("Game5StatSheet.csv")
df6 = pd.read_csv("Game6StatSheet.csv")
df7 = pd.read_csv("Game7StatSheet.csv")
allroster = pd.read_csv("allroster.csv")
##concat together
fulldf = pd.concat([df1,df2,df3,df4,df5,df6,df7])
fulldf['Points'] = (fulldf['Kills'] + fulldf['Perfect Passes'] + fulldf['Digs'] +
                    fulldf['Aces'] + fulldf['Assists']*0.5 + fulldf['Blocks'] -
                    fulldf['Errors'])
##calculate player stats
totalpoints = fulldf.groupby(['Name'])['Perfect Passes','Kills','Digs','Aces','Assists','Blocks','Errors','Points'].sum().reset_index()
##add in roster data- position and team
names = allroster['Name']
allroster['NameList'] = names.str.split(' ',1)
allroster['First Name'] = allroster['NameList'].apply(lambda x: x[0])
allroster['Last Name'] = allroster['NameList'].apply(lambda x: x[1])
##eliminate last name spaces in both dfs
allroster['Last Name'] = allroster['Last Name'].str.replace(' ','')
allroster['Full Name'] = allroster['First Name'] + ' ' + allroster['Last Name']
##create abbv name in allroster
allroster['AbbvName'] = allroster['First Name'].str.slice(stop=1) + '.' + allroster['Last Name']
##make position abbreviations in all roster df
allroster.loc[(allroster['Position2']=='Middle Blocker', 'Position')]= 'MB'
allroster.loc[(allroster['Position2']=='Libero', 'Position')]= 'L'
allroster.loc[(allroster['Position2']=='Outside Hitter', 'Position')]= 'OH'
allroster.loc[(allroster['Position2']=='Opposite', 'Position')]= 'OPP'
allroster.loc[(allroster['Position2']=='Setter', 'Position')]= 'S'
allroster.loc[(allroster['Position2']=='Setter/Libero', 'Position')]= 'S/L'
print(allroster['AbbvName'].value_counts())
##clean up all roster dataset
newallroster = allroster[['Full Name','AbbvName','Position','Team']]
##
gpdf = newallroster.merge(fulldf,how='outer',left_on='AbbvName',right_on='Name',indicator='Combine')
newdf = gpdf[gpdf['Combine']!='left_only']
dedup = newdf.drop_duplicates(subset=['Team','Date'],keep='first')
totalsets = dedup.groupby(['Team'])['Sets'].sum().reset_index()
print(totalsets)
##calculate matches played
gamesplayed = dedup.value_counts(['Team'])
gamesplayeddf = pd.DataFrame(gamesplayed.reset_index().values, columns=['Team','MatchesPlayed'])
##mergedf
allrosterdf2 = allroster.merge(totalsets,how='outer',on='Team')
allrosterdf = allrosterdf2.merge(gamesplayeddf,how='outer',on='Team')
totalpoints['Name'] = totalpoints['Name'].str.replace(' ','')
allstatscleaned = allrosterdf.merge(totalpoints,how='outer',left_on='AbbvName',right_on='Name',indicator='Drops')
allstatsdf = allstatscleaned[allstatscleaned['Drops']!='left_only']
print(allstatsdf)
#allstatsdf.to_csv("allstatsfixerrors7.csv")
##now make per set values to upload
allstatsdf['Kills/Match'] = allstatsdf['Kills']/allstatsdf['Sets']*4
allstatsdf['Assists/Match'] = allstatsdf['Assists']/allstatsdf['Sets']*4
allstatsdf['Digs/Match'] = allstatsdf['Digs']/allstatsdf['Sets']*4
allstatsdf['Blocks/Match'] = allstatsdf['Blocks']/allstatsdf['Sets']*4
allstatsdf['Perfect Passes/Match'] = allstatsdf['Perfect Passes']/allstatsdf['Sets']*4
allstatsdf['Aces/Match'] = allstatsdf['Aces']/allstatsdf['Sets']*4
allstatsdf['Errors/Match'] = allstatsdf['Errors']/allstatsdf['Sets']*4
allstatsdf['Fantasy Points/Set'] = allstatsdf['Points']/allstatsdf['Sets']
allstatsdf['Fantasy Points/Match'] = allstatsdf['Points']/allstatsdf['Sets']*4
##
allstatsdf['Fantasy Points/Match'] = np.round(allstatsdf['Fantasy Points/Match'],0).astype(int)
allstatsdf['Kills/Match'] = np.round(allstatsdf['Kills/Match'],0).astype(int)
allstatsdf['Assists/Match'] = np.round(allstatsdf['Assists/Match'],0).astype(int)
allstatsdf['Digs/Match'] = np.round(allstatsdf['Digs/Match'],0).astype(int)
allstatsdf['Blocks/Match'] = np.round(allstatsdf['Blocks/Match'],0).astype(int)
allstatsdf['Perfect Passes/Match'] = np.round(allstatsdf['Perfect Passes/Match'],0).astype(int)
allstatsdf['Aces/Match'] = np.round(allstatsdf['Aces/Match'],0).astype(int)
allstatsdf['Errors/Match'] = np.round(allstatsdf['Errors/Match'],0).astype(int)
allstatsdf['Total Pts'] = np.round(allstatsdf['Fantasy Points/Match'],0).astype(int).mul(allstatsdf['MatchesPlayed'].astype(int),axis='index')
print(allstatsdf['Team'])
##merge that in to add games played as a column
alltableexport = allstatsdf[['Name_x','Fantasy Team','Position','Fantasy Points/Match','Kills/Match','Assists/Match','Digs/Match',
                          'Blocks/Match','Perfect Passes/Match','Aces/Match',
                          'Errors/Match','Total Pts','Team']]
alltableexport.rename(columns={'Name_x':'Name','MatchesPlayed':'Matches Played'},inplace=True)
alltableexport.sort_values(by='Fantasy Points/Match',inplace=True,ascending=False)
alltableexport['Fantasy Team'].fillna('Free Agent',inplace=True)
freeagentrough = alltableexport.copy()
print(freeagentrough)
alltableexport.drop(columns='Team',inplace=True)
#alltableexport.to_csv(allTableExportName)
teamtablerough = allstatsdf[['Name_x','Team','Position','Fantasy Points/Match','Kills/Match','Assists/Match','Digs/Match',
                          'Blocks/Match','Perfect Passes/Match','Aces/Match',
                          'Errors/Match','Sets','MatchesPlayed','Total Pts','Fantasy Team']]
teamtablerough.rename(columns={'Name_x':'Name','MatchesPlayed':'Matches Played'},inplace=True)
teamtableclean = teamtablerough[teamtablerough['Fantasy Team'].isna()==False]
teamtableclean.sort_values(by='Position',inplace=True,ascending=False)
teamexport = teamtableclean[['Position','Name','Team','Fantasy Points/Match','Total Pts','Kills/Match','Assists/Match','Digs/Match','Blocks/Match','Perfect Passes/Match','Aces/Match','Errors/Match','Fantasy Team']]
AnnaTable = teamexport[teamexport['Fantasy Team']=='Oreo Cakesters']
LaurenTable = teamexport[teamexport['Fantasy Team']=="Screebie's Deebies"]
MadiTable = teamexport[teamexport['Fantasy Team']=='Madi']
MikeTable = teamexport[teamexport['Fantasy Team']=='Mike']
ShaunaTable = teamexport[teamexport['Fantasy Team']=='Shauna']
TimTable = teamexport[teamexport['Fantasy Team']=='Tim']
VincentTable = teamexport[teamexport['Fantasy Team']=='Bikini Kills']
AnnaTable.drop(columns='Fantasy Team',inplace=True)
LaurenTable.drop(columns='Fantasy Team',inplace=True)
MadiTable.drop(columns='Fantasy Team',inplace=True)
MikeTable.drop(columns='Fantasy Team',inplace=True)
ShaunaTable.drop(columns='Fantasy Team',inplace=True)
TimTable.drop(columns='Fantasy Team',inplace=True)
VincentTable.drop(columns='Fantasy Team',inplace=True)
##add in os.remove() later
# AnnaTable.to_csv("Team1.csv")
# LaurenTable.to_csv("Team2.csv")
# MadiTable.to_csv("Team3.csv")
# MikeTable.to_csv("Team4.csv")
# ShaunaTable.to_csv("Team5.csv")
# TimTable.to_csv("Team6.csv")
# VincentTable.to_csv("Team7.csv")
##
freeagent = freeagentrough[freeagentrough['Fantasy Team']=='Free Agent']
freeagent.sort_values(by='Fantasy Points/Match',inplace=True,ascending=False)
##enter free agent injury statuses
freeagent['Injury']=''
freeagent.loc[(freeagent['Name']=='Alli Linnehan', 'Injury')]= '+'
freeagentclean = freeagent[['Name','Team','Position','Injury','Fantasy Points/Match','Kills/Match','Assists/Match','Digs/Match',
                           'Blocks/Match','Perfect Passes/Match','Aces/Match',
                           'Errors/Match','Total Pts']]
freeagentclean.to_csv("freeagent2-10-2024v8.csv")
#print(teamtableclean)
##
##
standingstable = teamtableclean
# standingstable['Kills'] = standingstable['Kills/Match']*standingstable['Matches Played']
# standingstable['Assists'] = standingstable['Assists/Match']*standingstable['Matches Played']
# standingstable['Digs'] = standingstable['Digs/Match']*standingstable['Matches Played']
# standingstable['Blocks'] = standingstable['Digs/Match']*standingstable['Matches Played']
# standingstable['Perf Passes'] = standingstable['Perfect Passes/Match']*standingstable['Matches Played']
# standingstable['Aces'] = standingstable['Aces/Match']*standingstable['Matches Played']
# standingstable['Errors'] = standingstable['Errors/Match']*standingstable['Matches Played']
standingsdf = standingstable.groupby(['Fantasy Team']).sum('Total Pts')
print(standingsdf)
standingsclean = standingsdf[['Total Pts','Kills/Match','Assists/Match','Digs/Match','Perfect Passes/Match',
                              'Blocks/Match','Aces/Match','Errors/Match','Fantasy Points/Match']]
standingsclean.sort_values(by='Total Pts',inplace=True,ascending=False)
standingsclean.to_csv("standings2.csv")
#allstatsdf.fillna(value=0,inplace=True)
##export


