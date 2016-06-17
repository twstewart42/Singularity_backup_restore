#!/usr/bin/env python
##moves files from /tmp to /nfs/sing_backup once a week
### 08 17 * * 5 python /usr/local/bin/move_sing_backups.py
import fnmatch
import os
import shutil

def move_files():
	for filef in os.listdir('/tmp/.'):
		if fnmatch.fnmatch(filef, 'sing_back*.csv'):
			print filef
		 	newname='/nfs/sing_backup/%s' % filef
                        print newname
			oldname='/tmp/%s' %filef
			try:
				shutil.move(oldname, newname)

			except:
				print "file already exists"
				continue

if __name__ == '__main__':
        move_files()



