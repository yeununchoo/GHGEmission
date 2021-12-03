import time
import os

update_command = """python Dynamic_Update.py"""

for each_day in range(7):
    os.system(update_command)
    time.sleep(24*60*60)
    
    