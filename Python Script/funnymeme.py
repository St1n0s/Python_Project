import webbrowser

url = "https://www.youtube.com/watch?v=R51P599MxyA"
webbrowser.open(url)

import webbrowser
import requests
import time

r = requests.get('https://www.youtube.com/watch?v=R51P599MxyA')

def myfunction():
    start = time.time()
    while time.time() < start + 5:
        (webbrowser.open_new_tab(r.url))
    return
