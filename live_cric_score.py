import requests
import pynotify
import re
from time import sleep
import json
from notify_run import Notify

def push_notification(pnmsg):
  notify = Notify()
  notify.send(pnmsg)
  
 def getscore():
    url = "https://www.espncricinfo.com/series/19430/game/1187009/india-vs-south-africa-3rd-test-icc-world-test-championship-2019-2021"
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)
    data = json.loads(r.text)
    player_status = data['match']['current_summary'].strip()
    team1_name = data['other_scores']['international'][0]['team1_name'].strip()
    team1_score = data['other_scores']['international'][0]['team1_desc'].replace('&nbsp;ov',' ov').strip()
    team2_name = data['other_scores']['international'][0]['team2_name'].strip()
    team2_score = data['other_scores']['international'][0]['team2_desc'].replace('&nbsp;ov',' ov').strip()
    if not team1_score:
        team1_score = 'Yet to bat'
    if not team2_score:
        team2_score = 'Yet to bat'
    score = str(team1_name) + ' : ' + str(team1_score) + '\n\n' + str(team2_name) + ' : ' + str(team2_score)
    player_status = re.sub(r'.*ov,','', str(player_status))
    score = score + '\nPlayer status: ' + player_status
    push_notification("Score Board:-", score)
    sleep(120)
if __name__ == "__main__":
    while True:
        getscore()
        
