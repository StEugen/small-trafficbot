import webbrowser
import time
import os
import sys


path_to = input('Enter file name: ')
#list_of_url = open(path_to)
x = int(input('How many times: '))
#sites = input('Enter URL of sites (remember to put comma between): ')
with open(path_to) as list_of_url:
    sites = [line.rstrip('\n') for line in list_of_url]
web_page = sites

for j in range(x*2):
    for i in range(j):
        webbrowser.open(web_page[i])
        time.sleep(4)