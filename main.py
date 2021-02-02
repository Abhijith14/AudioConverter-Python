import os
from moviepy.editor import *


inVideo = "C:/Users/ABHIJITH UDAYAKUMAR/PycharmProjects/AudioConverter/Video"

VidData = os.listdir(inVideo)
count = 0
for i in VidData:
    print()
    count = count + 1
    toAudio = "C:/Users/ABHIJITH UDAYAKUMAR/PycharmProjects/AudioConverter/Audio"
    AudData = i[:-4]
    AudData = AudData + ".mp3"
    print("Starting #" + str(count))

    video = VideoFileClip(os.path.join(inVideo, i))
    video.audio.write_audiofile(os.path.join(toAudio, AudData))
    print("Finished. " + str(len(VidData) - count) + " remaining...")
    print()