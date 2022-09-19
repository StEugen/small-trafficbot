import webbrowser
import time
import os


x = int(input('How many times: '))
sites = input('Enter URL of sites (remember to put comma between): ')
web_page = sites.split(', ')


for j in range(x*2):
    for i in range(j):
        webbrowser.open(web_page[i])
        time.sleep(4)

