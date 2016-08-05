from datetime import datetime
import sys
import os
def mv_for_blog(files):
    today=datetime.today()
    repo=today.strftime("%Y-%m-%d_%H-%M-%S")
    command = 'mkdir '+repo
    os.system(command)
    command = 'mv '+files+'* '+repo
    os.system(command)

if len(sys.argv) < 2:
    print 'no argument'
    sys.exit()
else:
    mv_for_blog(sys.argv[1])
