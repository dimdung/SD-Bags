user@samal-dimdung3:~/pylabs$ cat bkupscript.py 
#./bkupscript.py

from mybackup import MyBackup
import logging
import zipfile

#start the main
if __name__ == "__main__":
#start logging
    logging.basicConfig(filename='backup.log',
                        format='%(asctime)s- %(levelname)s: %(message)s',
                        level=logging.DEBUG)
#create the backup object
    logging.info("Creating the backup object")
     
#set the backup directory
    logging.info("Setting the directory to backup")
    
#set the zipfile
    logging.info("Setting the zipfile")
     
    #backup the directory
    logging.info("Backing up the directory")
    
user@samal-dimdung3:~/pylabs$ 
