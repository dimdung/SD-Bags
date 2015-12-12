#./mybackup.py

import os
import zipfile
import glob


class MyBackup:
    """
    This is a utility class to backup local files in a directory to a zip
    archive
    """

    def __init__(self, zipfile=None, backupdir=None):
        """
        Initilize data elements for the backup object
        """
        self.dir_to_backup = backupdir
        self.backup_file = zipfile

    def check_directory(self, chkdir):
        """
        Checks for the existence of a directory and returns the
        directory name
        """
        if os.path.exists(chkdir):
            if os.path.isdir(chkdir):
                return chkdir

    def check_zipfile(self, chkzip):
        """
        Checks for the existence of the zipfile and returns a
        zipfile object in the correct mode.
        """

        if os.path.exists(chkzip):
            return zipfile.ZipFile(chkzip, "a")
        else:
            return zipfile.ZipFile(chkzip, "w")

    def zip_directory(self):
        """
            Zips up the directory in the dir to backup attribute
            Assumes no subdirectory structure
        """
        for name in glob.glob(self.dir_to_backup + '/*'):
            self.backup_file.write(
                name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        self.backup_file.close()
~                                                                                                                                                                                    
"mybackup.py" 49L, 1308C            
