# from pytube import Playlist

# playlist = Playlist('https://www.youtube.com/playlist?list=PLoVy-85EFtK92qMfHTNZi0BAA3T1AbDys')
# print("Total number of videos: " + str(len(playlist.videos)))
# for video in playlist.videos:
#     try:
#         video.streams.\
#             filter(type='video', progressive=True, file_extension='mp4').\
#             order_by('resolution').\
#             desc().\
#             first().\
#             download()
#     except Exception as e: 
#         print('exception in : {} with url : {}'.format(video.title, video.watch_url))



import os
from glob import glob

files = glob("*.mp4")

for fileName in files:
    newList = fileName.split(" ")
    if newList[2] == "Do":
        newName = "_".join(newList[3:])
    else:
        newName = "_".join(newList[2:])
        newName = newName[3:]
    print("Old Name is: {oldName}, and new name is: {newName}... ".format(oldName = fileName, newName = newName))
    os.rename(fileName, newName)