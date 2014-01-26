import os
import sys

rootdir = sys.argv[1]

for root, folders, files in os.walk(rootdir):
    for directory in folders:
        files = [f for f in os.listdir(os.path.join(root, directory))]
        if not 'cover.jpg' in files: print os.path.join(root,directory)
