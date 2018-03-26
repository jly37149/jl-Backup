import shutil
import os
import time

# List of source directories and destination
src_dir = ['your\source\path\or\paths']
dst_dir = 'your\destination\path'

# Copytree only works if dest is empty
def checkD():
    global dst_dir
    if os.path.isdir(dst_dir):
        time.sleep(1)
        ts = time.time() # timestamp
        dst_dir = dst_dir + str(ts)

# Copy from source to dest
def backup():
    global src_dir
    global dst_dir
    print("Starting backup ... ")
    try:
        for i in src_dir:
            checkD()
            shutil.copytree(i, dst_dir)
            print("Next ...")
        print("Backup complete!")
    except:
        print("Backup failed!")

# Start of main
backup()

