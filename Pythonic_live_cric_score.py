# More Pythonic way to get cricket score 
import requests
import pynotify
import re
from time import sleep
import json
from notify_run import Notify
from bs4 import BeautifulSoup 

def push_notification(pnmsg):
  notify = Notify()
  notify.send(pnmsg)
    
  print("HEY jatin, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
 
  print("Check again after an hour.")
  
  
  def cricscore():
    url = "https://www.espn.in/cricket/series/19312/game/1187013/india-vs-bangladesh-1st-t20i-bangladesh-in-india-2019-20"
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    r = requests.get(url)
    while r.status_code is  200:
        page = requests.get(url)
        soup= BeautifulSoup(page.content,'html.parser')
        push_notification(soup.title)
    sleep(100)
    
  cricscore()
  
  
