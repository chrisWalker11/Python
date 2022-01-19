import os
url = input('Enter url (you can paste into the prompt by right clicking in the window)\n-> ')
cmd = 'cmd /k "C:\\Users\\Austi\\Music\\youtube-dl.exe -o "C:\\Users\\Austi\\Music\\%(title)s.%(ext)s" -x --audio-format mp3 "' + url
os.system(cmd)
	