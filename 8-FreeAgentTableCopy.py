import pandas as pd
from tabulate import tabulate
import os
from datetime import datetime
os.chdir("C:\\Users\\Vince\\Downloads")
df1 = pd.read_csv("freeagent2-10-2024v8.csv",header=None)
os.chdir("C:\\Users\\Vince\\Desktop\\Fantasy Volleyball Website")
df1 = df1.iloc[1:, :]
df1.drop(df1.columns[0],axis=1,inplace=True)
##replace nan for healthy players in injury status
df1.fillna('',inplace=True)
#print(df1)
table = tabulate(df1,tablefmt="html",showindex=False)
sliced_table = table[15:]##remove wrong tags from start
clean_table = sliced_table[:-17]##remove wrong tags from end
#print(clean_table)
os.remove("FreeAgentTable.html")##removefile
f = open("FreeAgentTable.html", "w")
f.write('<link rel="stylesheet" href="FreeAgentTableStyles.css">' + '\n')
f.write('<script type="text/javascript" src="FreeAgentTableScript.js"></script>' + '\n')
f.write('<table id="FreeAgentTable">' + '\n')
f.write('<tr>' + '\n')
f.write('<th class="heading" onclick="sortTable(0)">Name<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(1)">Team<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(2)">Pos<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(3)">Injury Status<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(4)">Pts/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(5)">Kills/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(6)">Assists/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(7)">Digs/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(8)">Blocks/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(9)">Perf Pass/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(11)">Aces/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(12)">Errors/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(13)">Szn Pts<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('</tr>' + '\n')
f.write(clean_table)
f.write('</table>' + '\n')
f.close()