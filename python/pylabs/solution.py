user@samal-dimdung3:~/pylabs$ ls
backup  bkupscript.py  mybackup.py  __pycache__  solution.py
user@samal-dimdung3:~/pylabs$ cat solution.py 
#./solution.py

from mybackup import MyBackup
import logging
import sys
import glob

#start the main
if __name__ == "__main__":

#get the arguments from the command line
    backupdir = sys.argv[1]
    zipfile_name = sys.argv[2]

#start logging
    logging.basicConfig(filename='backup.log',
                        format='%(asctime)s- %(levelname)s: %(message)s',
                        level=logging.DEBUG)
#create the backup object
    logging.info("Creating the backup object")
    bkupobj = MyBackup()
#set the backup directory
    logging.info("Setting the directory to backup")
    if bkupobj.check_directory(backupdir):
        bkupobj.dir_to_backup = backupdir
    else:
        logging.error("Directory %s does not exist. Exiting" % backupdir)
        sys.exit()
#set the zipfile
    logging.info("Setting the zipfile")
    bkupobj.backup_file = bkupobj.check_zipfile(zipfile_name)
#backup the directory
    logging.info("Backing up the directory")
    for name in glob.glob(bkupobj.dir_to_backup):
        logging.info("Backing up the following file: %s" % name)
    bkupobj.zip_directory()
user@samal-dimdung3:~/pylabs$ 
