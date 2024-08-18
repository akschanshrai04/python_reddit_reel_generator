from moviepy.editor import *
from moviepy.video.VideoClip import ImageClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.fx.resize import resize
import random

def saveVideo(submission, bgcount, name):
    audio = AudioFileClip("./voicenotes/voice_{s}.mp3".format(s=submission.title[0:10]))
    duration = audio.duration
    nums = random.randint(1, bgcount)
    video = VideoFileClip("./background/{s}.mp4".format(s=nums)).subclip(0, duration)
    redditauthor = ImageClip("./screenshots/author_{s}.png".format(s=submission.title[0:10])).set_duration(5).set_pos("top", "center").margin(top=400, opacity=0)
    reddittitle = ImageClip("./screenshots/title_{s}.png".format(s=submission.title[0:10])).set_duration(5).set_pos("top", "center").margin(top=450, opacity=0)
    image1 = redditauthor.resize(1.5)
    image2 = reddittitle.resize(1.5)
    video.audio = CompositeAudioClip([audio])
    final = CompositeVideoClip([video, image1, image2])
    final.write_videofile("./output/final_output_{s}.mp4".format(s=name))