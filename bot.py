import webbrowser
import time


print('How many times: ')
x = int(input())
print('What site: ')
web_page = input()
for i in range(x):
	webbrowser.open(web_page)
	time.sleep(20)

	
	
