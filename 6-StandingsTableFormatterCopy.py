import pandas as pd
from tabulate import tabulate
import os
from datetime import datetime
os.chdir("C:\\Users\\Vince\\Downloads")
df1 = pd.read_csv("standings2.csv",header=None)
os.chdir("C:\\Users\\Vince\\Desktop\\Fantasy Volleyball Website")
df1 = df1.iloc[1:, :]
df1 = df1.iloc[0:10, :]
#print(df1)
table = tabulate(df1,tablefmt="html",showindex=False)
sliced_table = table[15:]##remove wrong tags from start
clean_table = sliced_table[:-17]##remove wrong tags from end
#print(clean_table)
os.remove("StandingsTable.html")##removefile
##calculate today to add later to update time
today = datetime.now()
today_format = today.strftime('%A, %B %d %Y')
time = datetime.now()
time_format = time.strftime('%I:%M%p')
f = open("StandingsTable.html", "w")
f.write('<link rel="stylesheet" href="StandingsTableStyles.css">' + '\n')
f.write('<script type="text/javascript" src="StandingsTableScript.js"></script>' + '\n')
f.write('<table id="Standings">' + '\n')
f.write('<tr>' + '\n')
f.write('<th class="heading" onclick="sortTable(0)">Team<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(1)">Szn Pts<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(2)">Kills/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(3)">Assists/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(4)">Digs/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(5)">Perf Pass/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(6)">Blocks/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(7)">Aces/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(8)">Errors/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('<th class="heading" onclick="sortTable(9)">Pts/Match<img class="icon" src="sorticon2.png" height=17 width=15 alt="Sort by column icon"/></th>' + '\n')
f.write('</tr>' + '\n')
f.write(clean_table)
f.write('</table>' + '\n')
datetimestring = "Last updated on " + str(today_format) + " at " + str(time_format)
f.write('<p style="font-style:italic;">' + datetimestring + '</p>')
f.close()