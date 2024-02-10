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
sets = input("Please enter number of the sets for this match: ")
sets = int(sets)
export_filename = 'Game7StatSheet.csv'
##load data
fulldf = pd.read_csv("Game7PBP.csv")
##
##calculate assists
fulldf['True Action'] = fulldf['Action'] + ' ' + fulldf['Effect']
fulldf.loc[(fulldf['Effect']==' error', 'True Action')]= 'Error'
#print(fulldf['True Action'].value_counts())
#print(fulldf)
##build assists checking list
assists_list = fulldf['True Action'].to_list()
print(assists_list)
#print(assists_list)
length = len(assists_list)
count = 0
assist_location_list = []
for x in range(length):
    nextcount = count + 1#actual count of position to use (0+1)
    thirdcount = nextcount + 1
    fourthcount = thirdcount + 1
    action = assists_list[count]
    action = action.strip()
    if action=='Setting':
        action2 = assists_list[nextcount]
        action2 = action2.strip()
        if action2=='Attack':
            action3 = assists_list[thirdcount]
            action3 = action3.strip()
            if action3=='Player scored':
                assist_location_list.append(count)
                #print(nextcount)
                count += 1
            elif action3=='Error':
                action4 = assists_list[fourthcount]
                action4 = action4.strip()
                if action4=='Player scored':
                    assist_location_list.append(count)
                    #print(nextcount)
                    count += 1
                else:
                    count += 1
            else:
                count += 1
        else:
            count += 1
    else:
        count += 1
fulldf['Assist'] = ''
for x in assist_location_list:
    fulldf.at[x, 'Assist'] = 'Yes'
assists_df = fulldf[fulldf['Assist']=='Yes']
assistvalues = assists_df.value_counts(['Name'])
newassistsdf = pd.DataFrame(assistvalues.reset_index().values, columns=['Name','Assists'])
##aces calculation
count = 0
ace_location_list = []
for x in range(length):
    nextcount = count + 1#actual count of position to use (0+1)
    thirdcount = nextcount + 1
    action = assists_list[count]
    action = action.strip()
    #print(action)
    if action=='Serve':
        #print('serve')
        action2 = assists_list[nextcount]
        action2 = action2.strip()
        if action2=='Player Scored':
            ace_location_list.append(count)
            #print(count)
            count += 1
        elif action2=='Error':
            action3 = assists_list[thirdcount]
            action3 = action3.strip()
            if action3=='Player scored':
                ace_location_list.append(count)
                #print(count)
                count += 1
            else:
                count += 1
        else:
            count += 1
    else:
        count += 1
fulldf['Ace'] = ''
for x in ace_location_list:
    #print(x)
    fulldf.at[x, 'Ace'] = 'Yes'
#print(fulldf['Ace'].value_counts(['Name']))
aces_df = fulldf[fulldf['Ace']=='Yes']
acevalues = aces_df.value_counts(['Name'])
newacesdf = pd.DataFrame(acevalues.reset_index().values, columns=['Name','Aces'])
#print(aces_df.value_counts(['Name']))
# fulldf.to_csv('fulldfcheck2.csv')
##calculate digs
##digs calculation
digsdf = fulldf[fulldf['True Action']=='Dig  ']
digvalues = digsdf.value_counts(['Name'])
newdigsdf = pd.DataFrame(digvalues.reset_index().values, columns=['Name','Digs'])
##kills calculation
count = 0
kill_location_list = []
for x in range(length):
    nextcount = count + 1#actual count of position to use (0+1)
    thirdcount = nextcount + 1
    action = assists_list[count]
    action = action.strip()
    #print(action)
    if action=='Attack':
        #print('serve')
        action2 = assists_list[nextcount]
        action2 = action2.strip()
        if action2=='Player scored':
            kill_location_list.append(count)
            count+=1
        elif action2=='Error':
            action3 = assists_list[thirdcount]
            action3 = action3.strip()
            if action3=='Player scored':
                kill_location_list.append(count)
                count += 1
            else:
                count += 1
        else:
            count += 1
    else:
        count += 1
fulldf['Kill'] = ''
for x in kill_location_list:
    #print(x)
    fulldf.at[x, 'Kill'] = 'Yes'
kills_df = fulldf[fulldf['Kill']=='Yes']
killvalues = kills_df.value_counts(['Name'])
newkilldf = pd.DataFrame(killvalues.reset_index().values, columns=['Name','Kills'])
#print(kills_df.value_counts(['Name']))
#print(fulldf['True Action'].value_counts())
passdf = fulldf[fulldf['True Action']=='Pass  perfect']
passvalues = passdf.value_counts(['Name'])
newpassdf = pd.DataFrame(passvalues.reset_index().values, columns=['Name','Perfect Passes'])
##calculate blocks
print(fulldf['True Action'].value_counts())
block_df = fulldf[fulldf['True Action']=='Block  ']
blockvalues = block_df.value_counts(['Name'])
blockdf = pd.DataFrame(blockvalues.reset_index().values, columns=['Name','Blocks'])
##calculate errors
first_df = fulldf[fulldf['True Action']=='Error']
errors_df = first_df[first_df['Action']!='Block']
errorvalues = errors_df.value_counts(['Name'])
newerrordf = pd.DataFrame(errorvalues.reset_index().values, columns=['Name','Errors'])
##merge back into roster dataset to get values per player
# print(newpassdf)
# print(newkilldf)
# print(newdigsdf)
# print(newacesdf)
# print(newassistsdf)
# print(blockdf)
# print(newerrordf)
merge1 = pd.merge(newpassdf,newkilldf,how='outer',on='Name')
merge2 = pd.merge(merge1,newdigsdf,how='outer',on='Name')
merge3 = pd.merge(merge2,newacesdf,how='outer',on='Name')
merge4 = pd.merge(merge3,newassistsdf,how='outer',on='Name')
merge5 = pd.merge(merge4,blockdf,how='outer',on='Name')
merge6 = pd.merge(merge5,newerrordf,how='outer',on='Name')
finaltallies = merge6.fillna(0)
finaltallies['Sets'] = sets
#finaltallies['Points'] = (finaltallies['Perfect Passes'] + finaltallies['Kills'] + finaltallies['Digs'] + finaltallies['Aces'] +
                        #finaltallies['Assists'] + finaltallies['Blocks'] - finaltallies['Errors'])/sets*3
print(finaltallies)
finaltallies.to_csv(export_filename)