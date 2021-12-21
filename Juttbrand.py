import os, sys, re, time, datetime, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
os.system('termux-setup-storage')
bit=platform.architecture()[0]
logo = """\n\x1b[1;91m\n\x1b[1;92m\n\x1b[1;96m\n\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}\n\x1b[1;97m         {|} {|}  {|}    {|}       {|}\n\x1b[1;93m         {|} {|}  {|}    {|}       {|}\n\x1b[1;96m         {|} {|}  {|}    {|}       {|}\n\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}\n\x1b[1;93m\n\x1b[1;92m             Jutt Badshah Brand~\n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah\n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/SHOOTER-MAKER\n\x1b[1;97m\xe2\x9e\xa3 WP  NO : +923007574310\n\x1b[1;91m-----------------------------------------------"""

def test():
    os.system('clear')
    print logo
    print ('\033[1;33mMethod Select Menu\033[0;97m')
    print (47*'-')
    print ('\033[1;32m[1] Method Wifi\n')
    print ('\033[1;32m[2] Method Sim Data\033[0;97m')
    print (47*'-')
    gg = raw_input('Select Method: \033[0;97m')
    if gg == '1':
        if bit == '64bit':
            from wifi64 import reg
            reg()
        elif bit == '32bit':
            from wifi32 import reg
            reg()
    elif gg == '2':
        if bit == '64bit':
            from Jutt import reg
            reg()
        elif bit == '32bit':
            from brand import reg
            reg()
    else:
        print ('Select Valid Option')
        time.sleep(2)
        test()

test()
