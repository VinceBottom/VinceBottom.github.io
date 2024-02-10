import pandas as pd
from tabulate import tabulate
import os
from datetime import datetime
os.chdir("C:\\Users\\Vince\\Downloads")
AnnaTable = pd.read_csv("Team1.csv",header=None)
LaurenTable = pd.read_csv("Team2.csv",header=None)
MadiTable = pd.read_csv("Team3.csv",header=None)
MikeTable = pd.read_csv("Team4.csv",header=None)
ShaunaTable = pd.read_csv("Team5.csv",header=None)
TimTable = pd.read_csv("Team6.csv",header=None)
VincentTable = pd.read_csv("Team7.csv",header=None)
##drop first column which is meaningless
AnnaTable.drop(AnnaTable.columns[0],axis=1,inplace=True)
LaurenTable.drop(LaurenTable.columns[0],axis=1,inplace=True)
MadiTable.drop(MadiTable.columns[0],axis=1,inplace=True)
MikeTable.drop(MikeTable.columns[0],axis=1,inplace=True)
ShaunaTable.drop(ShaunaTable.columns[0],axis=1,inplace=True)
TimTable.drop(TimTable.columns[0],axis=1,inplace=True)
VincentTable.drop(VincentTable.columns[0],axis=1,inplace=True)
list_teams = [AnnaTable,LaurenTable,MadiTable,MikeTable,ShaunaTable,TimTable,VincentTable]
os.chdir("C:\\Users\\Vince\\Desktop\\Fantasy Volleyball Website")
Name1 = "AnnaTable"
Name2 = "LaurenTable"
Name3 = "MadiTable"
Name4 = "MikeTable"
Name5 = "ShaunaTable"
Name6 = "TimTable"
Name7 = "VincentTable"
count = 0
NameList = [Name1,Name2,Name3,Name4,Name5,Name6,Name7]
for x in list_teams:
    df1 = x.iloc[1:, :].copy()
    df1 = df1.iloc[0:10, :].copy()
    Name = NameList[count]
    #print(df1)
    table = tabulate(df1,tablefmt="html",showindex=False)
    sliced_table = table[15:]##remove wrong tags from start
    clean_table = sliced_table[:-17]##remove wrong tags from end
    #print(clean_table)
    os.remove(str(Name) + '.html')
    ##calculate today to add later to update time
    f = open(str(Name) + ".html", "w")
    f.write('<link rel="stylesheet" href="TeamTableStyles.css">' + '\n')
    f.write('<script type="text/javascript" src="TeamTableScript.js"></script>' + '\n')
    f.write('<table id="TeamTable">' + '\n')
    f.write('<tr>' + '\n')
    f.write('<th class="heading" onclick="sortTable(0)">Slot<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(1)">Name<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(2)">Team<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(3)">Pts/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(4)">Szn Pts<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(5)">Kills/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(6)">Assists/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(7)">Digs/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(8)">Blocks/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(9)">Perf Pass/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(10)">Aces/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('<th class="heading" onclick="sortTable(11)">Errors/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
    f.write('</tr>' + '\n')
    f.write(clean_table)
    f.write('</table>' + '\n')
    f.close()
    count+=1