from requests import get
import pandas as pd
import difflib
import os
import string
import cloudscraper
import os
import re
import json
os.chdir("C:\\Users\\Vince\\Downloads")
from playwright.sync_api import sync_playwright
export_filename = 'grandrapidsatlanta.txt'
from bs4 import BeautifulSoup
##declare user agent
# with sync_playwright() as p:
#     #for browser_type in [p.chromium, p.firefox, p.webkit]:
#     for browser_type in [p.firefox]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://widgets.volleystation.com/play-by-play/2125267?side_force=home&amp;home_image=https:%2F%2Fpls-api.fra1.cdn.digitaloceanspaces.com%2Fwebsite%2Fteams%2F2109696%2Fbadge.svg&amp;away_image=https:%2F%2Fpls-api.fra1.cdn.digitaloceanspaces.com%2Fwebsite%2Fteams%2F2109694%2Fbadge.svg')
#         #print(page.inner_text('*'))
#         print(page.locator.all_text_contents())
#         #soup = BeautifulSoup(page.content())
#         browser.close()
f = open("Game7.txt", "r")
data = f.read()
f.close()
soup = BeautifulSoup(data)
#print(soup)
# digs = soup.find(string="Dig")
names = soup.find_all(['span','div'], class_=['player-name','player','skill','description','effect'])
skills = soup.find_all('span', class_=['skill','description'])
length_n = len(names)
length_s = len(skills)
print(length_s)
#print(length_n)
#print(length_s)
# print(length_s)
# print(length_n)
namescount = 0
skillscount = 0
##use names with all other elements to build a list and get rid of names that do not have a skill or description after them
list_names = []
count = 0
nextcount = 1
f = open(export_filename, "a")
f.write('Name,Action,Effect,' + '\n')
f.close()
for x in range(length_n):
    name1 = names[count]
    name2 = names[nextcount]
    #print(name1)
    namestr = names[count].text
    namestr = namestr.strip()
    namestr = namestr.replace('\n', '')
    #print(name1.attrs['class'])
    name1class = name1.attrs['class'][0]
    name1class = str(name1class)
    if name2.attrs['class'][0] == 'skill':
        if name1class == 'player-name':
            thirdcount = nextcount + 1
            thirdact = names[thirdcount]
            if thirdact.attrs['class'][0] == 'effect':
                #list_names.append(namestr)
                effect = thirdact.text
                effect = str(effect)
                count += 1
                nextcount += 1
                f = open(export_filename, "a")
                f.write(namestr + ',' + str(name2.text) + ',' + effect + ',' + '\n')
                f.close()
            else:
                f = open(export_filename, "a")
                f.write(namestr + ',' + str(name2.text) + ',' + 'Success' + ',' + '\n')
                f.close()
                count += 1
                nextcount += 1
        else:
            count += 1
            nextcount += 1
    elif name1class == 'description':
        if name2.attrs['class'][0] == 'player-name':
            print('yes')
            list_names.append(namestr)
            count += 1
            nextcount += 1
            f = open(export_filename, "a")
            f.write(str(name2.text) + ',' + namestr + ',' + ' ,' '\n')
            f.close()
            print(namestr)
        else:
            count += 1
            nextcount += 1
    else:
        count += 1
        nextcount += 1
        #print(namestr)
        #print(next_item)
        # if names[count].findNext.name != 'div':
        #     list_names.append(names[count])
        #
        # else:
        #     count += 1
print(len(list_names))
#print(len(list_names))
# s = open("PlayByPlayData.txt", 'a')
# s.write('Name,Skill' + '\n')
# s.close()
# for x in range(length_n):
#     name = str(names[namescount].text)
#     name = name.strip()
#     name = name.replace('\n', '')
#     skill = str(skills[skillscount].text)
#     s = open("PlayByPlayData.txt", 'a')
#     s.write(name + ',' + skill + ',' + '\n')
#     s.close()
#     namescount += 1
#     skillscount += 1
# str_soup = str(soup)
# print(str_soup)
# f = open("exportpbp.txt", 'w')
# f.write(str_soup)
# f.close()
# names = soup.find('body', class_='theme-auto')
# print(soup.find_all('div'))
#print(names.findChildren())