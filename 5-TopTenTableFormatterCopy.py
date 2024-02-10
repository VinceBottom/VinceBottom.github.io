import pandas as pd
from tabulate import tabulate
import os
os.chdir("C:\\Users\\Vince\\Downloads")
df1 = pd.read_csv("SeasonExport2-10-2024v7.csv",header=None)
os.chdir("C:\\Users\\Vince\\Desktop\\Fantasy Volleyball Website")
df1 = df1.iloc[1:, :]
df1 = df1.iloc[0:10, :]
df1.drop(df1.columns[0],axis=1,inplace=True)
#print(df1)
table = tabulate(df1,tablefmt="html",showindex=False)
sliced_table = table[15:]##remove wrong tags from start
clean_table = sliced_table[:-17]##remove wrong tags from end
print(clean_table)
os.remove("TopTenTable.html")##removefile
f = open("TopTenTable.html", "w")
f.write('<link rel="stylesheet" href="TopTenTableStyles.css">' + '\n')
f.write('<script type="text/javascript" src="TopTenTableScript.js"></script>' + '\n')
f.write('<table id="TopTen">' + '\n')
f.write('<input type="text" id="myInput" onkeyup="searchTable()" placeholder="Search for player names">' + '\n')
f.write('<tr>' + '\n')
f.write('<th class="heading" onclick="sortTable(0)">Player<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(1)">Team<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(2)">Pos<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(3)">Pts/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(4)">Kills/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(5)">Assists/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(6)">Digs/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(7)">Blocks/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(8)">Perf Pass/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(9)">Aces/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(10)">Errors/M<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(11)">Szn Pts<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('</tr>' + '\n')
f.write(clean_table)
f.write('</table')
f.close()