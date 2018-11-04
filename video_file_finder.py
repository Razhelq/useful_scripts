# video_file_finder.py - searches for videofile inside given directory

import os

def video_search(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize('{}\\{}'.format(foldername, filename))*(0.000001) > 5 and \
                (filename.endswith('.mkv') or filename.endswith('.avi') or \
                filename.endswith('.wmv') or filename.endswith('.rmvb') or \
                filename.endswith('.mp4') or filename.endswith('.wmv') or \
                filename.endswith('.flv')):

                print(os.path.join(foldername, filename))

video_search(os.path.abspath('.'))