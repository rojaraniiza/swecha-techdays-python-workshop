#python script to fetch the latest cricket score and notify every 5 minute.
#--- usage: python2 cricket_score.py
#!/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test-pricess")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    data = soup.find_all("description")
    score = data[1].text
    sendmessage("Score", score)
    sleep(300)
