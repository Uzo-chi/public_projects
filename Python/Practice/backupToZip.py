# backupToZip.py - Copies an entire folder and its content into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    
    folder = os.path.abspath(folder) # make sure folder is absolute
    
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
        
    # Create the ZIP file.
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' %(foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
    print('Done.')
    
backupToZip('C:\\delicious')